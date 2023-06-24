# Импортируем библеотеки
import random


# Создаем словари
digit_lower = ["Слишком мало, попробуй еще раз", "Чуть-чуть побольше ;)"]
digit_upper = ["Слишком много, попробуй еще раз", "Чуть-чуть поменьше ;)"]
digit_notfar = ["Ты уже очень близок :)"]
digit_done = ["Ты угадал, поздравляю!"]
trying = ["Попробуй еще раз:"]
count_ = ["Количество оставшихся попыток:"]


# Создаем функцию для начала игры
# Возвращает функцию проверки ответа
def start():
    print("Ты готов начать игру?")
    print("Напиши в ответ да = д, нет = н")
    return start_isvalid()


# Функция проверяющия запуск игры
# Возвращает функцию для ввода и сохранения числа
def start_isvalid():
    s = input().lower()
    while s != "д":
        if s != "н":
            print("К сожалению я не понял ответ:(")
            print('Введи "д", чтобы начать игру или "н", чтобы завершить программу')
            s = input().lower()
        else:
            return False
    print(
        "Правила просты - ты задаешь диапозон ЦЕЛЫХ чисел, а я загадываю ЦЕЛОЕ число в этом диапозоне."
    )
    print("Тебе дается на это 5 попыток")
    print("Твоя задача угадать это число. Удачи!")
    return digit()


# Функция проверки правильности введенного числа
def is_valid():
    x = input()
    while x.isdigit() == False:
        print("Ввести необходимо ЦЕЛОЕ число!")
        print("Попробуй еще раз:")
        x = input()
    return int(x)


# Функция для ввода и сохранения чисел
# Ссылается на функцию проверки числа
def digit():
    global x
    global y
    global num
    print("Введи первое число для диапозона:")
    x = is_valid()
    print("Введи второе число для диапозона:")
    y = is_valid()
    while y == x or y < x:
        print("Второе число для диапазона не должно быть меньше или равно первому!")
        print("Напоминаю, что первое число равно:", x)
        print("Введи второе число для диапозона:")
        y = is_valid()
    num = random.randrange(x, y)
    return find_digit()


# Функция угадывания числа
# Ссылается на функцию проверки удаленности числа
# Возвращает функцию игры заново
def find_digit():
    global d
    print("Итак, я загадал число!")
    print("А теперь попробуй его отгадать!")
    print("Введи его сюда:")
    d = is_valid()
    count = 4
    count1 = 1
    while d != num:
        count1 += 1
        if count == 0:
            print("У тебя не осталось попыток :()")
            return game_again()
        if d < x or d > y:
            print("Введенное число выходит за рамки заданного диапозона!")
            print("Напоминаю, число загадано в диапозоне от", x, "до", y)
            print(trying[0])
            d = is_valid()
        if num_notfar() == 1:
            count -= 1
            print(digit_lower[1])
            print(count_[0], count + 1)
            print(trying[0])
            d = is_valid()
        elif num_notfar() == 0:
            count -= 1
            print(digit_notfar[0])
            print(count_[0], count + 1)
            print(trying[0])
            d = is_valid()
        elif num_notfar() == -1:
            count -= 1
            print(digit_upper[1])
            print(count_[0], count + 1)
            print(trying[0])
            d = is_valid()
        elif d < num:
            count -= 1
            print(digit_lower[0])
            print(count_[0], count + 1)
            print(trying[0])
            d = is_valid()
        elif d > num:
            count -= 1
            print(digit_upper[0])
            print(count_[0], count + 1)
            print(trying[0])
            d = is_valid()
    print("Ты победил, поздравляю!!!", "Количество попыток:", count1)
    return game_again()


# Функция роверки удаленности числа
# Имеет связь только с функцией угадывания числа
def num_notfar():
    if [i for i in range(2, 6) if d + i == num]:
        return 1
    elif [i for i in range(2, 6) if d - i == num]:
        return -1
    elif d - 1 == num or d + 1 == num:
        return 0


# Функция игры заново
# Возвращает функцию проверяющую запуск игры
def game_again():
    print("Хочешь сыграть еще? Напиши в ответ да = д, нет = н")
    return start_isvalid()


# Запуск игры
if start() == False:
    print("До скорой встречи!")
else:
    digit()
