from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import datetime

def log(update: Update, context: ContextTypes.DEFAULT_TYPE,res,a,b) -> None:
    file = open('log.csv', 'a', encoding='utf-8')
    file.write(f'{datetime.datetime.now().time()}, {update.effective_user.first_name}, {a}+{b}={res} \n')
    file.close