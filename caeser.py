# Создаем переменную, в которую будет записываться итоговый текст

total = ""


# Создаем функцию для считывания и передачи введеного текста
# Функция также проверяет язык текста
def start(lan):
    s = input("Введите слово:")
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


# Создаем функцию для считывания и передачи количества сдвигов
def shift():
    num = input("Введите количество сдвигов: ")
    while num.isdigit() == False or num == 0:
        print("Количество должно быть ЦЕЛЫМ числом больше 0")
        num = input("Введите количество сдвигов: ")
    num = int(num)
    return num


# Создаем функцию для считывания и передачи направления сдвига
def turn_isvalid():
    turn = input("Введите направление сдвига: ").lower()
    while turn != "право" and turn != "лево":
        print("Направление необходимо указать право или лево")
        turn = input("Введите направление сдвига: ").lower()
    if turn == "лево":
        turn = -1
    else:
        turn = 1
    return turn


# Создаем приветсвенную функцию, которая определяет на каком языке будет введен текст
# И возвращает функцию шифровки текста в зависимости от выбранного языка
def lang():
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
    language = input('Введите "1" или "2" с клавиатуры: ').lower()
    while language != "1" and language != "2":
        print("Необходимо правильно задать язык")
        print(
            'Напишите в ответe "1" - чтобый выбрать русский язык или "2" - чтобы выбрать английский язык'
        )
        language = input('Введите "1" или "2" с клавиатуры: ').lower()
    if language == "1":
        return char_ru()
    else:
        return char_en()


# Создаем функцию для шифровки русского текста
# Функция возвращает итоговый результат
def char_ru():
    global total
    lan = 1
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


# Создаем функцию для шифровки английского текста
# Функция возвращает итоговый результат
def char_en():
    global total
    lan = 2
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
