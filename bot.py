from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8733211848:AA......FAeSp1kWmU6fArFvxJQHmREzVQmvej23I"



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 Mira AI is online.\n\nCommands:\n/idea\n/money\n/caption"
    )


async def idea(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 App Idea:\nAI WhatsApp TV Caption Generator"
    )


async def money(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Monetization:\nCharge creators monthly for viral captions."
    )


async def caption(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📢 Hustle silently until success becomes noise."
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("idea", idea))
app.add_handler(CommandHandler("money", money))
app.add_handler(CommandHandler("caption", caption))

print("Bot is running...")

app.run_polling()
