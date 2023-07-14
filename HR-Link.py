import pandas as pd
import sqlite3

# URL ссылки на Google Sheets
url = "https://docs.google.com/spreadsheets/d/1MT2L-W7ljYRZ7YfPOMwpPqoPv4T64koH7TVW_u5YMu0/export?format=csv&gid=1417323481"

# Чтение данных из ссылки Google Sheets
df_author = pd.read_csv(url, skiprows=1, usecols=[6, 7, 8, 9, 10], nrows=7)
df_book = pd.read_csv(url, skiprows=9, usecols=[6, 7, 8], nrows=7)
df_edition = pd.read_csv(url, skiprows=17, usecols=[6, 7, 8, 9, 10], nrows=7)

# Преобразование формата данных столбца 'date_birth' в таблице 'df_author'
df_author = df_author.rename(
    columns={
        "full_name": "full_name",
        "date_birth": "date_birth",
        "date_death": "date_death",
        "homeland": "homeland",
    }
)
df_author["date_birth"] = pd.to_datetime(df_author["date_birth"], format="%d.%m.%Y")
df_author["date_death"] = pd.to_datetime(df_author["date_death"], format="%d.%m.%Y")

# Создание базы данных в памяти
conn = sqlite3.connect(":memory:")

# Запись данных в таблицы базы данных
df_author.to_sql("Author", conn, index=False)
df_book.to_sql("Book", conn, index=False)
df_edition.to_sql("Edition", conn, index=False)

# Выполнение SQL-запросов
# 1) Авторы, пережившие некоторое событие (23 октября 2077 года)
authors_event = pd.read_sql_query(
    "SELECT * FROM Author WHERE date_death >= '2077-10-23'", conn
)

# 2) Книги, издававшиеся после смерти автора
books_after_death = pd.read_sql_query(
    """
    SELECT b.*
    FROM Book b
    INNER JOIN Edition e ON b.id = e.book_id
    INNER JOIN Author a ON b.author_id = a.id
    WHERE e.date_published > a.date_death
""",
    conn,
)

# Вывод результатов
print("Авторы, пережившие некоторое событие:")
print(authors_event)

print("Книги, издававшиеся после смерти автора:")
print(books_after_death)
