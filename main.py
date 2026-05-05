import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")
URL = os.getenv("RENDER_EXTERNAL_URL")  # auto from Render

app = Flask(__name__)
bot_app = ApplicationBuilder().token(TOKEN).build()

# Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is live on webhook 🚀")

bot_app.add_handler(CommandHandler("start", start))

# Webhook route
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    bot_app.update_queue.put_nowait(update)
    return "ok"

# Home route (important for Render)
@app.route("/")
def home():
    return "Bot is running"

if __name__ == "__main__":
    bot_app.bot.set_webhook(f"{URL}/{TOKEN}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
