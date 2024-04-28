import random

import telebot
from telebot.types import ReplyKeyboardRemove

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

q_a = {
    'Как перейти в другую директорию?': {
        'cd dir': True,
        'pwd': 'https://habr.com/ru/articles/775630/',
        'rm': 'https://habr.com/ru/articles/775630/'
    },
    'Как удалить файл?': {
        'pwd': 'https://habr.com/ru/articles/775630/',
        'cd dir': 'https://habr.com/ru/articles/775630/',
        'rm': True
    },
    'Как узнать текущую директорию?': {
        'rm': 'https://habr.com/ru/articles/775630/',
        'cd dir': 'https://habr.com/ru/articles/775630/',
        'pwd': True,
    },
    'Как вывести ваши текущие активные процессы?': {
        'top': 'https://losst.pro/komanda-ps-v-linux',
        'ps': True,
        'fg': 'https://losst.pro/komanda-ps-v-linux'
    },
    'Как показать все запущенный процессы?': {
        'top': True,
        'ps': 'https://losst.pro/komanda-top-v-linux',
        'fg': 'https://losst.pro/komanda-top-v-linux'
    },
    'Как посмотреть список файлов и каталогов?': {
        'top': 'https://losst.pro/komanda-ls-linux',
        'ls': True,
        'fg': 'https://losst.pro/komanda-ls-linux'
    },
    'Как посмотреть документацию?': {
        'man': True,
        'whatis': 'https://losst.pro/chto-takoe-man',
        'whoami': 'https://losst.pro/chto-takoe-man'
    },
    'Как посмотреть информацию о команде?': {
        'whatis': 'https://teamtutorials.com/other-tutorials/how-to-help-command-in-linux',
        'whoami': 'https://teamtutorials.com/other-tutorials/how-to-help-command-in-linux',
        '--help': True
    },
    'Как посмотреть свой идентификатор?': {
        'man': 'https://andreyex.ru/operacionnaya-sistema-linux/komanda-whoami-v-linux/',
        'whatis': 'https://andreyex.ru/operacionnaya-sistema-linux/komanda-whoami-v-linux/',
        'whoami': True
    }

}

user_data = {}


@bot.message_handler(
    func=lambda message: message.text == 'Начать тестирование')
def random_start(message):
    chat_id = message.chat.id
    user_data[chat_id] = {}
    user_data[chat_id]['counter'] = 0
    answer(message)


def answer(message):
    chat_id = message.chat.id

    if message.text not in q_a.keys() and message.text != 'Начать тестирование':
        for i in user_data[chat_id]:
            if user_data[chat_id][i] == None:

                if message.text not in q_a[i]:
                    bot.send_message(chat_id,
                                     f'❌ Неверный формат ответа')
                    bot.register_next_step_handler(message, answer)
                    return
                else:
                    user_data[chat_id][i] = message.text
                    ans = q_a[i][user_data[chat_id][i]]
                    if isinstance(ans, str):
                        bot.send_message(chat_id,
                                         f'❌ Ответ неверный, посетите:\n{ans}')

    if len(user_data[chat_id]) == len(q_a) or user_data[chat_id]['counter'] == 5:
        get_stats(message)
        return

    while True:
        random_question = random.choice(list(q_a.keys()))
        if random_question not in user_data[chat_id]:
            break

    user_data[chat_id]['counter'] += 1

    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []
    for i in q_a[random_question]:
        buttons.append(telebot.types.KeyboardButton(text=i))
    keyboard.add(*buttons)

    user_data[chat_id][random_question] = None
    bot.send_message(chat_id, random_question, reply_markup=keyboard)
    bot.register_next_step_handler(message, answer)


def get_stats(message):
    chat_id = message.chat.id
    correct_answer = 0
    for i in user_data[chat_id]:
        if i != 'counter' and isinstance(q_a[i][user_data[chat_id][i]], bool):
            correct_answer += 1
    bot.send_message(chat_id,
                     f'Отлично, количество верных ответов: {correct_answer}'
                     f'\nЧтобы пройти тест заново нажмите /start',
                     reply_markup=telebot.types.ReplyKeyboardRemove()
                     )


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton(text="Начать тестирование")
    keyboard.add(button1)
    bot.send_message(chat_id, 'Привет! Добро пожаловать! Тут кнопки',
                     reply_markup=keyboard)


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()


#поставить ограничение времени на вопросы