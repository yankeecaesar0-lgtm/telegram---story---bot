import os
import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

print("PTB version:", telegram.__version__)

TOKEN = os.getenv("8594936680:AAEA5qXLCbMRTp8TVUJz-C3Ti4cx_dIzAYQ")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /story or /startstory to begin!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
