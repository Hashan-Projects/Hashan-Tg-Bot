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
        bot.reply_to(message,"My Master is in Telegram @HashanDimuthu")

@bot.message_handler(commands=["website"])
def send_message(message):
        bot.reply_to(message,"https://hashandimuthu.github.io")

@bot.message_handler(commands=["about"])
def send_message(message):
        bot.reply_to(message,"Hello I Am Hashan I Am 16 Years Old I Am A Devloper From Sri Lanka I Am A Student Yet I Am Learning Some Programming Languages There Are Java And Python I Want To Be A Full Stack DEVLOPER And I Am Looking To Help You")

bot.polling()
