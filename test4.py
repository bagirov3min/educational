# Определение класса для элемента списка
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# Функция вставки элемента в список
def List_Insert(L, key, value):
    # Создание нового узла с заданным значением
    new_node = ListNode(value)

    # Если список пуст, новый узел становится головным элементом
    if L is None:
        return new_node

    # Если вставка происходит перед головным элементом,
    # новый узел становится новым головным элементом
    if key == L.value:
        new_node.next = L
        return new_node

    current = L

    # Поиск ключа для вставки
    while current.next is not None:
        if current.next.value == key:
            # Вставка нового узла после найденного ключа
            new_node.next = current.next
            current.next = new_node
            return L
        current = current.next

    # Если ключ не найден, вставляем новый узел в конец списка
    current.next = new_node

    return L

# Функция для печати списка
def print_list(L):
    if L is None:
        print("Список пуст")
    else:
        current = L
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print()

# Создание пустого списка
L = None

# Ввод количества элементов списка
while True:
    try:
        n = int(input("Введите количество элементов списка: "))
        if n >= 0:
            break
        else:
            print("Количество элементов должно быть неотрицательным числом")
    except ValueError:
        print("Некорректный ввод. Введите целое неотрицательное число")

print("Введите элементы списка:")
for i in range(n):
    value = input()
    # Если значение элемента не пусто
    if value != "":
        if L is None:
            # Если список пуст, создаем новый узел и делаем его головным элементом
            L = ListNode(value)
        else:
            current = L
            while current.next is not None:
                current = current.next
            # Добавляем новый узел в конец списка
            current.next = ListNode(value)

# Ввод значения вставляемого элемента
value = input("Введите значение для вставки: ")

# Если значение вставляемого элемента не пусто
if value != "":
    # Ввод ключа для вставки
    key = input("Введите ключ для вставки: ")

    # Вставка элемента в список
    L = List_Insert(L, key, value)

# Вывод списка
print("Список с вставленным элементом:")
print_list(L)