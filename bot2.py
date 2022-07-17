from client import Bot
from pyrogram import filters 

@Bot.on_message(filters.text)
async def second_start(client, message):
    await message.reply_text(
        text="Hello Bro 😉 i am bot2")
