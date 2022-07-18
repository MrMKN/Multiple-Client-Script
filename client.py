from pyrogram import Client, idle, filters
import os

BOT_TOKEN_1 = os.environ.get("BOT_TOKEN_1", "")
BOT_TOKEN_2 = os.environ.get("BOT_TOKEN_2", "")                             
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
API_ID2 = API_ID
API_HASH2 = API_HASH

# start text
TEXT_1 = os.environ.get("TEXT_1", "")
TEXT_2 = os.environ.get("TEXT_2", "")

app = Client("app", bot_token=BOT_TOKEN_2, api_id=API_ID, api_hash=API_HASH)
bot = Client("bot", bot_token=BOT_TOKEN_1, api_id=API_ID2, api_hash=API_HASH2)                                       #123
         
@app.on_message(filters.command("start"))
async def first_start(client, message):
    await message.reply_text(text=TEXT_1)


@bot.on_message(filters.command("start"))
async def second_start(client, message):
    await message.reply_text(text=TEXT_2)
       
                               
app.start()     
bot.start()

idle()

app.stop()
bot.stop()

       


       



























#123
