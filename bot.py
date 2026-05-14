import mimetypes
import sys

sys.modules['imghdr'] = mimetypes

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

TOKEN = "8703254616:AAEPFb_0RutEEwvy-vfeZBDPb7-JMi2IFmU"

menu = [
    ["📋 អ្នកជំងឺថ្មី", "📂 ស្វែងរកអ្នកជំងឺ"]
]

reply_markup = ReplyKeyboardMarkup(menu, resize_keyboard=True)

patients = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ស្វាគមន៍មកកាន់ Clinic Bot",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "📋 អ្នកជំងឺថ្មី":
        await update.message.reply_text("ផ្ញើឈ្មោះអ្នកជំងឺ")
        context.user_data["waiting"] = True

    elif context.user_data.get("waiting"):

        patients.append(text)

        await update.message.reply_text(
            f"បានរក្សាទុក: {text}"
        )

        context.user_data["waiting"] = False

    elif text == "📂 ស្វែងរកអ្នកជំងឺ":

        if len(patients) == 0:
            await update.message.reply_text("មិនមានទិន្នន័យ")

        else:
            result = "\n".join(patients)

            await update.message.reply_text(result)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(filters.TEXT, handle_message)
)

print("Bot Running...")

app.run_polling()