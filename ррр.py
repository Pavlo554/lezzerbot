import telebot
from telebot import types
from sqlighter import SQLighter
from cfg import *

# token
bot = telebot.TeleBot(TOKEN)
#Начало бд  В файле sqlighter.py там 4 вида подключение
db = SQLighter('db.db')
#конец бд

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Про нас")
    btn2 = types.KeyboardButton("Інформація")
    btn3 = types.KeyboardButton("Замовити сайт")
    btn4 = types.KeyboardButton("Сайти на нашій підтримці")
    btn5 = types.KeyboardButton("Підтримка Автора")
    btn6 = types.KeyboardButton("Я хочу купить сайт")
    btn7 = types.KeyboardButton("Коли працують скидки?")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id,text="Привет, меня звать LEZZER GAME STUDIO!\nЯкщо не пряцює бот то імоверно що світло на хостінгу пропало".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Про нас"):
        bot.send_message(message.chat.id, text="<b>Привіт Спасибо что читаешь статью!)\n</b>"
                                               "<b>Ми Украйнськая студия яка робить сайти для бізнесу і Проектов(ігрвих)</b>", parse_mode='html')

    elif (message.text == "Сайти на нашій підтримці"):
        bot.send_message(message.chat.id, text="<b>Наш сайт с підтримкой 24/7 - lezzer.com</b>", parse_mode='html')
    # Команда
    elif (message.text == "Інформація"):
        sti = open ('imgur/logo-1x.png','rb')
        bot.send_photo(message.chat.id, sti)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Наша студія❤️")
        btn2 = types.KeyboardButton("Як звати бота?")
        btn3 = types.KeyboardButton("Замовити сайт")
        btn4 = types.KeyboardButton("Підтримка Автора")
        btn5 = types.KeyboardButton("Я хочу купить сайт")
        btn6 = types.KeyboardButton("Коли працують скидки?")
        back = types.KeyboardButton("Повернутися до головного меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="<b>LGS – це невелика студія, що складається з команди розробників-самоучок, \nякі щодня оновлюють старі системи з минулого. Вони розробляють \nунікальні системи удосконалюючи старі. Вони працюють над продуктом у тісній співпраці. \nВід ідеї до результату, ви даєте нам ідею, а розробники реалізують якісно та оптимізовано. \nВони роблять все для гравців. Розробники - це ті, хто має за плечима понад 10 років ігрового досвіду.</b>", reply_markup=markup, parse_mode='html')
    # Команда
    elif (message.text == "Я хочу купить сайт"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Сайт - BUSINESS")
        button2 = types.KeyboardButton("Сайт - LITE")
        button3 = types.KeyboardButton("Сайт UCP - Сайт с личным кабинетом")
        button4 = types.KeyboardButton("Установка и настройка Telegram BOT")
        button5 = types.KeyboardButton("Цени")
        button6 = types.KeyboardButton("Коли працують скидки?")
        back = types.KeyboardButton('/start')
        markup.add(button1, button2, button3, button4, button5, button6, back)
        bot.send_message(message.chat.id, text="Вам открили пайс лист", reply_markup=markup)
    # Команда
    elif (message.text == "Замовити сайт"):
        sti = open ('imgur/prais.jpg','rb')
        bot.send_photo(message.chat.id, sti)
        bot.send_message(message.chat.id, "Щоб Замовити сайт можно подивится наш прайс лібо написать сюда @LEZZER_PROD на прямую с розробником")
    # Команда

    elif (message.text == "Коли працують скидки?"):
        bot.send_message(message.chat.id,"<b>🎅🏽Новий рік - 15% Скидка на всі товари👨🏽‍💻\nЧорная Пятниця - 50% Скидка на всі товари</b>",parse_mode='html')


    elif(message.text == "Підтримка Автора"):
        sit = open ('imgur/donate.jpg','rb')
        bot.send_photo(message.chat.id, sit)
        bot.send_message(message.chat.id, "Підтримку розробника @LEZZER_PROD на прямую \n\nПосиланя на донат - https://new.donatepay.ru/@327512 \n\n<b>Карта - 5375 4141 3369 1724 (monobank)</b>", parse_mode='html')
    
    elif (message.text == "Наша студія❤️"):
        bot.send_message(message.chat.id, "Наш телеграм - https://t.me/dev_lezzer_prod\n"
                                          "Наш Instogram - https://www.instagram.com/lezzer.games.studio/\n"
                                          "Наш Discord - https://discord.gg/uSp6VRASAf\n")
    # Команда
    elif (message.text =="Як звати бота?"):
        bot.send_message(message.chat.id, text="<b>Добре що ви мене спитали, мене мій розробник назвав як Мрія!\n"
                              "Я Украйнський Бот який працюе на LEZZER GAME STUDIO. мій розробником @LEZZER_PROD ❤️</b>".format(
                                message.from_user), parse_mode='html')
        #Сайт - BUSINESS
    elif (message.text =="Сайт - BUSINESS"):
        bot.send_message(message.chat.id, text="<b>Доброго дня ви согласні замовити сайт - Цена от 400 грн\n Платежна система - тик\n Після оплати напишить розробнику @LEZZER_PROD</b>".format(message.from_user), parse_mode='html')
        #Сайт - LITE
    elif (message.text =="Сайт - LITE"):
        bot.send_message(message.chat.id, text="<b>Доброго дня ви согласні замовити сайт - Цена от 300 грн\n Платежна система - тик\n Після оплати напишить розробнику @LEZZER_PROD</b>".format(message.from_user), parse_mode='html')
        # Сайт UCP - Сайт с личным кабинетом
    elif (message.text =="Сайт UCP - Сайт с личным кабинетом"):
        bot.send_message(message.chat.id, text="<b>Доброго дня ви согласні замовити сайт - Цена от 1.000 грн\n Платежна система - тик\n Після оплати напишить розробнику @LEZZER_PROD</b>".format(message.from_user), parse_mode='html')
        #Установка и настройка Telegram BOT
    elif (message.text =="Установка и настройка Telegram BOT"):
        bot.send_message(message.chat.id, text="<b>Доброго дня ви согласні замовити сайт - Цена от 1.000 грн\n Платежна система - тик\n Після оплати напишить розробнику @LEZZER_PROD</b>".format(message.from_user), parse_mode='html')
        #Цени
    elif (message.text == "Цени"):
        sti = open('imgur/prais.jpg', 'rb')
        bot.send_photo(message.chat.id, sti)
        bot.send_message(message.chat.id,text="<b>Сайт - BUSINESS - Цена от 400 грн \nСайт - LITE - Цена от 300 грн\nСайт UCP - Сайт с личным кабинетом - Цена от 1.000 грн \nУстановка и настройка Telegram BOT - Цена от 1.000 грн\n Розробник @LEZZER_PROD \n Після оплати напишить розробнику</b>".format(message.from_user), parse_mode='html')

    else:
        bot.send_message(message.chat.id, text="<b>Я вас не розумію</b>".format(message.from_user), parse_mode='html')

bot.polling(none_stop=True)