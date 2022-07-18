from pyrogram import Client, idle, filters
from pyro-tester.Script import START
import os

BOT_TOKEN_1 = os.environ.get("BOT_TOKEN_1", "")
BOT_TOKEN_2 = os.environ.get("BOT_TOKEN_2", "")                             
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
API_ID2 = API_ID
API_HASH2 = API_HASH

app = Client("app", bot_token=BOT_TOKEN_2, api_id=API_ID, api_hash=API_HASH)
bot = Client("bot", bot_token=BOT_TOKEN_1, api_id=API_ID2, api_hash=API_HASH2)                                       #123
         
@app.on_message(filters.text)
async def first_start(client, message):
    await message.reply_text(
        text=f"""Hello {message.from_user.mention} 👋

Sorry This bot is unauthorized 😔
Please use our new bot @MKN_Hyper_renameBOT

OR contact our support group @MKN_BOTZ_DISCUSSION_GROUP""")

@app.on_message(filters.command("t"))
async def test(client, message):
    await message.reply_text(text=START)


@bot.on_message(filters.text)
async def second_start(client, message):
    await message.reply_text(
        text=f"""Hello {message.from_user.mention} 👋

Sorry This bot is unauthorized 😔
Please use our new bot @MKN_ProRenameBOT

OR contact our support group @PYRO_BOTZ_CHAT""")
                               

app.start()     
bot.start()

idle()

app.stop()
bot.stop()

       


       



























#123
