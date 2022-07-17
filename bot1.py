from client import app
from pyrogram import filters 

@App.on_message(filters.text)
async def first_start(client, message):
    await message.reply_text(
        text="Hello Bro 😉 i am bot1")
