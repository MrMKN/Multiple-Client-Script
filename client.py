from pyrogram import Client, filters
import os

BOT_TOKEN_1 = os.environ.get("BOT_TOKEN_1", "")
BOT_TOKEN_2 = os.environ.get("BOT_TOKEN_2", "")                             
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
                        
class Bot:
    App1 = Client("app1", bot_token=BOT_TOKEN_2, api_id=API_ID, api_hash=API_HASH),                                           
    App2 = Client("app2", bot_token=BOT_TOKEN_1, api_id=API_ID, api_hash=API_HASH),

        
       
@App1.on_message(filters.text)
async def first_start(client, message):
    await message.reply_text(
        text="Hello Bro 😉 i am bot1")


@App2.on_message(filters.text)
async def second_start(client, message):
    await message.reply_text(
        text="Hello Bro 😉 i am bot2")


       
print("bot starting success full 🔥....")        
Bot.run()


