import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is running"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host="0.0.0.0", port=port)

TOKEN = os.getenv("8594936680:AAEA5qXLCbMRTp8TVUJz-C3Ti4cx_dIzAYQ")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message:
        await message.reply_text("Use /story or /startstory to begin!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

Thread(target=run_web).start()
app.run_polling()
