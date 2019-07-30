
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
try:
    cursor.execute(""" CREATE TABLE album 
                (title TEXT, artist TEXT)
                """)
except:
    pass

