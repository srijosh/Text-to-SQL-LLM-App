import sqlite3

# Database setup
connection=sqlite3.connect("student.db")

# Create cursor
cursor=connection.cursor()

# Create the table
create_table_query="""
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME    VARCHAR(25),
    COURSE   VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS   INT
);
"""

cursor.execute(create_table_query)

# Insert Records
sql_query = """INSERT INTO STUDENT (NAME, COURSE, SECTION, MARKS) VALUES (?, ?, ?, ?)"""
values = [
    ('Student1', 'Data Science', 'A', 90),
    ('Student2', 'Machine Learning', 'B', 100),
    ('Student3', 'AI', 'A', 86),
    ('Student4', 'DEVOPS', 'A', 50),
    ('Student5', 'MLOPS', 'A', 35)
]

cursor.executemany(sql_query, values)
connection.commit()
#In SQLite (and other relational databases), .commit() is used to save the changes made to the database during a transaction. It ensures that all executed SQL commands (such as INSERT, UPDATE, and DELETE) are permanently written to the database.

# Display the records
data=cursor.execute("""Select * from STUDENT""")

for row in data:
    print(row)

if connection:
    connection.close()