from pyrogram import Client, filters 
import os

BOT_TOKEN_1 = os.environ.get("BOT_TOKEN_1", "")
BOT_TOKEN_2 = os.environ.get("BOT_TOKEN_2", "")                             
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
API_ID2 = API_ID
API_HASH2 = API_HASH

app = Client("app1", bot_token=BOT_TOKEN_2, api_id=API_ID, api_hash=API_HASH)
bot = Client("bot", bot_token=BOT_TOKEN_1, api_id=API_ID2, api_hash=API_HASH2)                                       #123
         
@app.on_message(filters.text)
async def first_start(client, message):
    await message.reply_text(
        text="Hello Bro 😉 i am bot1")

@bot.on_message(filters.text)
async def second_start(client, message):
    await message.reply_text(
        text="Hello Bro 😉 i am bot2")
                               

app.run()                 
bot.run()

       


       



























#123
