import telebot

from telebot import types
from sqlighter import *
from cfg import *

bot = telebot.TeleBot(TOKEN)
db = SQLighter('db.db')



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Про нас")
    btn2 = types.KeyboardButton("Інформація")
    btn3 = types.KeyboardButton("Замовити сайт")
    btn4 = types.KeyboardButton("Підтримка Автора")
    btn5 = types.KeyboardButton("Я хочу купить сайт")
    btn6 = types.KeyboardButton("Коли працюють знижки?")
    btn7 = types.KeyboardButton("Наша студія❤️")
    btn8 = types.KeyboardButton("Як звати бота?")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.chat.id, text="Привіт, меня звати Мрія!".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):

    if (message.text == "Я хочу купить сайт"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Сделать с 0 сайт")
        button2 = types.KeyboardButton("Верстка сайта")
        button3 = types.KeyboardButton("Сайт с личным кабинетом")
        button4 = types.KeyboardButton("Дизайн форума")
        button5 = types.KeyboardButton("Установка и настройка форума")
        button6 = types.KeyboardButton("Установка и настройка Telegram BOT")
        button7 = types.KeyboardButton("Цени")
        button8 = types.KeyboardButton('Повернутся на головну')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
        bot.send_message(message.chat.id, text="Вам открили пайс лист", reply_markup=markup)

    elif (message.text == "Про нас"):
        bot.send_message(message.chat.id, text="<b>Привіт Дякуємо, що читаєш статтю!)\n</b>"
                                               "<b>Ми Українська студія яка робить сайти для бізнесу та Проектів(ігрвих)</b>", parse_mode='html')

    elif (message.text == 'Повернутся на головну'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Про нас")
        btn2 = types.KeyboardButton("Інформація")
        btn3 = types.KeyboardButton("Замовити сайт")
        btn4 = types.KeyboardButton("Підтримка Автора")
        btn5 = types.KeyboardButton("Я хочу купить сайт")
        btn6 = types.KeyboardButton("Коли працюють знижки?")
        btn7 = types.KeyboardButton("Наша студія❤️")
        btn8 = types.KeyboardButton("Як звати бота?")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Головна!".format(message.from_user),reply_markup=markup)

    # Команда
    elif (message.text == "Інформація"):
        sti = open ('imgur/logo-1x.png','rb')
        bot.send_photo(message.chat.id, sti)
        bot.send_message(message.chat.id, text="<b>LGS – це невелика студія, що складається з команди розробників-самоучок, \nякі щодня оновлюють старі системи з минулого. Вони розробляють \nунікальні системи удосконалюючи старі. Вони працюють над продуктом у тісній співпраці. \nВід ідеї до результату, ви даєте нам ідею, а розробники реалізують якісно та оптимізовано. \nВони роблять все для гравців. Розробники - це ті, хто має за плечима понад 10 років ігрового досвіду.</b>", parse_mode='html')
    # Команда
    elif (message.text == "Замовити сайт"):
        sti = open ('imgur/prais.jpg','rb')
        bot.send_photo(message.chat.id, sti)
        bot.send_message(message.chat.id, "Щоб Замовити сайт можна подивитись наш прайс або написати сюди @LEZZER_PROD на пряму з розробником")
    # Команда

    elif (message.text == "Коли працюють знижки?"):
        bot.send_message(message.chat.id,"<b>\n🎅🏽Новий рік - 15% Скидка на всі товари👨🏽‍💻\n🖤Чорная Пятниця - 50% Скидка на всі товари🖤\n </b>",parse_mode='html')
    # Команда

    elif(message.text == "Підтримка Автора"):
        sit = open ('imgur/donate.jpg','rb')
        bot.send_photo(message.chat.id, sit)
        bot.send_message(message.chat.id, "Підтримка розробника @LEZZER_PROD на прямую \n\nПосиланя на донат - https://new.donatepay.ru/@327512 \n\n<b>Карта - 5375 4141 3369 1724 (monobank)</b>", parse_mode='html')
    # Команда

    elif (message.text == "Наша студія❤️"):
        bot.send_message(message.chat.id, "Наш телеграм - https://t.me/dev_lezzer_prod\n"
                                          "Наш Instogram - https://www.instagram.com/lezzer.games.studio/\n"
                                          "Наш Discord - https://discord.gg/uSp6VRASAf\n")
    # Команда
    elif (message.text =="Як звати бота?"):
        bot.send_message(message.chat.id, text="<b>Добре, що ви мене запитали, мене мій розробник назвав як Мрія!\n"
                              "Я Український Бот який працює на LEZZER GAME STUDIO. мій розробник @LEZZER_PROD ❤️</b>".format(
                                message.from_user), parse_mode='html')
        #Сайт - BUSINESS
    elif (message.text =="Сделать с 0 сайт"):
        bot.send_message(message.chat.id, text="<b>Доброго дня ви согласні замовити сайт - Цена от 1600 грн\nПлатежна система - тик\nПісля оплати напишить розробнику @LEZZER_PROD</b>".format(message.from_user), parse_mode='html')
        #Сайт - LITE
    elif (message.text =="Верстка сайта"):
        bot.send_message(message.chat.id, text="<b>Доброго дня ви согласні замовити сайт - Цена от 5000 грн\nПлатежна система - тик\nПісля оплати напишить розробнику @LEZZER_PROD</b>".format(message.from_user), parse_mode='html')
        # Сайт UCP - Сайт с личным кабинетом
    elif (message.text =="Сайт с личным кабинетом "):
        bot.send_message(message.chat.id, text="<b>Доброго дня ви согласні замовити сайт - Цена от 1.000 грн\nПлатежна система - тик\nПісля оплати напишить розробнику @LEZZER_PROD</b>".format(message.from_user), parse_mode='html')
        #Установка и настройка Telegram BOT
    elif (message.text =="Дизайн форума"):
        bot.send_message(message.chat.id, text="<b>Доброго дня ви согласні Дизайн форума - Цена от 200 грн\nПлатежна система - тик\nПісля оплати напишить розробнику @LEZZER_PROD</b>".format(message.from_user), parse_mode='html')
        
    elif (message.text =="Установка и настройка форума"):
        bot.send_message(message.chat.id, text="<b>Доброго дня ви согласні Установка и настройка форума - Цена от 150 грн\nПлатежна система - тик\nПісля оплати напишить розробнику @LEZZER_PROD</b>".format(message.from_user), parse_mode='html')

    elif (message.text =="Установка и настройка Telegram BOT"):
        bot.send_message(message.chat.id, text="<b>Доброго дня ви согласні замовити сайт - Цена от 1.000 грн\nПлатежна система - тик\nПісля оплати напишить розробнику @LEZZER_PROD</b>".format(message.from_user), parse_mode='html')
        #Цени
    elif (message.text == "Цени"):
        sti = open('imgur/prais.jpg', 'rb')
        bot.send_photo(message.chat.id, sti)
        bot.send_message(message.chat.id,text="<b>1. Сделать с 0 сайт - Цена от 1600 - грн \n2. Верстка сайта - Цена от 5000 грн\n3. Сайт с личным кабинетом  - Цена от 1.000 грн\n4. Дизайн форума - Цена от 200 грн\n5. Установка и настройка форума - Цена от 150 грн\n6.Установка и настройка Telegram BOT - Цена от 1.000 грн</b>".format(message.from_user), parse_mode='html')
        # Команда
    else:
        bot.send_message(message.chat.id, text="<b>Я вас не розумію</b>".format(message.from_user), parse_mode='html')
        #closse

bot.polling(none_stop=True)
