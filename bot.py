import asyncio
from pyrogram import Client, compose, idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5873664112:AAEMhsbdC4TCLp_efpJXw9eWeqg1dmREdaM")
API_ID = int(os.environ.get("API_ID", "23906038"))
API_HASH = os.environ.get("API_HASH", "dff1eb42fad7971f16da662a99c0f376")
STRING = os.environ.get("STRING", "BQFsxvYASF2KNfHPjeWo0LQfgFYomldGggEHiFN5rvkgigZEoOrbR29b_WHnIzYgC2B7fnsRl14BmLlppOmVAToXa4gRth5RjPxK9cbGFWNGF31UQxc5WkTlOUW2fucV7-RIh5frKvP2rGQOQWHKvD5q_eyqNcslUU3HPwPcMu8ye5rDUilqjqx6V6CsbqQ_T7cv4mnVB8gWOMZ819_Nz7DS_aNVc3oJ3slLwCHLlqQu756HCY7tTzQESH4EXbGmpDj5tn4HXvyW62PbKnMKzbe27jzGUWUcrg4fzhtKAH0jaL9xeBwGlzYYckzfEYxmRqNGLljC4M2f-mW-1_ERnckrYNlZTQAAAAE2-ZleAA")


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
