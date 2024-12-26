import sqlite3

connection = sqlite3.connect('Information.db')
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS AccountDB(ID INTEGER PRMARY KEY, Batch_No TEXT,Batch_Start_Date TEXT,Batch_Start_Time  TEXT,Batch_End_Date TEXT,Batch_End_Time  TEXT"
            "Started_By TEXT,Stoped_By TEXT)")

connection.commit()
connection.close()
