import sqlite3

num = "devesh"
classHJ = "7th"
section = "B"
# Connecting to sqlite
conn = sqlite3.connect('geeks2.db')

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

# Creating table
table = """CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255),
SECTION VARCHAR(255));"""
# cursor.execute(table)

# Queries to INSERT records.
# cursor.execute("INSERT INTO STUDENT VALUES (?, ?, ?);", )
# cursor.execute('''INSERT INTO STUDENT VALUES ('Shyam', '8th', 'B')''')
# cursor.execute('''INSERT INTO STUDENT VALUES ('Baburao', '9th', 'C')''')

# Display data inserted
# print("Data Inserted in the table: ")
# data = cursor.execute('''SELECT * FROM STUDENT''')
# for row in data:
#     print(row)

# Commit your changes in the database
conn.commit()

statement = '''SELECT * FROM STUDENT'''

cursor.execute(statement)

# output = cursor.fetchall()
# for row in output:
#     print(row)
# conn.commit()

output = cursor.fetchmany(2)
for row1 in output:
    if row1[0] == "Raju":
        print(row1[0])
conn.commit()

print(type(output))

