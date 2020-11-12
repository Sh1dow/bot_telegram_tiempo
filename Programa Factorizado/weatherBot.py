#!/usr/bin/pythont3
#-*- coding utf-8 -*-

import requests
from WeatherCls import weather
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update 


updater = Updater(token = '1318823004:AAEsNexeWxcihER_YF3img-hNeWUiHJh770', use_context = True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s -%(name)s - &(levelname)s - %(message)s', level = logging.INFO)

print("funcionando")

def paraguas (update, context):
    weather = WeatherCls.weather.rain()
     
    

    print(weather.rain())
    
    #context.bot.send_message(chat_id = update.effective_chat.id, text = weather)

    context.bot.send_message(chat_id = update.effective_chat.id, text = "todo bien")
#handler 

print("antes del handler")
paraguas_handler = CommandHandler('paraguas', paraguas)
dispatcher.add_handler(paraguas_handler)

updater.start_polling()
