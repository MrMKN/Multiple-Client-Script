from client import bot
from pyrogram import filters 

@bot.on_message(filters.text)
async def second_start(client, message):
    await message.reply_text(
        text="Hello Bro 😉 i am bot2")
