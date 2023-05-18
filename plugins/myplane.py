import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.database import (
    find_one, used_limit, daily as daily_, uploadlimit, usertype
)
from helper.progress import humanbytes
from helper.date import check_expi
from datetime import timedelta, date, datetime

@Client.on_message(filters.private & filters.command(["myplan"]))
async def start(client, message):
    used_ = find_one(message.from_user.id)
    daily = used_["daily"]
    expi = daily - int(time.mktime(time.strptime(str(date.today()), '%Y-%m-%d')))
    if expi != 0:
        today = date.today()
        pattern = '%Y-%m-%d'
        epcho = int(time.mktime(time.strptime(str(today), pattern)))
        daily_(message.from_user.id, epcho)
        used_limit(message.from_user.id, 0)
    _newus = find_one(message.from_user.id)
    used = _newus["used_limit"]
    limit = _newus["uploadlimit"]
    remain = int(limit) - int(used)
    user = _newus["usertype"]
    ends = _newus["prexdate"]
    if ends:
        pre_check = check_expi(ends)
        if not pre_check:
            uploadlimit(message.from_user.id, 1288490188)
            usertype(message.from_user.id, "Free")
    if ends is None:
        text = f"User ID: ```{message.from_user.id}```\nPlan: {user}\nDaily Upload Limit: {humanbytes(limit)}\nToday Used: {humanbytes(used)}\nRemain: {humanbytes(remain)}"
    else:
        normal_date = datetime.fromtimestamp(ends).strftime('%Y-%m-%d')
        text = f"User ID: ```{message.from_user.id}```\nPlan: {user}\nDaily Upload Limit: {humanbytes(limit)}\nToday Used: {humanbytes(used)}\nRemain: {humanbytes(remain)}\n\nYour Plan Ends On: {normal_date}"

    if user == "Free":
        await message.reply(text, quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💰 Upgrade", callback_data="upgrade"), InlineKeyboardButton("Cancel ✖️", callback_data="cancel")]]))
    else:
        await message.reply(text, quote=True)
