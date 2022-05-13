from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, CallbackContext
from datetime import datetime
from telegram import Update
import logging
from cred import token
from BotAPIs import *

TOKEN=token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"""List of Commands :

    /start ---> This message
    /date ---> today date
    /excuse ---> Get a random excuse
    /facts ---> Get a random fact
    /meme ---> Get a random meme
    /qt ---> Get a random Stoicism Quote
    /cp ---> Get cryptocurrencies price
    /contact ---> Contact info

{tozih} """)

async def qt(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Quotes.quote("https://api.themotivate365.com/stoic-quote")
    )

async def date(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=datetime.now().strftime("%x")
    )

async def excuse(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Excuse.excuse_maker('https://excuser.herokuapp.com/v1/excuse')
    )

async def meme(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Meme.meme('https://api.imgflip.com/get_memes')
    )
async def ufacts(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=UselessFacts.useless_facts('https://uselessfacts.jsph.pl/random.json?language=en')
    )


async def crypto(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Crypocurrencies.crypto('https://api.coinlore.net/api/tickers/?start=0&limit=25')
    )

async def contact(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="My Telegram ID : @Argonarty \
              My Gmail : Yasin10ar@gmail.com"
    )

# async def rmessage(update: Update, context: CallbackContext.DEFAULT_TYPE):
#     await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler=CommandHandler("start", start)
    date_handler=CommandHandler("date", date)
    exc_handler=CommandHandler("excuse", excuse)
    meme_handler=CommandHandler("meme", meme)
    qt_handler=CommandHandler("qt", qt)
    uf_handler=CommandHandler("facts", ufacts)
    cprice_handler=CommandHandler("cp", crypto)
    contact_handler=CommandHandler("contact", contact)
    message_handler = MessageHandler(filters.ALL ,start)
    application.add_handler(start_handler)
    application.add_handler(date_handler)
    application.add_handler(exc_handler)
    application.add_handler(uf_handler)
    application.add_handler(meme_handler)
    application.add_handler(qt_handler)
    application.add_handler(cprice_handler)
    application.add_handler(contact_handler)
    application.add_handler(message_handler)

    application.run_polling()
