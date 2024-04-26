#Querying data from the tables (with different filters)
import psycopg2

conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='Daldalushel500@',
	host='localhost',
	#port='5432'
)
cursor = conn.cursor()
conn.autocommit = True

#select all
#sql = f"select * from phonebook";

#select filter 
sql = f"select * from phonebook where first_name = \'timon\' ";


#select with sort filter decrease by first
#sql = f"select * from phonebook by order by first_name desc";


#select with sort filter increase by first
#sql = f"select * from phonebook by order by first_name asc";


cursor.execute(sql)
info = cursor.fetchall()
print(info)
