# Имортируем библеотеки
import random

# Создаем списки символов и счетчик количества генерируемых паролей
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."
ambigous = "il1Lo0O"
quantity = 0


# Создаем начальную функцию, определяющуюю количество генерируемых паролей
# Функция возвращает функцию подсчета количества паролей
def start():
    global quantity
    print("Эта программа помогает сгенерировать пароль")
    print("Введите необходимое количество паролей для генерации:")
    quantity = input()
    while quantity.isdigit() == False or int(quantity) == 0:
        print("Введите пожалуйста ЦЕЛОЕ число, не равное нулю")
        quantity = input()
    quantity = int(quantity)
    return number_password()


# Создаем функцию подсчета количества генерируемых паролей
# Функция возвращает функцию выбора настроек пароля
def number_password():
    global quantity
    quantity -= 1
    return choice_settings()


# Функция выбора настроек пароля
# Возвращает функцию генерации пароля
# Или возвращает функцию заново, если не выбрана ни одна настройка
def choice_settings():
    pass_len = 0
    chars = list()
    print("Введите желаемую длину пароля")
    pass_len = input()
    while pass_len.isdigit() == False or int(pass_len) == 0:
        print("Введите пожалуйста ЦЕЛОЕ число, не равное нулю")
        pass_len = input()
    pass_len = int(pass_len)
    print("Выберите, использовать ли цифры?")
    print("Напишите да или нет")
    s_digit = input().lower()
    while s_digit != "да" and s_digit != "нет":
        print("Напишите да или нет")
        s_digit = input().lower()
    if s_digit == "да":
        chars.extend(digits)
    print("Хорошо, выберите использовать ли нижний регистр?")
    print("Напишите да или нет")
    lowercase = input().lower()
    while lowercase != "да" and lowercase != "нет":
        print("Напишите да или нет")
        lowercase = input().lower()
    if lowercase == "да":
        chars.extend(lowercase_letters)
    print("Отлично! Осталось два вопроса")
    print("Выберите, использовать ли верхний регистр?")
    uppercase = input().lower()
    while uppercase != "да" and uppercase != "нет":
        print("Напишите да или нет")
        uppercase = input().lower()
    if uppercase == "да":
        chars.extend(uppercase_letters)
    print("Вы великолепны! Осталось совсем чуть чуть")
    print('Использовать ли символы "!#$%&*+-=?@^_." ?')
    s_punctuation = input().lower()
    while s_punctuation != "да" and s_punctuation != "нет":
        print("Напишите да или нет")
        s_punctuation = input().lower()
    if s_punctuation == "да":
        chars.extend(punctuation)
    print("Замечательно! И последний вопрос")
    print("Исключать ли неоднозначные символы?")
    s_ambigous = input().lower()
    while s_ambigous != "да" and s_ambigous != "нет":
        print("Напишите да или нет")
        s_ambigous = input().lower()
    if s_ambigous == "да":
        for i in range(len(ambigous)):
            x = chars.index(ambigous[i])
            chars.pop(x)
    if len(chars) == 0:
        return again()
    return pass_choice(pass_len, chars)


# Функция заново, которая запускается если не выбран ни один варинат символов
# Начинает программу заново или выходит из программы
def again():
    global quantity
    print("Вы не выбрали ни один из предложенных вариантов символов")
    print("Хотите продолжить?")
    s = input().lower()
    while s != "да":
        if s != "нет":
            print("Напишите да или нет")
            s = input().lower()
        else:
            print("Возвращайтесь еще")
            return False
    quantity += 1
    return number_password()


# Функция генерации пароля. Возвращает сгенерированный пароль
# Если счетчик количества паролей не равен 0
# Возвращает функцию подсчета количества генерируемых паролей
def pass_choice(pass_len, chars):
    global password
    password = list()
    for _ in range(pass_len):
        password += random.choice(chars)
    print("Ваш пароль сгенерирован:")
    if quantity == 0:
        print(*password, sep="")
        return False
    else:
        print(*password, sep="")
        return number_password()


start()
