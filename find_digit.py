import random

digit_lower = ["Слишком мало, попробуй еще раз", "Чуть-чуть побольше ;)"]
digit_upper = ["Слишком много, попробуй еще раз", "Чуть-чуть поменьше ;)"]
digit_notfar = ["Ты уже очень близок :)"]
digit_done = ["Ты угадал, поздравляю!"]
trying = ["Попробуй еще раз:"]
count_ = ["Количество оставшихся попыток:"]


def start() -> None:
    """Функция старта игры"""
    s = input("Ты готов начать игру?\n" "Напиши в ответ да = 1, нет = 2:\n").lower()
    while s != "1":
        if s != "2":
            print("К сожалению я не понял ответ:(")
            s = input(
                'Введи "1", чтобы начать игру или "2", чтобы завершить программу:\n'
            ).lower()
        else:
            print("До скорой встречи!")
            return False
    print(
        "Правила просты - ты задаешь диапозон ЦЕЛЫХ чисел, а я загадываю ЦЕЛОЕ число в этом диапозоне.\n",
        "Тебе дается на это 5 попыток. Твоя задача угадать это число. Удачи!",
    )
    return digit()


def is_valid() -> int:
    """Функция проверки правильности введенного числа"""
    n = input()
    while n.isdigit() == False:
        print()
        n = input("Ввести необходимо ЦЕЛОЕ число!\n", "Попробуй еще раз:\n")
    return int(n)


def digit() -> int:
    """Функция для ввода и сохранения чисел"""
    print("Введи первое число для диапозона:")
    x = is_valid()
    print("Введи второе число для диапозона:")
    y = is_valid()
    while y == x or y < x:
        print(
            "Второе число для диапазона не должно быть меньше или равно первому!\n",
            "Напоминаю, что первое число равно:\n",
            x,
            "\n" "Введи второе число для диапозона:\n",
        )
        y = is_valid()

    return find_digit(x, y)


def find_digit(x: int, y: int) -> None:
    """Функция угадывания числа"""
    print(
        "Итак, я загадал число!\n"
        "А теперь попробуй его отгадать!\n"
        "Введи его сюда:"
    )
    d = is_valid()
    num = random.randrange(x, y)
    count = 4
    while d != num:
        if count == 0:
            print("У тебя не осталось попыток :()")
            return game_again()
        notfar = num_notfar(d, num)
        if d < x or d > y:
            print(
                "Введенное число выходит за рамки заданного диапозона!\n",
                "Напоминаю, число загадано в диапозоне от",
                x,
                "до",
                y,
                "\n",
                trying[0],
            )
            d = is_valid()  
        elif notfar == 1:
            count -= 1
            print(digit_lower[1])
            print(count_[0], count + 1)
            print(trying[0])
            d = is_valid()
        elif notfar == 0:
            count -= 1
            print(digit_notfar[0])
            print(count_[0], count + 1)
            print(trying[0])
            d = is_valid()
        elif notfar == -1:
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
    print("Ты победил, поздравляю!!!", "Количество предпринятых попыток:", 5 - count)
    return game_again()


def num_notfar(d: int, num: int) -> int:
    """Функция проверки удаленности числа"""
    if [i for i in range(2, 6) if d + i == num]:
        return 1
    elif [i for i in range(2, 6) if d - i == num]:
        return -1
    elif d - 1 == num or d + 1 == num:
        return 0


def game_again() -> None:
    """Функция игры заново"""
    print("Хочешь сыграть еще?")
    return start()


start()
