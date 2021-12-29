import os
import telebot

bot = telebot.Telebot("API Key here")

@bot.message_handler(commands=["start"])
def send_welcome(message):
	 bot.reply_to(message,"Hello! I'm Hashan Dimuthu Chat Bot")

@bot.message_handler(commands=["youtube"])
def send_message(message):
	bot.reply_to(message,"https://www.youtube.com/channel/UCMb9Rcf7mh71x9glgb5oR8A")

@bot.message_handler(commands=["hashan"])
def send_message(message):
        bot.reply_to(message, "My Master is in Telegram @HashanDimuthu")

@bot.message_handler(commands=["website"])
def send_message(message):
        bot.reply_to(message, "https://hashandimuthu.github.io")

bot.polling()
