from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import random
import asyncio

# Luhn algorithm to validate
def luhn(card_number):
    def digits_of(n): return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_sum = sum(digits[-1::-2])
    even_sum = sum(sum(digits_of(2 * d)) for d in digits[-2::-2])
    return (odd_sum + even_sum) % 10 == 0

# Complete BIN to 16 digit
def complete_bin(bin_input):
    return bin_input + ('x' * (16 - len(bin_input))) if 'x' not in bin_input else bin_input

# Generate cards with CVV & expiry
def generate_cards(bin_input):
    bin_format = complete_bin(bin_input)
    cards = []
    while len(cards) < 10:
        cc = ""
        for ch in bin_format:
            cc += str(random.randint(0, 9)) if ch.lower() == "x" else ch
        if len(cc) == 16 and luhn(cc):
            mm = str(random.randint(1, 12)).zfill(2)
            yy = str(random.randint(26, 30))
            cvv = str(random.randint(100, 999))
            cards.append(f"{cc}|{mm}|{yy}|{cvv}")
    return cards

# Main command handler
@app.on_message(filters.command("ccgen"))
async def ccgen_handler(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply( "**⚠️ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ʙɪɴ!**\n\n**ᴇxᴀᴍᴘʟᴇ:**\n`/ccgen 414720`\n`/ccgen 414720xxxxxx1010`", quote=True)

    bin_input = message.command[1]
    cards = generate_cards(bin_input)
    card_text = "\n".join(cards)

    text = f"**⌬ ᴄᴀʀᴅ ɢᴇɴᴇʀᴀᴛᴏʀ**\n"
    text += f"**➥ ʙɪɴ:** `{bin_input}`\n"
    text += f"**➥ ǫᴛʏ:** `{len(cards)}`\n\n"
    text += "**╭── ɢᴇɴᴇʀᴀᴛᴇᴅ ᴄᴀʀᴅs ──╮**\n"
    text += "\n".join(f"`{c}`" for c in cards)
    text += "\n**╰────────────────────╯**"

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("◆ ʀᴇɢᴇɴᴇʀᴀᴛᴇ ◆", callback_data=f"regen_{bin_input}")],
        [InlineKeyboardButton("◆ ᴍᴀᴋᴇ ғɪʟᴇ ◆", callback_data=f"txt_{bin_input}")]
    ])

    await message.reply(text, reply_markup=buttons)

# Regenerate callback
@app.on_callback_query(filters.regex(r"^regen_(.+)"))
async def regenerate_cb(client, query: CallbackQuery):
    bin_input = query.data.split("_", 1)[1]
    cards = generate_cards(bin_input)

    text = f"**⌬ ᴄᴀʀᴅ ʀᴇɢᴇɴᴇʀᴀᴛᴇᴅ**\n"
    text += f"**➥ ʙɪɴ:** `{bin_input}`\n"
    text += f"**➥ ǫᴛʏ:** `{len(cards)}`\n\n"
    text += "**╭── ɴᴇᴡ ᴄᴀʀᴅs ──╮**\n"
    text += "\n".join(f"`{c}`" for c in cards)
    text += "\n**╰────────────────╯**"

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("◆ ʀᴇɢᴇɴᴇʀᴀᴛᴇ ◆", callback_data=f"regen_{bin_input}")],
        [InlineKeyboardButton("◆ ᴍᴀᴋᴇ ғɪʟᴇ ◆", callback_data=f"txt_{bin_input}")]
    ])

    try:
        await query.message.edit(text, reply_markup=buttons)
        await query.answer()
    except:
        await query.answer("ᴍᴇssᴀɢᴇ ᴛᴏᴏ ᴏʟᴅ ᴛᴏ ᴇᴅɪᴛ.", show_alert=True)

# TXT download callback
@app.on_callback_query(filters.regex(r"^txt_(.+)"))
async def send_txt_cb(client, query: CallbackQuery):
    bin_input = query.data.split("_", 1)[1]
    cards = generate_cards(bin_input)
    file_path = f"/tmp/{bin_input}_cards.txt"

    with open(file_path, "w") as f:
        for card in cards:
            f.write(card + "\n")

    await query.answer("sᴇɴᴅɪɴɢ ᴛxᴛ ғɪʟᴇ...", show_alert=False)
    await client.send_document(
        query.message.chat.id,
        file_path,
        caption=f"**ʙɪɴ:** `{bin_input}`\n**ɢᴇɴᴇʀᴀᴛᴇᴅ ᴄᴀʀᴅs:** `{len(cards)}`",
    )
    await asyncio.sleep(3)
