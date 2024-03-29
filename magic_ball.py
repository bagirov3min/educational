import random

answer = [
    "Бесспорно",
    "Предрешено",
    "Никаких сомнений",
    "Определённо да",
    "Можешь быть уверен в этом",
    "Мне кажется - да",
    "Вероятнее всего",
    "Хорошие перспективы",
    "Знаки говорят - да",
    "Да",
    "Пока неясно, попробуй снова",
    "Спроси позже",
    "Лучше не рассказывать",
    "Сейчас нельзя предсказать",
    "Сконцентрируйся и спроси опять",
    "Даже не думай",
    "Мой ответ - нет",
    "По моим данным - нет",
    "Перспективы не очень хорошие",
    "Весьма сомнительно",
]


def greetings():
    """Функция приветствия"""
    s = input("Представляю вашему вниманию магический шар!\n" "Как тебя зовут?\n")
    print(
        "Привет,",
        s + "!",
    )
    return start()


def start():
    """Функция старта программы"""
    s = input('Чтобы начать набери "1", чтобы выйти из программы набери "2":\n').lower()
    while s != "1":
        if s != "2":
            s = input('Набери "1" или "2", чтобы продолжить:\n').lower()
        else:
            print("До скорой встречи!")
            return False
    return magic_print()


def magic_print():
    """Функция вывода ответа"""
    s = input(
        "Введи свой вопрос, на который можно ответить односложно(да или нет)\n"
        'Чтобы выйти из программы набери "2":\n'
    )
    while s != "2":
        print(random.choice(answer))
        s = input("Задай еще один вопрос\n" 'Чтобы выйти из программы набери "2":\n')
    return print("До скорой встречи!")


greetings()
