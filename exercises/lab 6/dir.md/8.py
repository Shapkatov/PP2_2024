import os
p=(r"/Users/Хамид Шапкатов/Desktop/PP2/exercises/lab 6/dir.md//delete.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file does not exist")