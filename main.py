import random
import time
from loguru import logger
import telebot
from telebot.types import ReplyKeyboardRemove
from config import TOKEN

logger.add('debug.log', format='{time}. {level}: {message}', level='ERROR',
           rotation='1 week', compression='zip')

bot = telebot.TeleBot(TOKEN)
MAX_TIME = 7

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
    },

    'Как вывести содержимое файла на экран?': {
        'man': 'https://losst.pro/komanda-cat-linux#ispolzovanie-cat-v-linux',
        'whatis': 'https://losst.pro/komanda-cat-linux#ispolzovanie-cat-v-linux',
        'cat': True
    },
    'Как постранично посмотреть содержимое файла?': {
        'man': 'https://losst.pro/komanda-more-v-linux',
        'more': True,
        'cat': 'https://losst.pro/komanda-more-v-linux'
    },
    'Как сменить права доступа?': {
        'mod': 'https://losst.pro/komanda-chmod-linux',
        'chmod': True,
        'chmd': 'https://losst.pro/komanda-chmod-linux'
    },
    'Как создать архив с расширением .tar?': {
        'tar cf': True,
        'tar xf': 'https://losst.pro/komanda-tar-v-linux',
        'tar czf': 'https://losst.pro/komanda-tar-v-linux'
    },
    'Как распаковать архив с расширением .tar?': {
        'tar cf': 'https://losst.pro/komanda-tar-v-linux',
        'tar xf': True,
        'tar czf': 'https://losst.pro/komanda-tar-v-linux'
    },
    'Как создать архив с расширением .gzip?': {
        'tar cf': 'https://losst.pro/komanda-tar-v-linux',
        'tar xf': 'https://losst.pro/komanda-tar-v-linux',
        'tar czf': True
    },
    'Как распаковать архив с расширением .gzip?': {
        'tar cf': 'https://losst.pro/komanda-tar-v-linux',
        'tar xzf': True,
        'tar czf': 'https://losst.pro/komanda-tar-v-linux'
    },
    'Как убить процесс с id pid?': {
        'kill pid': True,
        'kill fish': 'https://losst.pro/kak-ubit-protsess-linux',
        'kill pig': 'https://losst.pro/kak-ubit-protsess-linux'
    },
    'Как проверить хост?': {
        'ssh host': 'https://losst.pro/komanda-ping-v-linux',
        'more host': 'https://losst.pro/komanda-ping-v-linux',
        'ping host': True
    },
    'Как узнать использование памяти и swap?': {
        'top': 'https://losst.pro/ispolzovanie-operativnoj-pamyati-linux',
        'free': True,
        'ps': 'https://losst.pro/ispolzovanie-operativnoj-pamyati-linux'
    },
    'Как подключиться к хосту(host) как пользователь(user)?': {
        'ssh user@host': True,
        'ping user@host': 'https://losst.pro/kak-polzovatsya-ssh',
        'wget user@host': 'https://losst.pro/kak-polzovatsya-ssh'
    }
}

user_data = {}


@bot.message_handler(
    func=lambda message: message.text == 'Начать тестирование')
@logger.catch
def random_start(message):
    chat_id = message.chat.id
    user_data[chat_id] = {}
    user_data[chat_id]['counter'] = 0
    answer(message)


@logger.catch
def answer(message):
    chat_id = message.chat.id

    if message.text not in q_a.keys() and message.text != 'Начать тестирование':
        for i in user_data[chat_id]:
            if user_data[chat_id][i] == None:

                if message.text not in q_a[i]:
                    keyboard = get_keyboard(i)
                    bot.send_message(chat_id,
                                     f'❌ Неверный формат ответа', reply_markup=keyboard)
                    bot.register_next_step_handler(message, answer)
                    return
                else:
                    user_data[chat_id][i] = message.text
                    ans = q_a[i][user_data[chat_id][i]]
                    if isinstance(ans, str):
                        bot.send_message(chat_id,
                                         f'❌ Ответ неверный, посетите:\n{ans}')
                    else:
                        if time.time() - user_data[chat_id]['time_start'] > MAX_TIME:
                            bot.send_message(chat_id,
                                             f'❌ К сожалению, вы не успели ответить на вопрос')
                            for j in q_a[i]:
                                if q_a[i][j] is not True:
                                    user_data[chat_id][i] = j

                        else:
                            bot.send_message(chat_id,
                                             f'✅ Ответ верный')

    if len(user_data[chat_id]) == len(q_a) or user_data[chat_id]['counter'] == 5:
        get_stats(message)
        return

    while True:
        random_question = random.choice(list(q_a.keys()))
        if random_question not in user_data[chat_id]:
            break

    user_data[chat_id]['counter'] += 1
    user_data[chat_id]['time_start'] = time.time()

    keyboard = get_keyboard(random_question)

    user_data[chat_id][random_question] = None
    bot.send_message(chat_id, random_question, reply_markup=keyboard)
    bot.register_next_step_handler(message, answer)


@logger.catch
def get_keyboard(random_question):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []
    for i in q_a[random_question]:
        buttons.append(telebot.types.KeyboardButton(text=i))
    keyboard.add(*buttons)
    return keyboard


@logger.catch
def get_stats(message):
    chat_id = message.chat.id
    correct_answer = 0
    for i in user_data[chat_id]:
        if i not in ('counter', 'time_start') and isinstance(q_a[i][user_data[chat_id][i]], bool):
            correct_answer += 1
    bot.send_message(chat_id,
                     f'Вы закончили тестирование. Количество верных ответов: {correct_answer}'
                     f'\nЧтобы пройти тест заново нажмите /start',
                     reply_markup=telebot.types.ReplyKeyboardRemove()
                     )


@bot.message_handler(commands=['start'])
@logger.catch
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton(text="Начать тестирование")
    keyboard.add(button1)
    bot.send_message(chat_id,
                     'Привет! Добро пожаловать! Данный бот поможет проверить знание команд для работы в терминале Linux. '
                     'Тестирование состоит из пяти вопросов, c тремя вариантами ответов. На каждый вопрос дается 7 секунд. '
                     'В конце будет выведен результат тестирования. '
                     'Для начала прохождения, необходимо нажать на кнопку "Начать тестирование". Удачи!',
                     reply_markup=keyboard)


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()
