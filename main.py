import os
from telegram import Bot

TOKEN = os.getenv("TOKEN")

print("TOKEN =", repr(TOKEN))

bot = Bot(TOKEN)
print(bot.get_me())
