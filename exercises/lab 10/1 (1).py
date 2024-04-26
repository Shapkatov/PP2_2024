# Design tables for PhoneBook.

import psycopg2

# connection establishment
conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='Daldalushel500@',
	host='localhost',
	#port= '5432'
)

conn.autocommit = True
# Creating a cursor object
cursor = conn.cursor()

# ------------1 ----------query to create a database
#sql = ''' CREATE database Phone ''';

# ----------2 --------create user
#sql = ''' CREATE ROLE phone_user WITH PASSWORD 'Esko28:)' LOGIN''';

# ----------3 -------create table

sql = '''CREATE TABLE PhoneBook(
   first_name VARCHAR(255) NOT NULL,
   last_name VARCHAR(255),
   phone_num INT
)''';

# executing above query
cursor.execute(sql)
print("Database has been created successfully !!");

# Closing the connection
conn.close()