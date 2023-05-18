import os
from pyrogram import Client, filters
from helper.database import botdata, find_one
from helper.progress import humanbytes

TOKEN = os.environ.get('TOKEN', '')
BOT_ID = TOKEN.split(':')[0]

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client, message):
    botdata(int(BOT_ID))
    data = find_one(int(BOT_ID))
    total_rename = data["total_rename"]
    total_size = data["total_size"]
    await message.reply_text(f"Creator: <a href='https://t.me/MinutesOnline'>👑 MinutesOnline 👑</a>\nLanguage: Python3\nLibrary: Pyrogram 2.0\nServer: Anywhere\nTotal Renamed Files: {total_rename}\nTotal Size Renamed: {humanbytes(int(total_size))}", quote=True)
