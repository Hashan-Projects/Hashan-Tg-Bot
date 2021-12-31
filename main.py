#Created By @2021-Hashan Dimuthu All Right Reserved

import os
import telebot

bot = telebot.Telebot("API Key here")

@bot.message_handler(commands=["start"])
def send_welcome(message):
	 bot.reply_to(message,"𝓗𝓮𝓵𝓵𝓸 [{}](tg://user?id={})! 𝓘'𝓶 𝓗𝓪𝓼𝓱𝓪𝓷 𝓓𝓲𝓶𝓾𝓽𝓱𝓾'𝓼 𝓒𝓱𝓪𝓽 𝓑𝓸𝓽\n\n 𝓕𝓸𝓻 𝓢𝓽𝓪𝓻𝓽 𝓣𝓱𝓲𝓼 𝓑𝓸𝓽 : /start \n\n 𝓕𝓸𝓻 𝓯𝓲𝓷𝓭 𝓜𝔂 𝔂𝓸𝓾𝓽𝓾𝓫𝓮 : /youtube \n\n 𝓕𝓸𝓻 𝓜𝔂 𝓣𝓮𝓵𝓮𝓰𝓻𝓪𝓶 : /hashan \n\n 𝓕𝓲𝓷𝓭 𝓜𝔂 𝓸𝔀𝓷 𝔀𝓮𝓫𝓼𝓲𝓽𝓮 : /website \n\n  𝓕𝓸𝓻 𝓐𝓫𝓸𝓾𝓽 𝓜𝓮 : /about \n\n 𝓕𝓲𝓷𝓭 𝓜𝔂 𝓖𝓲𝓽𝓱𝓾𝓫 : /github")

@bot.message_handler(commands=["youtube"])
def send_message(message):
	bot.reply_to(message,"𝓣𝓱𝓲𝓼 𝓲𝓼 𝓶𝔂 𝓨𝓸𝓾𝓣𝓾𝓫𝓮 \n\n https://www.youtube.com/channel/UCMb9Rcf7mh71x9glgb5oR8A")

@bot.message_handler(commands=["hashan"])
def send_message(message):
        bot.reply_to(message,"𝓘 𝓪𝓶 𝓲𝓷 𝓣𝓮𝓵𝓮𝓰𝓻𝓪𝓶 @HashanDimuthu")

@bot.message_handler(commands=["website"])
def send_message(message):
        bot.reply_to(message,"𝓣𝓱𝓲𝓼 𝓲𝓼 𝓶𝔂 𝔀𝓮𝓫𝓼𝓲𝓽𝓮 \n\n https://hashandimuthu.github.io")

@bot.message_handler(commands=["about"])
def send_message(message):
        bot.reply_to(message,"𝓗𝓮𝓵𝓵𝓸 𝓘 𝓐𝓶 𝓗𝓪𝓼𝓱𝓪𝓷 𝓘 𝓐𝓶 17 𝓨𝓮𝓪𝓻𝓼 𝓞𝓵𝓭 𝓘 𝓐𝓶 𝓐 𝓓𝓮𝓿𝓵𝓸𝓹𝓮𝓻 𝓕𝓻𝓸𝓶 𝓢𝓻𝓲 𝓛𝓪𝓷𝓴𝓪 𝓘 𝓐𝓶 𝓐 𝓢𝓽𝓾𝓭𝓮𝓷𝓽 𝓨𝓮𝓽 𝓘 𝓐𝓶 𝓛𝓮𝓪𝓻𝓷𝓲𝓷𝓰 𝓢𝓸𝓶𝓮 𝓟𝓻𝓸𝓰𝓻𝓪𝓶𝓶𝓲𝓷𝓰 𝓛𝓪𝓷𝓰𝓾𝓪𝓰𝓮𝓼 𝓣𝓱𝓮𝓻𝓮 𝓐𝓻𝓮 𝓙𝓪𝓿𝓪 𝓐𝓷𝓭 𝓟𝔂𝓽𝓱𝓸𝓷 𝓘 𝓦𝓪𝓷𝓽 𝓣𝓸 𝓑𝓮 𝓐 𝓕𝓾𝓵𝓵 𝓢𝓽𝓪𝓬𝓴 𝓓𝓔𝓥𝓛𝓞𝓟𝓔𝓡 𝓐𝓷𝓭 𝓘 𝓐𝓶 𝓛𝓸𝓸𝓴𝓲𝓷𝓰 𝓣𝓸 𝓗𝓮𝓵𝓹 𝔂𝓸𝓾 𝓘 𝓪𝓶 𝓐𝓿𝓵𝓲𝓪𝓫𝓵𝓮 𝓸𝓷 𝓣𝓮𝓵𝓮𝓰𝓻𝓪𝓶 𝓪𝓼 @HashanDimuthu")

@bot.message_handler(commands=["github"])
def send_message(message):
        bot.reply_to(message,"𝓘 𝓪𝓶 𝓲𝓷 𝓖𝓲𝓽𝓱𝓾𝓫 \n\n https://github.com/HashanDimuthu")

bot.polling()
