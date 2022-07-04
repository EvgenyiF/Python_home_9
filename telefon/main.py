from ast import Return, Str
from atexit import register
from logging import Filter
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, Updater, ConversationHandler
from write import *
from separator import *


TWO = 1
THREE = 2
FOUR = 3
FIVE = 4
SIX = 5
SEVEN = 6

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Введите Имя')
    return TWO
     

async def family(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global first_name
    first_name = update.message.text
    await update.message.reply_text(f"Введите Фамилию")
    return THREE

async def tel(update: Update, context: ContextTypes):
    global second_name
    second_name = update.message.text
    await update.message.reply_text('Введите телефон')
    return FOUR

     
async def commit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global telefon
    telefon = update.message.text
    await update.message.reply_text(f"Введите комментарий")
    return FIVE
    

async def resalt(update: Update, context: ContextTypes):
    global coment
    global b
    coment = update.message.text
    file = 'ucheniki.csv'
    b = [first_name, second_name,telefon,coment]
    await update.message.reply_text('"Выберите разделитель (1 =\ n) (2=:) (3=-) (4=*): "')
    return SIX

async def delimetr(update: Update, context: ContextTypes):
    global delim
    delim = int(update.message.text)
    y = get_separ(delim)
    file = 'tel.csv'
    writer(b,file,y)
    await update.message.reply_text(f'Информация Успешно добавлена \n {first_name}{y}{second_name}{y}{telefon}{y}{coment}')
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes):
    ConversationHandler.END

app = ApplicationBuilder().token("5484921901:AAF7OJVbEsiHSnUEuM417j5REfl0Mlm0QAQ").build()

start_handler = CommandHandler('start',start)
family_handler = MessageHandler(filters.TEXT,family)
tel_hendler = MessageHandler(filters.TEXT,tel)
comit_handler = MessageHandler(filters.TEXT,commit)
resalt_handler = MessageHandler(filters.TEXT,resalt)
delim_handler = MessageHandler(filters.TEXT,delimetr)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states ={TWO:[family_handler],
                                            THREE:[tel_hendler],
                                            FOUR: [comit_handler],
                                            FIVE:[resalt_handler],
                                            SIX:[delim_handler]},
                                    fallbacks=[cancel_handler])

app.add_handler(conv_handler)

app.run_polling()