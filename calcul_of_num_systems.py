lst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]


def system() -> None:
    """Функция приветсвия и выбора системы счисления"""
    print(
        "Эта программа переводит числа из десятичной системы счисления\n",
        "или переводит числа в десятичную систему счисления",
    )
    print("Выберите систему счисления из которой хотите перевести число")
    p = input("Введите число:\n")
    while p.isdigit() == False:
        print("Введено должно быть число от 1 до 16!")
        p = input("Введите число:\n")
    if p != 10:
        print("Введенное число будет переведено в десятичную систему счисления")
        num = is_valid()
        return create_other(num, int(p))
    else:
        print("Выберите систему счисления в которую хотите перевести число")
        s = input("Введите число:\n")
        while s.isdigit() == False:
            print("Введено должно быть число от 1 до 16!")
            s = input("Введите число:\n")
        print(
            "Теперь необходимо ввести целое число, для его перевода в выбранную вами систему счисления"
        )
        num = is_valid()
        return create_decimal(int(num), int(s))


def is_valid() -> int:
    num = [i for i in input("Введите число:\n").upper() if i in lst]
    return num


def create_decimal(num: int, s: int) -> print:
    """Функция перевода числа из десятичной системы"""
    total = ""
    while num != 0:
        x = num % s
        total = lst[x] + total
        num //= s
    print(total)


def create_other(num: int, p: int) -> print:
    """Функция перевода числа в десятичную систему"""
    total = 0
    for i in range(len(num)):
        x = lst.index(num[i]) * p ** (len(num) - i - 1)
        total += x
    print(total)


system()
