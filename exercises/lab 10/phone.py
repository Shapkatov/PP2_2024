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

# Запрос для получения данных из таблицы PhoneBook
sql = '''SELECT * FROM PhoneBook;'''

# Выполнение запроса
cursor.execute(sql)

# Получение результатов
phonebook_data = cursor.fetchall()

# Вывод данных
print("Содержимое таблицы PhoneBook:")
for row in phonebook_data:
    print(row)

# Закрытие соединения
conn.close()