
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

BOT_TOKEN = '8455698889:AAGaonB2zHMjKFIvWZDkgokd-Ksa8330vfs'  # 🔐 Your Token
CHAT_ID = '6105686395'  # Your Chat ID

# Mock stock prices
stock_data = {
    "TCS": "₹3755.25",
    "RELIANCE": "₹2845.10",
    "INFY": "₹1579.85"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to ZANGU Meme + Stock Bot!\nCommands:\n/meme\n/stock TCS")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📌 Commands:\n/meme – Random meme\n/stock TCS – Get stock price")

async def stock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        symbol = context.args[0].upper()
        price = stock_data.get(symbol, "❌ Stock not found.")
        await update.message.reply_text(f"📈 {symbol}: {price}")
    except:
        await update.message.reply_text("⚠️ Use: /stock TCS")

async def meme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        res = requests.get("https://meme-api.com/gimme").json()
        await update.message.reply_photo(photo=res['url'], caption=res['title'])
    except:
        await update.message.reply_text("❌ Couldn’t fetch meme.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stock", stock))
    app.add_handler(CommandHandler("meme", meme))
    print("🤖 ZANGU Bot running...")
    app.run_polling()
