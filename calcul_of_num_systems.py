# Создаем переменные

s = 0
p = 0
num = 0
lst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]


# Создаем функцию приветсвия и выбора системы счисления
# Возвращает одну из функций перевода числа в другую систему счисления
def system():
    global s
    global p
    global num
    print(
        "Эта программа переводит числа из десятичной системы счисления",
        "или переводит числа в десятичную систему счисления",
    )
    print("Выберите систему счисления из которой хотите перевести число")
    p = input()
    while p.isdigit() == False:
        print("Введено должно быть число от 1 до 16!")
        p = input()
    p = int(p)
    if p != 10:
        print("Введенное число будет переведено в десятичную систему счисления")
        print("Введите число")
        num = is_valid()
        return create_other()
    else:
        print("Выберите систему счисления в которую хотите перевести число")
        s = input()
        while s.isdigit() == False:
            print("Введено должно быть число от 1 до 16!")
            s = input()
        s = int(s)
        print("Введите число")
        num = input()
        while num.isdigit() == False:
            print("Необходимо ввести целое число!")
            num = input()
        num = int(num)
        return create_decimal()


def is_valid():
    num = [i for i in input().upper() if i in lst]
    return num


# Функция перевода числа из десятичной системы
# Возвращает результат
def create_decimal():
    global num
    total = ""
    while num != 0:
        x = num % s
        total = lst[x] + total
        num //= s
    print(total)


# Функция перевода числа в десятичную систему
# Возвращает результат
def create_other():
    total = 0
    for i in range(len(num)):
        x = lst.index(num[i]) * p ** (len(num) - i - 1)
        total += x
    print(total)


system()
