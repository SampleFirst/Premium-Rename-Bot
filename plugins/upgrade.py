from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client, filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot, update):
    text = """**Free Plan User**
    Daily Upload limit: 1.2GB
    Price: 0
    
    **🪙 Silver Tier 🪙** 
    Daily Upload limit: 10GB
    Price: Rs 60 / 🌎 $0.72 per Month
    
    **💫 Gold Tier 💫**
    Daily Upload limit: 25GB
    Price: Rs 110 / 🌎 $1.33 per Month
    
    **🔱 Platinum Tier 🔱**
    Daily Upload limit: 50GB
    Price: Rs 170 / 🌎 $2 per Month
    
    **💎 Diamond 💎**
    Daily Upload limit: 100GB
    Price: Rs 200 / 🌎 $2.4 per Month
    
    Pay Using UPI ID 
    
    After Payment, Send Screenshots of Payment to Admin @MinutesOnline"""
    
    keyboard = InlineKeyboardMarkup([[ 
        InlineKeyboardButton("ADMIN", url="https://t.me/MinutesOnline")], 
        [InlineKeyboardButton("Pay", url="https://t.me/MinutesOnline"),
        InlineKeyboardButton("Pay", url="https://t.me/MinutesOnline")],
        [InlineKeyboardButton("Cancel", callback_data="cancel")]])
    
    await update.message.edit(text=text, reply_markup=keyboard)

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot, message):
    text = """**Free Plan User**
    Daily Upload limit: 1.2GB
    Price: 0
    
    **🪙 Silver Tier 🪙** 
    Daily Upload limit: 10GB
    Price: Rs 60 / 🌎 $0.72 per Month
    
    **💫 Gold Tier 💫**
    Daily Upload limit: 25GB
    Price: Rs 110 / 🌎 $1.33 per Month
    
    **🔱 Platinum Tier 🔱**
    Daily Upload limit: 50GB
    Price: Rs 170 / 🌎 $2 per Month
    
    **💎 Diamond 💎**
    Daily Upload limit: 100GB
    Price: Rs 200 / 🌎 $2.4 per Month
    
    Pay Using UPI ID 
    
    After Payment, Send Screenshots of Payment to Admin @MinutesOnline"""
    
    keyboard = InlineKeyboardMarkup([[ 
        InlineKeyboardButton("ADMIN", url="https://t.me/MinutesOnline")], 
        [InlineKeyboardButton("Pay", url="https://t.me/MinutesOnline"),
        InlineKeyboardButton("Pay", url="https://t.me/MinutesOnline")],
        [InlineKeyboardButton("Cancel", callback_data="cancel")]])
    
    await message.reply_text(text=text, reply_markup=keyboard)
