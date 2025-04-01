from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("sᴇᴀʀᴄʜ", callback_data="mplus HELP_Search"), 
                InlineKeyboardButton("ɢᴀᴍᴇs", callback_data="mplus HELP_Game"),
                InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="mplus HELP_Sticker")],

    [InlineKeyboardButton("ɪᴍᴘᴏsᴛᴇʀ", callback_data="mplus HELP_Imposter"), 
    InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="mplus HELP_Q"),
    InlineKeyboardButton("ᴀᴄᴛɪᴏɴ", callback_data="mplus HELP_Action")],

    [InlineKeyboardButton("ᴛᴀɢ-ᴀʟʟ", callback_data="mplus HELP_TagAll"), 
    InlineKeyboardButton("ᴇxᴛʀᴀ", callback_data="mplus HELP_Extra"),
    InlineKeyboardButton("ɪɴꜰᴏ", callback_data="mplus HELP_Info")],

    [InlineKeyboardButton("Ⓣ-ɢʀᴀᴘʜ", callback_data="mplus HELP_TG"),
    InlineKeyboardButton("ᴄʜᴀᴛɢᴘᴛ", callback_data="mplus HELP_ChatGPT"), 
    InlineKeyboardButton("ғᴏɴᴛ", callback_data="mplus HELP_Font")],

    [InlineKeyboardButton("ʜᴀsᴛᴀɢ", callback_data="mplus HELP_HT"), 
    InlineKeyboardButton("ᴛʀᴜᴛʜ-ᗪᴀʀᴇ", callback_data="mplus HELP_TD"),
    InlineKeyboardButton("ɢʀᴏᴜᴘs", callback_data="mplus HELP_Group")],

    [InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="mplus HELP_Sticker"), 
    InlineKeyboardButton("ɪᴍᴀɢᴇ", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("ᴛᴛs", callback_data="mplus HELP_TTS")],

    [InlineKeyboardButton("", callback_data=f"managebot123 settings_back_helper"), 
    InlineKeyboardButton("< ʀᴇᴛᴜʀɴ", callback_data=f"settings_back_helper")]
    ]
