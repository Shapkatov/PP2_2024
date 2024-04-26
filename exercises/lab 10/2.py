#upload data from csv file
import psycopg2

conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='Daldalushel500@',
	host='localhost',
	#port= '5432'
)
cursor = conn.cursor()
conn.autocommit = True
# CSV to TABLE
'''
f = open("persons.csv", "r")
cursor.copy_from(f, 'phonebook', sep=',')
f.close()
'''

#insert entering user name, phone from console
first = str(input("First: "))
last = str(input("Last: "))
num = int(input("Num: "))


postgres_insert_query = """ INSERT INTO  phonebook(first_name, last_name, phone_num) VALUES (%s,%s,%s)"""
record_to_insert = (first, last, num)
cursor.execute(postgres_insert_query, record_to_insert)


conn.commit()
print("successfully !!");
conn.close()