import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")
URL = os.getenv("RENDER_EXTERNAL_URL")

app = Flask(__name__)
bot_app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is live on webhook 🚀")

bot_app.add_handler(CommandHandler("start", start))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    bot_app.update_queue.put_nowait(update)
    return "ok"

@app.route("/")
def home():
    return "Bot is running"

if __name__ == "__main__":
    asyncio.run(bot_app.initialize())
    asyncio.run(bot_app.bot.set_webhook(f"{URL}/{TOKEN}"))
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
