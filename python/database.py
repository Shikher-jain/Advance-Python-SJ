import mysql.connector
conn = mysql.connector.connect(
    host="localHost",
    user="Username",
    password="password", 
    database="database"
)
print(conn)
cursor = conn.cursor()
print(cursor)
cursor.execute("poiuytrewqlkjhgfdsamnbvcxz")
conn.commit()
conn.close()