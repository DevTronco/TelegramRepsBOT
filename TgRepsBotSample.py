import telegram
from telegram import Update
import telegram.ext
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import difflib
import os


key = "YOUR_TOKEN"

# Add more products as needed
links = {
    #you put yours links here
}

async def handle_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.lower().strip()
    matches = difflib.get_close_matches(user_input, links.keys(), n=1, cutoff=0.8)

    if matches:
        best_match = matches[0]
        await update.message.reply_text(f"Ho trovato questo: {best_match}\nLink: {links[best_match]}")
    else:
        await update.message.reply_text("Non ho trovato nessun prodotto simile")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi. Please insert the product name ot gain the link.")

def main():
    app = ApplicationBuilder().token(key).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_msg))

    print("In execution...")
    app.run_polling()

if __name__ == "__main__":
    main()   