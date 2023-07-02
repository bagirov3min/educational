import math

# Функция для распределения сумм по детализации
def distribute_amounts(details):
    total_quantity = sum(detail['quantity'] for detail in details)  # Вычисляем общее количество
    total_amount = round(sum(detail['quantity'] * detail['price'] for detail in details), 2)  # Вычисляем общую сумму

    for detail in details:
        detail['rounded_quantity'] = round(detail['quantity'], 8)  # Округляем количество до 10 знаков
        detail['rounded_price'] = round(detail['rounded_quantity'] * detail['price'], 2)  # Вычисляем округленную сумму
        cents = round(detail['rounded_price'] - math.floor(detail['rounded_price']), 2)  # Вычисляем копейки
        detail['cents_distribution'] = cents  # Сохраняем распределение копеек
        detail['amount'] = round(detail['rounded_price'] + detail['cents_distribution'], 8)  # Вычисляем окончательную сумму

    return details

# Функция для вывода результатов
def print_details(details):
    for detail in details:
        print(f"{detail['name']}: Количество(кг) = {detail['quantity']:.8f}, Округленное Количество*Цена = {detail['rounded_price']:.7f}, Распределение копеек = {detail['cents_distribution']:.2f}, Сумма = {detail['amount']:.8f}")

# Ввод значений товарной позиции
quantity = 58.21942216
price = 10

# Создание детализации
details = [
    {'name': 'Иванов', 'quantity': 30.88848888, 'price': price, 'rounded_quantity': 0, 'rounded_price': 0, 'cents_distribution': 0.0, 'amount': 0.0},
    {'name': 'Петров', 'quantity': 5.88848888, 'price': price, 'rounded_quantity': 0, 'rounded_price': 0, 'cents_distribution': 0.0, 'amount': 0.0},
    {'name': 'Сидоров', 'quantity': 5.88848888, 'price': price, 'rounded_quantity': 0, 'rounded_price': 0, 'cents_distribution': 0.0, 'amount': 0.0},
    {'name': 'Малевин', 'quantity': 5.88848888, 'price': price, 'rounded_quantity': 0, 'rounded_price': 0, 'cents_distribution': 0.0, 'amount': 0.0},
    {'name': 'Макаров', 'quantity': 5.88848888, 'price': price, 'rounded_quantity': 0, 'rounded_price': 0, 'cents_distribution': 0.0, 'amount': 0.0},
    {'name': 'Сетченко', 'quantity': 1.88848888, 'price': price, 'rounded_quantity': 0, 'rounded_price': 0, 'cents_distribution': 0.0, 'amount': 0.0},
    {'name': 'Козлов', 'quantity': 1.88848888, 'price': price, 'rounded_quantity': 0, 'rounded_price': 0, 'cents_distribution': 0.0, 'amount': 0.0}
]

# Вычисление распределения сумм
details = distribute_amounts(details)

# Вывод результатов
print_details(details)