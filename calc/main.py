from ast import Return, Str
from logging import Filter
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, Updater, ConversationHandler
from db import *




async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')

# def info(update: Update, context: ContextTypes):
#     update.message.reply_text('Меня создал Джонни')
ONE = 0
TWO = 1
THREE = 2
FOUR = 3
FIVE = 4
SIX = 5
SEVEN = 6

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #  log(update,context)
     await update.message.reply_text(f'Введите действительную часть')
     return ONE

async def input1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(update,context)
    global first_number
    first_number = update.message.text
    await update.message.reply_text(f"Введите мнимую часть")
    return TWO

async def input2(update: Update, context: ContextTypes):
    #  log(update,contt)
     global second_number
     global a
     second_number = update.message.text
     a = complex(int(first_number),int(second_number))
     print (a)
     await update.message.reply_text('Введите действительную часть 2 числа')
     return THREE

     
async def input3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(update,context)
    global first_number1
    first_number1 = update.message.text
    await update.message.reply_text(f"Введите мнимую часть 2 числа")
    return FOUR

async def input4(update: Update, context: ContextTypes):
    #  log(update,contt)
     global second_number1
     global b
     second_number1 = update.message.text
     b = complex(int(first_number1),int(second_number1))
     print (b)
     await update.message.reply_text('Введите операцию')
     return FIVE

async def resalt(update: Update, context: ContextTypes):
    operation = update.message.text
    if operation == '+':
        res = a+b
        await update.message.reply_text(f'{str(a)} + {str(b)} = {str(res)}')
    if operation == '-':
        res = a-b
        await update.message.reply_text(f'{str(a)} - {str(b)} = {str(res)}')
    if operation == '*':
        res = a*b
        await update.message.reply_text(f'{str(a)} * {str(b)} = {str(res)}')
    if operation == '/':
        res = a/b
        await update.message.reply_text(f'{str(a)} / {str(b)} = {str(res)}')
    log(update,context,res,a,b)
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes):
    ConversationHandler.END







app = ApplicationBuilder().token("").build()

start_handler = CommandHandler('start', start)
first_handler = MessageHandler(filters.TEXT, input1)
second_handler = MessageHandler(filters.TEXT, input2)
third_handler = MessageHandler(filters.TEXT, input3)
fourth_handler = MessageHandler(filters.TEXT, input4)
fifth_handler = MessageHandler(filters.TEXT, resalt)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states ={ONE:[first_handler],
                                            TWO:[second_handler],
                                            THREE:[third_handler],
                                            FOUR: [fourth_handler],
                                            FIVE:[fifth_handler]},
                                    fallbacks=[cancel_handler])

# app.add_handler(CommandHandler("hello", hello))
# # dispatcher.add_handler(CommandHandler("info", info))
# app.add_handler(CommandHandler('start', start))
# app.add_handler(MessageHandler(filters.TEXT, input1))
# app.add_handler(MessageHandler(filters.TEXT, input2))
app.add_handler(conv_handler)
app.run_polling()
