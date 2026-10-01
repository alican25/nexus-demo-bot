
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from flask import Flask
​app = Flask('')
​@app.route('/')
def home():
return "Bot aktif ve calisiyor!"
​def run_web():
app.run(host='0.0.0.0', port=8080)
​async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text("Merhaba! Bot başarıyla çalışıyor.")
​def main():
token = os.environ.get("TOKEN")
if not token:
print("TOKEN bulunamadi!")
return
​import threading
t = threading.Thread(target=run_web)
t.start()
​application = ApplicationBuilder().token(token).build()
application.add_handler(CommandHandler("start", start))
​print("Bot baslatiliyor...")
application.run_polling()
​if __name__ == 'main':
main()
