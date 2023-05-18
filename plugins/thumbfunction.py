from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client,message):
		print(message.chat.id)
		thumb = find(int(message.chat.id))[0]
		if thumb :
			await client.send_photo(message.chat.id,photo =f"{thumb}")
		else:
			await message.reply_text("**You don't have any custom thumbnail**")

@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client, message):
    chat_id = message.chat.id
    delthumb(int(chat_id))
    await message.reply_text("**Custom thumbnail deleted successfully**")

@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    chat_id = message.chat.id
    file_id = str(message.photo.file_id)
    addthumb(chat_id, file_id)
    await message.reply_text("**Custom thumbnail saved successfully** ✅")
