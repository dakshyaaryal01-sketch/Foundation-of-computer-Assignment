import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE Student (
    StudentID INTEGER PRIMARY KEY,
    StudentName TEXT,
    Email TEXT
)
""")

conn.commit()
conn.close()