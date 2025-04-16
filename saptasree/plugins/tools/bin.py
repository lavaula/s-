from aiogram import Router, types, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import random

router = Router(name="ccgen_plugin")

def luhn(card_number):
    def digits_of(n): return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_sum = sum(digits[-1::-2])
    even_sum = sum(sum(digits_of(2 * d)) for d in digits[-2::-2])
    return (odd_sum + even_sum) % 10 == 0

def generate_cc(bin_format):
    cards = []
    while len(cards) < 10:
        cc = ""
        for char in bin_format:
            if char == "x":
                cc += str(random.randint(0, 9))
            else:
                cc += char
        if luhn(cc):
            cards.append(cc)
    return cards

@router.message(F.text.startswith("/ccgen"))
async def handle_ccgen(message: types.Message):
    parts = message.text.split()
    if len(parts) < 2:
        return await message.reply("⚠️ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ʙɪɴ ʟɪᴋᴇ:\n`/ccgen 414720xxxxxx1010`", parse_mode="Markdown")
    
    bin_format = parts[1]
    try:
        cards = generate_cc(bin_format)
    except:
        return await message.reply("⚠️ ɪɴᴠᴀʟɪᴅ ʙɪɴ ғᴏʀᴍᴀᴛ.", parse_mode="Markdown")
    
    text = "**ʜᴇʀᴇ ᴀʀᴇ ʏᴏᴜʀ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴄᴀʀᴅs:**\n\n"
    text += "\n".join(f"`{card}`" for card in cards)

    button = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="🔁 ɢᴇɴᴇʀᴀᴛᴇ ᴀɢᴀɪɴ", callback_data=f"regen:{bin_format}")
    ]])
    await message.reply(text, reply_markup=button, parse_mode="Markdown")

@router.callback_query(F.data.startswith("regen:"))
async def regen_callback(query: CallbackQuery):
    bin_format = query.data.split(":", 1)[1]
    cards = generate_cc(bin_format)
    text = "**ʀᴇ-ɢᴇɴᴇʀᴀᴛᴇᴅ ᴄᴀʀᴅs:**\n\n"
    text += "\n".join(f"`{card}`" for card in cards)

    button = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="🔁 ɢᴇɴᴇʀᴀᴛᴇ ᴀɢᴀɪɴ", callback_data=f"regen:{bin_format}")
    ]])
    await query.message.edit_text(text, reply_markup=button, parse_mode="Markdown")
