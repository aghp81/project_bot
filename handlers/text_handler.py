from telegram import Update
from telegram.ext import ContextTypes
from services.nlp import extract_event_info

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    event_info = extract_event_info(user_message)
    if event_info["datetime"]:
        response = f"""
📅 زمان رویداد: {event_info['datetime']}
📝 عنوان: {event_info['title']}
"""
    else:
        response = f"📝 متن شما دریافت شد اما زمان مشخصی پیدا نشد:\n{event_info['title']}"

    await update.message.reply_text(response)
