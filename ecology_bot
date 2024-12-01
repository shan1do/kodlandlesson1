import telebot as tbot
import os
import random
from data_plastic import data


token = '7632191782:AAGHk7MVQP0vBKQEKmo1SslRQF5uJ9Qc2Ts'
bot = tbot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
    
text_messages = {'start - Запуск бота \n plastic - Поделки из пластика + инструкция'}
    
@bot.message_handler(commands= ['help'])
def help(message):
    bot.reply_to(message, text_messages)
    
    
    
@bot.message_handler(commands= ['plastic'])
def plactic(message):
    img_name = random.choice(os.listdir('crafts'))
    with open(f'crafts/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f, caption= data[f'crafts/{img_name}'])
        
        
waste_sorting = {
    "пластиковая бутылка": {
        "advice": "Отдать на переработку",
        "image": "https://metalbaki.ru/wp-content/uploads/2017/02/konteiner-dla-rso-1.gif"
    },
    "стеклянная бутылка": {
        "advice": "Отдать на переработку",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPaK17mGUC2Jj7t0K5SeUvmXV0JBIWr2TUag&s"
    },
    "алюминиевая банка": {
        "advice": "Отдать на переработку",
        "image": "https://citibin.ru/wp-content/uploads/2018/10/jubilee_paper_07.jpg"
    },
    "макулатура": {
        "advice": "Отдать на переработку",
        "image": "https://rusbin.ru/wp-content/uploads/2018/02/urna_edge_paper_4.jpg"
    },
    "остатки пищи": {
        "advice": "Выбросить в обычную урну",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTq0q4UT0dJsNVtTAYN39ynKEQ191z23ixEdg&s"
    },
    
}


def sort_waste(item):
    return waste_sorting.get(item.lower(), None)


@bot.message_handler(commands=['waste'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Напишите название предмета, и я подскажу, как его утилизировать.")


@bot.message_handler(func=lambda message: True)
def send_sorting_advice(message):
    item = message.text
    sorting_info = sort_waste(item)
    
    if sorting_info:
        advice = sorting_info['advice']
        image_url = sorting_info['image']
        bot.send_message(message.chat.id, advice)
        bot.send_photo(message.chat.id, image_url)
    else:
        bot.send_message(message.chat.id, "Информация не найдена.")
    
    


decay_times = {
    "пластиковая бутылка": 450,
    "стеклянная бутылка": 1000,
    "алюминиевая банка": 200,
    "макулатура": 2,               
    "полиэтиленовый пакет": 100,  
    "остальные пищевые отходы": 1, 
    "обычный мусор": 10,
    "одежда из синтетики": 20,
    "деревянные предметы": 10,
    "памперсы": 500,
}


def get_decay_time(item):
    return decay_times.get(item.lower(), "Информация не найдена.")


@bot.message_handler(commands=['decay'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Напишите мне название бытового предмета, и я расскажу, сколько времени он разлагается.")


@bot.message_handler(func=lambda message: True)
def send_decay_time(message):
    item = message.text
    decay_time = get_decay_time(item)
    bot.send_message(message.chat.id, f"Время разложения '{item}': {decay_time} лет.")
  

    
    
    
        

        
        
        
        


print('Бот запущен')
bot.polling()
