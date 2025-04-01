from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("sᴇᴀʀᴄʜ", callback_data="mplus help_search"),
    InlineKeyboardButton("ɪᴍᴀɢᴇ", callback_data="mplus help_image"), 
    InlineKeyboardButton("ᴇxᴛʀᴀ", callback_data="mplus help_extra")], 
    
    [InlineKeyboardButton("ɪᴍᴘᴏsᴛᴇʀ", callback_data="mplus help_imposter"), 
    InlineKeyboardButton("ғᴏɴᴛ", callback_data="mplus help_font"), 
    InlineKeyboardButton("ᴛᴀɢ-ᴀʟʟ", callback_data="mplus help_tagall")], 
    
    [InlineKeyboardButton("ᴄʜᴀᴛɢᴘᴛ", callback_data="mplus help_chatgpt"), 
    InlineKeyboardButton("ᴛʀᴜᴛʜ-ᴅᴀʀᴇ", callback_data="mplus help_td"), 
    InlineKeyboardButton("ғᴜɴ", callback_data="mplus help_fun")], 
    
    [InlineKeyboardButton("ɪɴꜰᴏ", callback_data="mplus help_info"), 
    InlineKeyboardButton("ɢʀᴏᴜᴘ", callback_data="mplus help_group"), 
    InlineKeyboardButton("ᴛᴛs", callback_data="mplus help_tts")], 
    
    [InlineKeyboardButton("ɢᴀᴍᴇs", callback_data="mplus help_game"), 
    InlineKeyboardButton("ᴀᴄᴛɪᴏɴ", callback_data="mplus help_action"), 
    InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="mplus help_sticker")], 
    
    [InlineKeyboardButton("Ⓣ-ɢʀᴀᴘʜ", callback_data="mplus help_tg"), 
    InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="mplus help_q"), 
    InlineKeyboardButton("ʜᴀsᴛᴀɢ", callback_data="mplus help_ht")],  
    
    [InlineKeyboardButton("", callback_data="settings_back_helper"), 
    InlineKeyboardButton("↞ ʀᴇᴛᴜʀɴ", callback_data="managebot123 settings_back_helper")]
    ]
