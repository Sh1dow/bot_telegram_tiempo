#!/usr/bin/python3
# -*- coding_ utf-8 -*- 
#pylint: disable= W0613, C0116
#type: ignore[union-attr]
#primer encuentro con un bot para aprender los primeros conceptos

"""
El bot tendra algunas funciones basicas handler functions (manipuladoras) estas funciones
despues se pasaran al Dispatcher (entrega) para ser posicionadas a sus lugares respectivos

luego el bot se unciara hasta que le hagamos CTRL+C

Echobot basico que nos dara un echo

"""

import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Insercion del token de la API

updater = Updater(token = '1318823004:AAEsNexeWxcihER_YF3img-hNeWUiHJh770', use_context = True)

#introduccion del dispatcher 

dispatcher = updater.dispatcher

#habilitando el LOGGING

logging.basicConfig(format='%(asctime)s -%(name)s - &(levelname)s - %(message)s', level = logging.INFO)

def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text = "SOY TU NUEVO BOT, HABLAME <3") # el objetivo de esto es recivir el mensaje cuando le añadamos /start

def echo(update, context): 
	context.bot.send_message(chat_id=update.effective_chat.id, text = update.message.text) #me gustaria saber que hace esa ultima asignacion al texto
	 
#handler del start
start_handler = CommandHandler('start' , start)
dispatcher.add_handler(start_handler)

#handler del echo, filtra el mensaje
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


updater.start_polling() 

