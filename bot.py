import os
import asyncio
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from flask import Flask
from threading import Thread

# Flask App setup
app = Flask(__name__)

@app.route("/")
def home():
    return "VexaPay Bot is running successfully!"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# Telegram Bot setup
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📋 Tasks"],
        ["👥 Invite Friends"],
        ["🏆 Top Winners"],
        ["💰 My Wallet"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Welcome to VexaPay Official!\n\nChoose an option:",
        reply_markup=reply_markup
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📋 Tasks":
        await update.message.reply_text(
            "🏆 **Complete these tasks to earn rewards:**\n\n"
            "✅ **Telegram:** https://t.me\n"
            "✅ **YouTube:** https://youtube.com\n"
            "✅ **TikTok:** https://tiktok.com\n"
            "✅ **Instagram:** https://instagram.com"
        )
    elif text == "👥 Invite Friends":
        await update.message.reply_text("👥 Invite friends feature is coming soon.")
    elif text == "🏆 Top Winners":
        await update.message.reply_text("🥇 Top Winners feature is coming soon.")
    elif text == "💰 My Wallet":
        await update.message.reply_text("💰 Your balance: 0 Points")

def main():
    # Start Flask in a background thread so Render doesn't timeout
    Thread(target=run_flask, daemon=True).start()

    # Start Telegram Bot
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))
    
    application.run_polling()

if __name__ == "__main__":
    main()
