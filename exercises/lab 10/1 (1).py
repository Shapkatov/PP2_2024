import psycopg2

# Установка соединения
conn = psycopg2.connect(
    database="postgres",
    user='postgres',
    password='Daldalushel500@',
    host='localhost',
    # port= '5432'
)

conn.autocommit = True
# Создание объекта-курсора
cursor = conn.cursor()

# Создание таблицы PhoneBook
sql = '''CREATE TABLE PhoneBook(
   id SERIAL PRIMARY KEY,
   first_name VARCHAR(255) NOT NULL,
   last_name VARCHAR(255),
   phone_num VARCHAR(15) NOT NULL UNIQUE
)'''

# Выполнение запроса
cursor.execute(sql)
print("Таблица PhoneBook успешно создана!")

# Закрытие соединения
conn.close()