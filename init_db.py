import sqlite3

connection = sqlite3.connect('tracking.db')

with open('init_db.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()