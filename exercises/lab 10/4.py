import psycopg2

try:
    # Подключение к базе данных
    conn = psycopg2.connect(
        database="postgres",
        user='postgres',
        password='Daldalushel500@',
        host='localhost',
        #port='5432'
    )
    
    # Создание объекта курсора
    cursor = conn.cursor()
    
    # Установка автоподтверждения для выполнения запросов
    conn.autocommit = True
    
    # SQL-запрос
    sql = "SELECT * FROM phonebook WHERE first_name = 'Sheikh'"
    
    # Выполнение запроса
    cursor.execute(sql)
    
    # Извлечение данных
    info = cursor.fetchall()
    
    # Вывод результатов
    print(info)
    
except (psycopg2.DatabaseError, Exception) as error:
    print("Ошибка:", error)

finally:
    # Закрытие соединения
    if conn is not None:
        conn.close()
