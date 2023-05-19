import os
import asyncio
import time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from helper.database import getid, delete

ADMIN = int(os.environ.get("ADMIN", "5217294686"))

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if message.reply_to_message:
        ms = await message.reply_text("Getting all IDs from the database...\nPlease wait")
        ids = getid()
        total = len(ids)
        success = 0
        failed = 0
        await ms.edit(f"Starting broadcast...\nSending message to {total} users")
        for chat_id in ids:
            try:
                time.sleep(1)
                await message.reply_to_message.copy(chat_id)
                success += 1
            except:
                failed += 1
                delete({"_id": chat_id})
                pass
            try:
                await ms.edit(f"Message sent to {success} chat(s). {failed} chat(s) failed to receive the message.\nTotal: {total}")
            except FloodWait as e:
                await asyncio.sleep(e.x)
