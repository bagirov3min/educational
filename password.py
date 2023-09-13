import random


def start() -> None:
    """Функция, определяющая количество генерируемых паролей"""
    global quantity
    print("Эта программа помогает сгенерировать пароль")
    quantity = input("Введите необходимое количество паролей для генерации:\n")
    while quantity.isdigit() == False or int(quantity) == 0:
        quantity = input("Введите пожалуйста ЦЕЛОЕ число, не равное нулю:\n")
    for _ in range(int(quantity)):
        choice_settings()


def choice_settings() -> list[str] | str:
    """Функция выбора настроек генерируемого пароля"""
    # Создаем строки
    settings = {
        "digits": ("0123456789", "цифры"),
        "lowercase_letters": ("abcdefghijklmnopqrstuvwxyz", "буквы нижнего регистра"),
        "uppercase_letters": ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "буквы верхнего регистра"),
        "punctuation": ("!#$%&*+-=?@^_.", "символы"),
        "ambiguous": ("il1Lo0O", "неочевидные символы 'il1Lo0O'"),
    }

    chars = []
    # Добавляем строки в список в соответствии с выбранными параметрами
    for key, (value, description) in settings.items():
        answer = input(f"Наберите 1, если хотите использовать {description}: ")

        if answer.lower() == "1":
            chars.extend(value)
        elif key == "ambiguous" and answer.lower() != "1":
            for char in value:
                if char in chars:
                    chars.remove(char)

    # Проверяем содержит ли список строки после параметризации
    if len(chars) == 0:
        print("Вы не выбрали ни один из предложенных вариантов символов")
        return choice_settings()
    return pass_choice(chars)


def pass_choice(chars: list) -> str:
    """Функция генерации пароля. Возвращает сгенерированный пароль"""
    global password
    password = list()
    for _ in range(random.randint(8, 17)):
        password += random.choice(chars)
    print("Ваш пароль сгенерирован:\n", *password, sep="")

start()
