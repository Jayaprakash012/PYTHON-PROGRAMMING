import mysql.connector as myconn
mydb = myconn.connect(host="localhost", user="system", password="yes")
print("Connected to MySQL database")