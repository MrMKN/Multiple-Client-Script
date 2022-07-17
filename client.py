from pyrogram import Client
import os

BOT_TOKEN_1 = os.environ.get("BOT_TOKEN_1", "")
BOT_TOKEN_2 = os.environ.get("BOT_TOKEN_2", "")                             
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")

App = Client("app1", bot_token=BOT_TOKEN_2, api_id=API_ID, api_hash=API_HASH)
App.start()
                                         
Bot = Client("app2", bot_token=BOT_TOKEN_1, api_id=API_ID, api_hash=API_HASH)
Bot.start()

       


       




