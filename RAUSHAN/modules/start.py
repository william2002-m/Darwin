import random
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import EMOJIOS, IMG, STICKER
from RAUSHAN import BOT_NAME, AMBOT, dev
from RAUSHAN.database.chats import add_served_chat
from RAUSHAN.database.users import add_served_user
from RAUSHAN.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


@dev.on_message(filters.command(["start", "aistart"]) & ~filters.bot)
async def start(_, m: Message):
    try:
        if m.chat.type == ChatType.PRIVATE:
            accha = await m.reply_text(
                text=random.choice(EMOJIOS),
            )
            await asyncio.sleep(1.3)

            # Handle message edit with different content
            messages = [
                "__ᴋᴇᴇʀᴛʜɪ ʜᴇʀᴇ..__",
                "__sᴛᴀʀᴛɪɴɢ..__",
                "__sᴛᴀʀᴛᴇᴅ..__"
            ]
            for msg in messages:
                if accha.text != msg:  # Check if content is different
                    await accha.edit(msg)
                await asyncio.sleep(0.2)

            await accha.delete()

            umm = await m.reply_sticker(sticker=random.choice(STICKER))
            await asyncio.sleep(2)
            await umm.delete()

            await m.reply_photo(
                photo=random.choice(IMG),
                caption=f"""**╭───────────────────⦿**\n**│⛩️ ʜᴇʏ ɪ ᴀᴍ {BOT_NAME} •**\n**├───────────────────⦿**\n**│-꩜> ɪ ʀᴇᴀᴅ ʏᴏᴜʀ ᴍɪɴᴅ •**\n**│⚡︎ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ •**\n**├───────────────────⦿**\n**│ꑭ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs •**\n**│☘ ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ •**\n**│✿ ғᴏʀ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ •**\n**│✇ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ] •**\n**│𖣐 ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ •**\n**│🔥 24x7 ᴛɪᴍᴇ ᴏɴʟɪɴᴇ •**\n**├───────────────────⦿**\n**│🦊 ᴍᴀᴅᴇ ʙʏ...[𝙈𝙖𝙧𝙬𝙞𝙣🤍](https://t.me/Shunn_Mizushino)**\n**╰───────────────────⦿""",
                reply_markup=InlineKeyboardMarkup(DEV_OP),
            )
            await add_served_user(m.from_user.id)
        else:
            await m.reply_photo(
                photo=random.choice(IMG),
                caption=START,
                reply_markup=InlineKeyboardMarkup(HELP_START),
            )
            await add_served_chat(m.chat.id)

    except Exception as e:
        print(f"Error in start command: {e}")


@dev.on_message(filters.command(["help"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def help(client: AMBOT, m: Message):
    try:
        if m.chat.type == ChatType.PRIVATE:
            hmm = await m.reply_photo(
                photo=random.choice(IMG),
                caption=HELP_READ,
                reply_markup=InlineKeyboardMarkup(HELP_BTN),
            )
            await add_served_user(m.from_user.id)
        else:
            await m.reply_photo(
                photo=random.choice(IMG),
                caption="**❍ ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
                reply_markup=InlineKeyboardMarkup(HELP_BUTN),
            )
            await add_served_chat(m.chat.id)

    except Exception as e:
        print(f"Error in help command: {e}")


@dev.on_message(filters.command("repo") & ~filters.bot)
async def repo(_, m: Message):
    try:
        await m.reply_text(
            text=SOURCE_READ,
            reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
            disable_web_page_preview=True,
        )
    except Exception as e:
        print(f"Error in repo command: {e}")


@dev.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    try:
        for member in m.new_chat_members:
            await m.reply_photo(photo=random.choice(IMG), caption=START)
    except Exception as e:
        print(f"Error in welcome command: {e}")
