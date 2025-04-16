import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
import aiohttp

# --- Config ---
API_ID = 26416419  # your api_id here
API_HASH = "c109c77f5823c847b1aeb7fbd4990cc4"
BOT_TOKEN = "6400675462:AAFlUPT3-RlVZ33MCqduP_6MaaSsx00e5Ak"
LOG_CHANNEL = "AotLogsVro"
LOG_MESSAGE_ID = 1091
NODES_BOT = "NodesGGbot"

# --- Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SaptasreeClone")

# --- Bot Client ---
bot = Client("saptasree-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- This will be initialized after loading session ---
user = None


async def get_string_session():
    """Fetch the string session from the log message in AotLogsVro."""
    async with Client("temp-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN) as temp:
        msg = await temp.get_messages(LOG_CHANNEL, LOG_MESSAGE_ID)
        return msg.text.strip()


@bot.on_message(filters.command("convert"))
async def handle_convert(_, message: Message):
    global user
    if not user:
        await message.reply("Initializing user session, please wait...")
        string = await get_string_session()
        user = Client(name="user-session", api_id=API_ID, api_hash=API_HASH, session_string=string)
        await user.start()

    query = message.text
    sender = message.from_user.id

    try:
        # Send query to NodesGGbot
        sent = await user.send_message(NODES_BOT, query)

        # Wait for reply
        @user.on_message(filters.chat(NODES_BOT))
        async def handle_reply(_, reply):
            # Send back to original user
            if reply.text:
                await message.reply_text(reply.text, parse_mode=ParseMode.MARKDOWN)
            elif reply.photo:
                await message.reply_photo(reply.photo.file_id, caption=reply.caption or "")
            elif reply.document:
                await message.reply_document(reply.document.file_id, caption=reply.caption or "")
            await sent.delete()
            return

    except Exception as e:
        await message.reply(f"Error: {e}")


# --- Start the bot ---
if __name__ == "__main__":
    bot.run()
