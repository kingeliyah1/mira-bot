from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8733211848:AA...EnpSxng_6ED_XqCR1c3LAUOu57eiv03yo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 Mira AI is online.\n\nCommands:\n/idea\n/money\n/caption"
    )

async def idea(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 App Idea:\nAI WhatsApp TV Caption Generator for Nigerian creators."
    )

async def money(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Monetization:\nCharge creators monthly for viral captions and content ideas."
    )

async def caption(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📢 Caption:\n'Hustle silently until your results become noise.'"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("idea", idea))
app.add_handler(CommandHandler("money", money))
app.add_handler(CommandHandler("caption", caption))

print("Bot is running...")
app.run_polling()
