from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from saptasree import app  # Import the app instance from the main bot file
import random
import asyncio

# Luhn algorithm and other functions go here...

@app.on_message(filters.command("ccgen"))
async def ccgen_handler(client: Client, message: Message):
    # Your card generation logic
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
    # Handle regeneration callback
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
    # Handle sending the .txt file
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
