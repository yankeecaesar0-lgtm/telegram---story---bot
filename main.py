import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")
URL = os.getenv("RENDER_EXTERNAL_URL")

app = Flask(name)

bot_app = ApplicationBuilder().token(TOKEN).build()


bot_app.add_handler(CommandHandler("start", start))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    bot_app.update_queue.put_nowait(update)
    return "ok"


@app.route("/")
def home():
    return "Bot is running"

async def setup():
    await bot_app.initialize()
    await bot_app.start()
    await bot_app.bot.delete_webhook(drop_pending_updates=True)
    await bot_app.bot.set_webhook(f"{URL}/{TOKEN}")

if name == "main":
    asyncio.run(setup())
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
