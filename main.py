"""
Данный файл представляет Tg-бота https://t.me/Study_Linux_bot, который помогает
проверить знание командной строки Linux.
"""

import random
import time

import telebot
from loguru import logger

from config import TOKEN
from q_a import Q_A

# Выполняется логирование в файл debug.log в формате:
# время, уровень логирования, сообщение, частота записи нового файла, формат директории хранения файла
logger.add(
    "debug.log",
    format="{time}. {level}: {message}",
    level="ERROR",
    rotation="1 week",
    compression="zip",
)

bot = telebot.TeleBot(TOKEN)
MAX_TIME = 11  # Задается время ответа на вопрос



# user_data - словарь в котором находятся промежуточные пользовательские данные
user_data = {}


@bot.message_handler(func=lambda message: message.text == "Начать тестирование")
@logger.catch
def random_start(message: telebot.types.Message) -> None:
    """
    Выбирает рандомный вопрос.

    Выбирает рандомный вопрос; чтобы не было повторений, счетчик равен 0
    """
    chat_id = message.chat.id
    user_data[chat_id] = {}
    user_data[chat_id]["counter"] = 0
    answer(message)


@logger.catch
def answer(message: telebot.types.Message) -> None:
    """
    Обрабатывает ответы пользователя.

    Обрабатывает ответы пользователя.
    При вызове сообщения 'Начать тестирование',
    в цикле for происходит итерация в словарь user_data:
    если пользователь дает неверный ответ,
    то выводится сообщение "Неверный формат ответа"
    с рекомендацией по посещению сайта с теорией;
    если, пользователь не укладывается в лимит по времени,
    то выводится сообщение
    "К сожалению, вы не успели ответить на вопрос" и ответ не засчитывается;
    если пользователь дает верный ответ, то выводится сообщение "Ответ верный"

    Args:
        message: telebot.types.Message
    """

    chat_id = message.chat.id

    if message.text not in Q_A.keys() and message.text != "Начать тестирование":
        for i in user_data[chat_id]:
            if user_data[chat_id][i] == None:

                if message.text not in Q_A[i]:
                    keyboard = get_keyboard(i)
                    bot.send_message(
                        chat_id, f"❌ Неверный формат ответа", reply_markup=keyboard
                    )
                    bot.register_next_step_handler(message, answer)
                    return
                else:
                    user_data[chat_id][i] = message.text
                    ans = Q_A[i][user_data[chat_id][i]]
                    if isinstance(ans, str):
                        bot.send_message(
                            chat_id, f"❌ Ответ неверный, посетите:\n{ans}"
                        )
                    else:
                        if time.time() - user_data[chat_id]["time_start"] > MAX_TIME:
                            bot.send_message(
                                chat_id,
                                f"❌ К сожалению, вы не успели ответить на вопрос",
                            )
                            for j in Q_A[i]:
                                if Q_A[i][j] is not True:
                                    user_data[chat_id][i] = j

                        else:
                            bot.send_message(chat_id, f"✅ Ответ верный")

    if len(user_data[chat_id]) == len(Q_A) or user_data[chat_id]["counter"] == 5:
        get_stats(message)
        return

    while True:
        random_question = random.choice(list(Q_A.keys()))
        if random_question not in user_data[chat_id]:
            break

    user_data[chat_id]["counter"] += 1
    user_data[chat_id]["time_start"] = time.time()

    keyboard = get_keyboard(random_question)

    user_data[chat_id][random_question] = None
    bot.send_message(chat_id, random_question, reply_markup=keyboard)
    bot.register_next_step_handler(message, answer)


@logger.catch
def get_keyboard(random_question: str):
    """
    Вызов клавиатуры.

    Вызов клавиатуры для формирования вариантов ответа на вопросы.

    Args:
        random_question: str

    Returns:
        keyboard: telebot.types.ReplyKeyboardMarkup
    """
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []
    for i in Q_A[random_question]:
        buttons.append(telebot.types.KeyboardButton(text=i))
    keyboard.add(*buttons)
    return keyboard


@logger.catch
def get_stats(message: telebot.types.Message):
    """
    Вывод результатов тестирования.

    Выводится результат тестирования с указанием верных ответов.

    Args:
        message: telebot.types.Message
    """
    chat_id = message.chat.id
    correct_answer = 0
    for i in user_data[chat_id]:
        if i not in ("counter", "time_start") and isinstance(
            Q_A[i][user_data[chat_id][i]], bool
        ):
            correct_answer += 1
    bot.send_message(
        chat_id,
        f"Вы закончили тестирование. Количество верных ответов: {correct_answer}"
        f"\nЧтобы пройти тест заново нажмите /start",
        reply_markup=telebot.types.ReplyKeyboardRemove(),
    )


@bot.message_handler(commands=["start"])
@logger.catch
def welcome(message: telebot.types.Message) -> None:
    """
    Приветственное сообщение.

    Приветственное сообщение с описанием работы бота.

    Args:
        message: telebot.types.Message
    """
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton(text="Начать тестирование")
    keyboard.add(button1)
    bot.send_message(
        chat_id,
        "Привет! Добро пожаловать! "
        "Данный бот поможет проверить знание команд для работы "
        "в терминале Linux. "
        "Тестирование состоит из пяти вопросов, "
        "c тремя вариантами ответов. На каждый вопрос дается 7 секунд. "
        "В конце будет выведен результат тестирования. "
        'Для начала прохождения, необходимо нажать на кнопку '
        '"Начать тестирование". Удачи!',
        reply_markup=keyboard,
    )


if __name__ == "__main__":
    print("Бот запущен!")
    bot.infinity_polling()
