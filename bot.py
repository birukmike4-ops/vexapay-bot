async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📋 Tasks":
        await update.message.reply_text(
            "🏆 **Complete these tasks to earn rewards:**\n\n"
            "✅ **Telegram:** https://t.me/VexaPayOfficial\n"
            "✅ **YouTube:** https://www.youtube.com/@VexaPayOfficial\n"
            "✅ **TikTok:** https://tiktok.com/@vexapayofficial\n"
            "✅ **Instagram:** https://www.instagram.com/vexapayofficial"
        )
    elif text == "👥 Invite Friends":
        await update.message.reply_text("👥 Invite friends feature is coming soon.")
    elif text == "🏆 Top Winners":
        await update.message.reply_text("🥇 Top Winners feature is coming soon.")
    elif text == "💰 My Wallet":
        await update.message.reply_text("💰 Your balance: 0 Points")
