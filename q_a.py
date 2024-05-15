# Словарь q_a содержит вопросы и варианты ответов
Q_A = {
    "Как перейти в другую директорию?": {
        "cd dir": True,
        "pwd": "https://habr.com/ru/articles/775630/",
        "rm": "https://habr.com/ru/articles/775630/",
    },
    "Как удалить файл?": {
        "pwd": "https://habr.com/ru/articles/775630/",
        "cd dir": "https://habr.com/ru/articles/775630/",
        "rm": True,
    },
    "Как узнать текущую директорию?": {
        "rm": "https://habr.com/ru/articles/775630/",
        "cd dir": "https://habr.com/ru/articles/775630/",
        "pwd": True,
    },
    "Как вывести ваши текущие активные процессы?": {
        "grep": "https://losst.pro/komanda-ps-v-linux",
        "ps": True,
        "fg": "https://losst.pro/komanda-ps-v-linux",
    },
    "Как показать все запущенный процессы?": {
        "top": True,
        "grep": "https://losst.pro/komanda-top-v-linux",
        "fg": "https://losst.pro/komanda-top-v-linux",
    },
    "Как посмотреть список файлов и каталогов?": {
        "top": "https://losst.pro/komanda-ls-linux",
        "ls": True,
        "fg": "https://losst.pro/komanda-ls-linux",
    },
    "Как посмотреть документацию?": {
        "man": True,
        "whatis": "https://losst.pro/chto-takoe-man",
        "whoami": "https://losst.pro/chto-takoe-man",
    },
    "Как посмотреть информацию о команде?": {
        "whatis": "https://teamtutorials.com/other-tutorials/how-to-help-command-in-linux",
        "whoami": "https://teamtutorials.com/other-tutorials/how-to-help-command-in-linux",
        "--help": True,
    },
    "Как посмотреть свой идентификатор?": {
        "man": "https://andreyex.ru/operacionnaya-sistema-linux/komanda-whoami-v-linux/",
        "whatis": "https://andreyex.ru/operacionnaya-sistema-linux/komanda-whoami-v-linux/",
        "whoami": True,
    },
    "Как вывести содержимое файла на экран?": {
        "man": "https://losst.pro/komanda-cat-linux#ispolzovanie-cat-v-linux",
        "whatis": "https://losst.pro/komanda-cat-linux#ispolzovanie-cat-v-linux",
        "cat": True,
    },
    "Как постранично посмотреть содержимое файла?": {
        "man": "https://losst.pro/komanda-more-v-linux",
        "more": True,
        "cat": "https://losst.pro/komanda-more-v-linux",
    },
    "Как сменить права доступа?": {
        "mod": "https://losst.pro/komanda-chmod-linux",
        "chmod": True,
        "chmd": "https://losst.pro/komanda-chmod-linux",
    },
    "Как создать архив с расширением .tar?": {
        "tar cf": True,
        "tar xf": "https://losst.pro/komanda-tar-v-linux",
        "tar czf": "https://losst.pro/komanda-tar-v-linux",
    },
    "Как распаковать архив с расширением .tar?": {
        "tar cf": "https://losst.pro/komanda-tar-v-linux",
        "tar xf": True,
        "tar czf": "https://losst.pro/komanda-tar-v-linux",
    },
    "Как создать архив с расширением .gzip?": {
        "tar cf": "https://losst.pro/komanda-tar-v-linux",
        "tar xf": "https://losst.pro/komanda-tar-v-linux",
        "tar czf": True,
    },
    "Как распаковать архив с расширением .gzip?": {
        "tar cf": "https://losst.pro/komanda-tar-v-linux",
        "tar xzf": True,
        "tar czf": "https://losst.pro/komanda-tar-v-linux",
    },
    "Как убить процесс с id pid?": {
        "kill pid": True,
        "kill fish": "https://losst.pro/kak-ubit-protsess-linux",
        "kill pig": "https://losst.pro/kak-ubit-protsess-linux",
    },
    "Как проверить хост?": {
        "ssh host": "https://losst.pro/komanda-ping-v-linux",
        "more host": "https://losst.pro/komanda-ping-v-linux",
        "ping host": True,
    },
    "Как узнать использование памяти и swap?": {
        "top": "https://losst.pro/ispolzovanie-operativnoj-pamyati-linux",
        "free": True,
        "ps": "https://losst.pro/ispolzovanie-operativnoj-pamyati-linux",
    },
    "Как подключиться к хосту(host) как пользователь(user)?": {
        "ssh user@host": True,
        "ping user@host": "https://losst.pro/kak-polzovatsya-ssh",
        "wget user@host": "https://losst.pro/kak-polzovatsya-ssh",
    },
}