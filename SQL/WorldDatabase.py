import mysql.connector

all_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=
)

print(all_db)

# Check if Database Exisits
input_cursor = all_db.cursor()
input_cursor.execute("SHOW DATABASES")

for db in input_cursor:
    print(db)

# World Database
world_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=
    database="world"
)





