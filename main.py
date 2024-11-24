
import telebot
import random
from main import generate_password
text_messages = {
    'welcome':
        u'Please welcome {name}!\n\n'
        u'This chat is intended for questions about and discussion of the pyTelegramBotAPI.\n'
        u'To enable group members to answer your questions fast and accurately, please make sure to study the '
        u'project\'s documentation (https://github.com/eternnoir/pyTelegramBotAPI/blob/master/README.md) and the '
        u'examples (https://github.com/eternnoir/pyTelegramBotAPI/tree/master/examples) first.\n\n'
        u'I hope you enjoy your stay here!',

    'info':
        u'My name is TeleBot,\n'
        u'I am a bot that assists these wonderful bot-creating people of this bot library group chat.\n'
        u'Also, I am still under development. Please improve my functionality by making a pull request! '
        u'Suggestions are also welcome, just drop them in this group chat!',

    'wrong_chat':
        u'Hi there!\nThanks for trying me out. However, this bot can only be used in the pyTelegramAPI group chat.\n'
        u'Join us!\n\n'
        u'https://telegram.me/joinchat/067e22c60035523fda8f6025ee87e30b'
}
def fiftyfifty():
    return random.choice(["Орёл", "Решка"])

def smile():
    return random.choice([":0", ";)", "oo", ":>"])
token = ""

    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(token)
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, message)
    print(message)
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    
@bot.message_handler(commands = ['generate_password'])
def gen_pas(message):
    bot.reply_to(message, generate_password(8))
    
@bot.message_handler(commands = ['smile'])
def smile(message):
    bot.reply_to(message, smile())  
    
@bot.message_handler(commands = ['monet'])
def fiftyfifty(message):
    bot.reply_to(message, fiftyfifty())
    
# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)    
    
@bot.message_handler(commands=['go'])
def on_start(message):
    bot.reply_to(message, text_messages['wrong_chat'])


@bot.message_handler(commands=['calc'])
def handle_text(message): 
    numvan = bot.send_message(message.chat.id, 'Введите первое число: ') 
    bot.register_next_step_handler(numvan ,num1_fun)

def num1_fun(message):
   global num1;
   num1 = message.text
   numtwo = bot.send_message(message.chat.id, 'Введите второе число: ')
   bot.register_next_step_handler(numtwo ,num2_fun)
   
def num2_fun(message):
    global num2;
    num2 = message.text      
    operu = bot.send_message(message.chat.id, 'Введите действие: ')
    bot.register_next_step_handler(operu ,operi)
    
def operi(message):
    global oper;
    oper = message.text
    if oper == "+":
        resylit = int(num1)+int(num2)
        bot.send_message(message.chat.id,resylit)
    elif oper == "-":
        resylit = int(num1)-int(num2)
        bot.send_message(message.chat.id,resylit)
    elif oper == "*":
        resylit = int(num1)*int(num2)
        bot.send_message(message.chat.id,resylit)
    elif oper == "/": 
        resylit = int(num1)/int(num2)
        bot.send_message(message.chat.id,resylit)
    elif oper == "**":
        resylit = int(num1)**int(num2)
        bot.send_message(message.chat.id,resylit)
    
    else:
        bot.send_message(message.chat.id,"ошибка ведите /calc")
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
    

    
    
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)    
    

def get_random_anime_image():
    url = "https://kitsu.io/api/edge/anime?filter[text]=tokio"
    res = requests.get(url)
    data = res.json()
    if 'data' in data and len(data['data']) > 0:
        random_anime = random.choice(data['data'])
        return random_anime['attributes']['posterImage']['medium']
    return None
    
    
 


@bot.message_handler(commands=['anime'])
def send_anime_image(message):
    image_url = get_random_anime_image()
    bot.send_photo(message.chat.id, image_url)

   
@bot.message_handler(commands=['mem'])
def send_mem(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)      
    
    
    
    
    
           
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
   

    
    

print("Бот запущен")
bot.polling()

