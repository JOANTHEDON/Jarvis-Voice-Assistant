import sqlite3

connection = sqlite3.connect('Admin.db')
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Admin(ID INTEGER PRIMARY KEY,User TEXT,Password TEXT)")
connection.commit()
connection.close()
