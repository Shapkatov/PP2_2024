import psycopg2

def insert_data():
    """Insert data into the table."""
    name = input("Enter name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    data = (name, last_name, phone_number)
    command = """
        INSERT INTO phonebook(first_name, last_name, phone_num) 
        VALUES(%s, %s, %s)
        """
    try:
        # Устанавливаем соединение с базой данных
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="Daldalushel500@")
        # Создаем курсор для выполнения SQL-запросов
        cursor = conn.cursor()
        # Выполняем запрос на вставку данных
        cursor.execute(command, data)
        # Фиксируем изменения
        conn.commit()
        print("Data inserted successfully!")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)
    finally:
        # В любом случае закрываем соединение с базой данных
        cursor.close()
        conn.close()

if __name__ == '__main__':
    insert_data()