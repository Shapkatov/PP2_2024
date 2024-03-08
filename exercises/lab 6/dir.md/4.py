import os

f = open(r"/Users/Хамид Шапкатов/Desktop/PP2/exercises/lab 6/dir.md/4.txt")
cnt = 0
for lines in f:
    cnt += 1
print(f"file has {cnt} lines")