import psycopg2 as pgsql

connection=pgsql.connect(host="localhost", dbname="postgres", user="postgres", 
                         password="Daldalushel500@", port=5432)
cur=connection.cursor()

# 1 - task

def createpattern():
    global query
    query="""SELECT * FROM phonebook
    WHERE """
    print(r"Do you want to search by first_name(0)/last_name(1)/break(any num) enter the number:")
    mode=int(input())
    if mode==0:
            query+="last_name"
            print("Enter string")
            substr=input()
            print("""Select option:
            1-last_name is equal to string
            2-last_name starts with the string
            3-last_name ends with the string
            4-last_name contains the string""")
            mode1=int(input())
            if mode1==1:
                query+="='{}'".format(substr)
            elif mode1==2:
                query+=" iLIKE '{}%'".format(substr)
            elif mode1==3:
                query+=" iLIKE '%{}'".format(substr)
            else:
                query+=" iLIKE '%{}%'".format(substr)
    elif mode==1:
            query+="""first_name"""
            print("Enter string")
            substr=input()
            print("""Select option:
            1-first_name is equal to string
            2-first_name starts with the string
            3-first_name ends with the string
            4-first_name contains the string""")
            mode1=int(input())
            if mode1==1:
                query+="='{}'".format(substr)
            elif mode1==2:
                query+=" iLIKE '{}%'".format(substr)
            elif mode1==3:
                query+=" iLIKE '%{}'".format(substr)
            else:
                query+=" iLIKE '%{}%'".format(substr)
    else:
         return "error"
    return query

# 2 - task

def insert(last_name, first_name, phone_num):
    cur.execute("SELECT count(*) FROM phonebook WHERE last_name='{}' AND first_name='{}'".format(last_name, first_name))
    if cur.fetchone()[0]==0:
         cur.execute("""INSERT INTO phonebook VALUES ('{}','{}', {})""".format(last_name, first_name, phone_num))
    else:
         cur.execute("""UPDATE phonebook
         SET number={}
         WHERE last_name='{}' AND first_name='{}'
         """.format(phone_num, last_name, first_name))

# 3 - task
         
def loopinsert():
    banned=[]
    while True:
        print("Want to enter a person's data? yes/no")
        mode=input()
        if mode=="no":
             break
        person=input().split()
        if len(person)>3:
             banned.append(person)
             continue
        
        if not person[2].isdigit():
             banned.append(person)
             continue
        
        insert(*person)
    if len(banned)==0:
         return
    print("This data were not added due to incorrect format:")
    for i in banned:
         print(i)
        
# 4 - task
         
def pagination():
    query=createpattern()
    if query=="error":
        return "error"
    print("Need offset? yes/no:")
    mode=input()
    if mode=="yes":
         print("Enter offset:")
         offset=int(input())
         query+=" OFFSET {}".format(offset)
    print("Need limit? yes/no:")
    mode=input()
    if mode=="yes":
         print("Enter limit:")
         limit=int(input())
         query+=" LIMIT {}".format(limit)
    query +=";"
    return query

# 5 - task

def delete():
    query="""DELETE FROM phonebook
    WHERE """
    cur.execute("SELECT * from phonebook")
    print(cur.fetchall())
    print("Do you wanna delete by last_name(0)/first_name(1)/phone_num(2) enter the number")
    mode=int(input())
    if mode==0:
         print("Enter last_name to delete:")
         last_name=input()
         query+="last_name='{}'".format(last_name)
    elif mode==1:
         print("Enter first_name to delete:")
         first_name=input()
         query+="first_name='{}'".format(first_name)
    else:
         print("Enter phone_num to delete:")
         phone_num=input()
         query+="phone_num={}".format(phone_num)
    cur.execute(query)
         

s1=createpattern()
if s1!="error":
     cur.execute(s1+";")
     print(cur.fetchall())
insert("Berik", "Serik", 123)
loopinsert()
s1=pagination()
if s1!="error":
     cur.execute(s1+";")
     print(cur.fetchall())
delete()

connection.commit()
cur.close()
connection.close()