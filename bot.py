import config
import telebot
import random
import os
import time

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music1/'):
        if file.split('.')[-1] == 'ogg':
            f = open("music1/" + file, 'rb')
            res = bot.send_voice(message.chat.id, f, None)
            print(res)
        time.sleep(3)


if __name__ == '__main__':
    bot.polling(none_stop=True)
