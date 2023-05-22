import asyncio
from pyrogram import Client, compose, idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5873664112:AAEMhsbdC4TCLp_efpJXw9eWeqg1dmREdaM")
API_ID = int(os.environ.get("API_ID", "23906038"))
API_HASH = os.environ.get("API_HASH", "dff1eb42fad7971f16da662a99c0f376")
STRING = os.environ.get("STRING", "BQFsxvYAjTCvH2WI7jkNxYt_5vXnQQLorHinUWnE2kHWEP7S9jcQk972K65cBa38Oo4-_8yfk3dQIYiu5LCnuDSvTmEE6ocCNW13qcpILwtStp-eDOTYMIO8sGRcBXveX282YYW2Z6-iuWntcJ2-6NW4NReIyW9xktOnv4jS0USW1xHZUUr-yUB1gyRaHnS8vyrpoEZd7BPgS8WlGg7PmfUqBD-wEbuSZw99Oo5uDaNQdXkc-6B4rJn_3CDYomjycj1-wNlrjMOR-b52FP8co2e3vpjdDUvrb_W7izY-dEImVnbqKHipHR10ZgMeV58BHgpceIV96uZSCD1wQPwrZMesR5B0mgAAAAE2-ZleAA")


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
