import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute("CREATE TABLE students(roll INTEGER, name VARCHAR(30))")

roll = int(input())
name = input()

cursor.execute("INSERT INTO students VALUES(?, ?)", (roll, name))

print("inserted")

conn.close()