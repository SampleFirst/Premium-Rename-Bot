import asyncio
from pyrogram import Client, compose, idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5873664112:AAEMhsbdC4TCLp_efpJXw9eWeqg1dmREdaM")
API_ID = int(os.environ.get("API_ID", "23906038"))
API_HASH = os.environ.get("API_HASH", "dff1eb42fad7971f16da662a99c0f376")
STRING = os.environ.get("STRING", "")


def update_session_string(session_string):
    if 'use_export_session_string' in session_string:
        session_string = session_string.use_export_session_string()
    return session_string


# Create the bot client
bot = Client(
    "Renamer",
    bot_token=TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins')
)

# Check if STRING is present and update session string if needed
if STRING:
    STRING = update_session_string(STRING)

if STRING:
    apps = [Client2, bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()

else:
    bot.run()
