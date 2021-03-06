#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:52:17 2020

@author: deniszagorodnev
"""

import os
import time
import logging

import telebot
from telebot import apihelper

# Logger
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

# Configuration
TG_PROXY = 'https://103.241.156.250:8080'
TG_BOT_TOKEN = 'xxxxxxxx'

# Set proxy
apihelper.proxy = {'http': TG_PROXY}

# Init bot
bot = telebot.TeleBot(TG_BOT_TOKEN)

# /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

# Plain message
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Polling
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logger.error(e)
        time.sleep(15)