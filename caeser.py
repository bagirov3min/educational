def start(lan: int) -> None | str:
    """Функция для считывания и передачи введеного текста"""
    s = input("Введите слово:\n")
    if lan == 1:
        for i in range(len(s)):
            if s[i] not in [chr(i) for i in range(ord("А"), ord("я") + 1)]:
                print("Необходимо ввести текст на русском языке!")
                return start(1)
    else:
        for i in range(len(s)):
            if s[i] not in [chr(i) for i in range(ord("A"), ord("Z") + 1)] and s[
                i
            ] not in [chr(i) for i in range(ord("a"), ord("z") + 1)]:
                print("Необходимо ввести текст на английском языке!")
                return start(2)
    return s


def shift() -> int:
    """Функция для считывания и передачи количества сдвигов"""
    num = input("Введите количество сдвигов:\n")
    while num.isdigit() == False or num == 0:
        print("Количество должно быть ЦЕЛЫМ числом больше 0")
        num = input("Введите количество сдвигов:\n")
    return int(num)


def turn_isvalid() -> int:
    """Функция для считывания и передачи направления сдвига"""
    turn = input('Введите направление сдвига цифрой "1" - право, "2"- лево:\n').lower()
    while turn != "1" and turn != "2":
        print('Направление необходимо указать цифрой "1" - право или "2" - лево')
        turn = input("Введите направление сдвига:\n").lower()
    if turn == "2":
        return -1
    return 1


def lang() -> None:
    """Создаем функцию определения языка"""
    print(
        "Добро пожаловать в программу шифровщик текста!",
        "Данная программа шифрует текст по указанным Вами параметрам",
        "Шифрование происходит с использованием шифра Цезаря",
        "Для того, чтобы начать, необходимо выбрать язык шифруемого текста",
        "На данный момент программа обрабатывает английский и русский языки",
        'Напишите в ответe "1" - чтобый выбрать русский язык или "2" - чтобы выбрать английский язык,',
        "для текста, который необходимо зашифровать",
        sep="\n",
    )
    language = input('Введите "1" или "2" с клавиатуры:\n').lower()
    while language != "1" and language != "2":
        print("Необходимо правильно задать язык")
        print(
            'Напишите в ответe "1" - чтобый выбрать русский язык или "2" - чтобы выбрать английский язык'
        )
        language = input('Введите "1" или "2" с клавиатуры:\n').lower()
    if language == "1":
        return char_ru(1)
    return char_en(2)


def char_ru(lan: int) -> print:
    """Функция для шифровки русского текста"""
    total = ""
    num = shift()
    s = start(lan)
    turn = turn_isvalid()
    if turn == 1:
        for i in range(len(s)):
            for j in range(1, num + 1):
                if s[i].isalpha() == False:
                    count = ord(s[i])
                    break
                count = turn * j + ord(s[i])
                if s[i].isupper():
                    if count > ord("Я"):
                        count = ord("А") + (num - j)
                        break
                else:
                    if count > ord("я"):
                        count = ord("а") + (num - j)
                        break
            total += chr(count)
    else:
        for i in range(len(s)):
            for j in range(1, num + 1):
                if s[i].isalpha() == False:
                    count = ord(s[i])
                    break
                count = turn * j + ord(s[i])
                if s[i].isupper():
                    if count < ord("А"):
                        count = ord("Я") - (num - j)
                        break
                else:
                    if count < ord("а"):
                        count = ord("я") - (num - j)
                        break
            total += chr(count)
    print(total)


def char_en(lan: int) -> print:
    """Функция для шифровки английского текста"""
    total = ""
    num = shift()
    s = start(lan)
    turn = turn_isvalid()
    if turn == 1:
        for i in range(len(s)):
            for j in range(1, num + 1):
                if s[i].isalpha() == False:
                    count = ord(s[i])
                    break
                count = turn * j + ord(s[i])
                if s[i].isupper():
                    if count > ord("Z"):
                        count = ord("A") + (num - j)
                        break
                else:
                    if count > ord("z"):
                        count = ord("a") + (num - j)
                        break
            total += chr(count)
    else:
        for i in range(len(s)):
            for j in range(1, num + 1):
                if s[i].isalpha() == False:
                    count = ord(s[i])
                    break
                count = turn * j + ord(s[i])
                if s[i].isupper():
                    if count < ord("A"):
                        count = ord("Z") - (num - j)
                        break
                else:
                    if count < ord("a"):
                        count = ord("z") - (num - j)
                        break
            total += chr(count)
    print(total)


lang()
