import mysql.connector 
from mysql.connector import Error

connection=mysql.connector.connect(
    host='localhost' ,#'127.0.0.1', 
    user='root',
    password='Sh!kherJ@!n786',
    database="MySQL"
)

cursor=connection.cursor()

cursor.execute( '''CREATE TABLE IF NOT EXISTS users(  id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(255),
               age INT )''' )

cursor.execute("INSERT INTO users (name, age) VALUESN(%s, %s)", ("ABC",10) )

connection.commit()
