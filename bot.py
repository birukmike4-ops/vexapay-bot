from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

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
            "📋 Complete these tasks:\n\n"
            "📢 Telegram: https://t.me/VexaPayOfficial\n"
            "▶️ YouTube: https://www.youtube.com/@VexaPayOfficial\n"
            "🎵 TikTok: https://tiktok.com/@vexapayofficial\n"
            "📷 Instagram: https://www.instagram.com/vexapayofficial"
        )

    elif text == "👥 Invite Friends":
        await update.message.reply_text("Invite friends feature is coming soon.")

    elif text == "🏆 Top Winners":
        await update.message.reply_text("Top Winners feature is coming soon.")

    elif text == "💰 My Wallet":
        await update.message.reply_text("Your balance: 0 Points")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

app.run_polling()
