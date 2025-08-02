from telegram.ext import ApplicationBuilder, MessageHandler, filters
from handlers.text_handler import handle_text
from handlers.voice_handler import handle_voice

TOKEN = "8266782644:AAFT1xYinsplKoew2JTscg7msa3-XuZ9QLg"

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # هندلر پیام متنی
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # هندلر پیام صوتی
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))

    print("ربات فعال شد. برای توقف Ctrl+C بزنید.")
    app.run_polling()

if __name__ == "__main__":
    main()
    