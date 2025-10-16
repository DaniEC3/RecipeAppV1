import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='')

cursor = conn.cursor()
# cursor.execute("CREATE DATABASE my_database")

cursor.execute("USE my_database")
# In Python, you can contain multi-line text using triple quotes at the start and end
# cursor.execute('''CREATE TABLE inventory(
#     item_id             INT,
#     item_name           VARCHAR(50),
#     price               FLOAT,
#     qty                 INT
# )''')


cursor.execute("DESCRIBE inventory")
result = cursor.fetchall()
# for row in result:
#     print(row)
cursor.execute("SELECT item_id, item_name, price, qty FROM stock")