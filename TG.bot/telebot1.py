import telebot
from telebot import types
import requests
import json

#API_GOOGLE = 'AIzaSyC80IDyeM8Qzau1me_KLuYyWZGQRLVkmDI'
API_TOKEN = '6180701510:AAEIKzrA5nAdH7M55wP4PMA3TP17fB2ujz0'
bot = telebot.TeleBot(API_TOKEN)
last_update_id = 0
            
#Кнопки
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Что ты умеешь?', 'Кто тебя сделал и зачем?')

#Приветствие
@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}. Благодарю что обратились ко мне.\n/help', reply_markup=keyboard1)

#gitHub
@bot.message_handler(commands = ['github'])
def github(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить github', url = 'https://github.com/VasiliiDev'))
    bot.send_message(message.chat.id, 'Мой github', reply_markup = markup)

#Help
@bot.message_handler(commands = ['help'])
def buttoms(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    github = types.KeyboardButton('/github')
    start = types.KeyboardButton('/start')
    composition = types.KeyboardButton('/composition')
    markup.add(start, github, composition)
    bot.send_message(message.chat.id, 'Вот список моих команд:', reply_markup = markup)

#Тех.Карты
@bot.message_handler(commands = ['composition'])
def composition(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Лимонады '))
    bot.send_message(message.chat.id, 'Вот их список')

#Ответы на разные сообщения
@bot.message_handler(content_types=['text'])
def send_text(message):
    print (f'Сообщение: {message.text} \nОтправитель: {message.from_user.first_name} {message.from_user.last_name} \nUsername: {message.from_user.username} \nID: {message.from_user.id}')
    if message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMsZGnsi8re0t1UhXNlCDpA1Z6qA7sAAgoAA8A2TxP_Da4-6A79CC8E')
        bot.send_message(message.chat.id, 'И я тебя:3')
    elif message.text.lower() == 'фото':
        photo = open ('1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text.lower() == 'что ты умеешь?':
        bot.send_message(message.chat.id, '/help')
    elif message.text.lower() == 'кто тебя сделал и зачем?':
        bot.send_message(message.chat.id, 'Я самый первый, почти разумный бот, сделанный начинающим разработчиком @A1mL0k, для упрощения работы в коллективе ресторан "Фибоначи"')
    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю')

#Ответ на фото
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, вот это да!!!')

#Узнать ID отправителя (file_id)
@bot.message_handler(content_types=['sticker'])
def send_message(message):
    print(message.sticker.file_id, message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)

#Пробую getUpdates
#bot.get_updates()

#Постоянная работа бота
bot.polling(none_stop=True)