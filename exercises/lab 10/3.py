#Implement updating data in the table (change user first name or phone)

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

#looking with the first and last name
first_old = str(input("First_name: "))
last_old = str(input("Last_name: "))
num_old = int(input("Num_: "))
sql = f"select * from phonebook where first_name =\'{first_old}\' and last_name = \'{last_old}\' and phone_num = \'{num_old}\' "
cursor.execute(sql)
info = cursor.fetchall()

if len(info) > 0:
    new_first = str(input("First_new: "))
    new_last = str(input("Last_new: "))
    new_phone = int(input("Num_new: "))
    sql_update = f"Update phonebook set phone_num =\'{new_phone}\', first_name =\'{new_first}\', last_name =\'{new_last}\' where first_name =\'{first_old}\' and last_name = \'{last_old}\'; " 
    cursor.execute(sql_update)
    print("successfully !!");
else:
    print("this people name is not in phonebook")


conn.commit()

conn.close()