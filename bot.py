import os
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
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

def start(update, context):
    keyboard = [
        ["📋 Tasks"],
        ["👥 Invite Friends"],
        ["🏆 Top Winners"],
        ["💰 My Wallet"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(
        "👋 Welcome to VexaPay Official!\n\nChoose an option:",
        reply_markup=reply_markup
    )

def buttons(update, context):
    text = update.message.text

    if text == "📋 Tasks":
        update.message.reply_text(
            "🏆 **Complete these tasks to earn rewards:**\n\n"
            "✅ **Telegram:** https://t.me/VexaPayOfficial\n"
            "✅ **YouTube:** https://www.youtube.com/@VexaPayOfficial\n"
            "✅ **TikTok:** https://tiktok.com/@vexapayofficial\n"
            "📸 **Instagram:** https://www.instagram.com/vexapayofficial"
        )
    elif text == "👥 Invite Friends":
        update.message.reply_text("👥 Invite friends feature is coming soon.")
    elif text == "🏆 Top Winners":
        update.message.reply_text("🥇 Top Winners feature is coming soon.")
    elif text == "💰 My Wallet":
        update.message.reply_text("💰 Your balance: 0 Points")

def main():
    # Start Flask in a background thread
    Thread(target=run_flask, daemon=True).start()

    # Start Telegram Bot (v13.15 style)
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, buttons))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
