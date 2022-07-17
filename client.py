from pyrogram import Client, filters
import os

BOT_TOKEN_1 = os.environ.get("BOT_TOKEN_1", "")
BOT_TOKEN_2 = os.environ.get("BOT_TOKEN_2", "")                             
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")

##--------------------[(Client 1)]----------------

client1 = Client(
          "bot1",
          bot_token=BOT_TOKEN_1,
          api_id=API_ID,
          api_hash=API_HASH
)

@client1.on_message(filters.command("start"))
async def first_start(client, message):
    await message.reply_text(
        text="Hello Bro 😉 i am bot1")

print("bot1 starting success full 🔥....")        
client1.start()

##--------------------[(Client 2)]----------------
                        
client2 = Client(
          "app2",
          bot_token=BOT_TOKEN_2,
          api_id=API_ID,
          api_hash=API_HASH
)


@client2.on_message(filters.command("start"))
async def second_start(client, message):
    await message.reply_text(
        text="Hello Bro 😉 i am bot2")
       

print("bot2 starting success full 🔥....")
client2.start()

