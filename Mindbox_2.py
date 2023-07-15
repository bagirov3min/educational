import pyodbc

# Подключение к базе данных
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=название_сервера;"
    "Database=название_базы;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# SQL-запрос для выборки всех пар "Имя продукта - Имя категории"
sql_query = """
SELECT P.ProductName, C.CategoryName
FROM Products P
LEFT JOIN ProductCategory PC ON P.ProductID = PC.ProductID
LEFT JOIN Categories C ON C.CategoryID = PC.CategoryID;
"""

# Выполнение SQL-запроса
cursor.execute(sql_query)

# Получение результатов выборки
results = cursor.fetchall()

# Вывод пар "Имя продукта - Имя категории"
for row in results:
    product_name, category_name = row
    print(f"Имя продукта: {product_name}, Имя категории: {category_name}")

cursor.close()
conn.close()
