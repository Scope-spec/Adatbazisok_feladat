import sqlite3 as db

conn = db.connect('Database/industrial.db')
cursor = conn.cursor()

cursor.execute("CREATE INDEX kezdete_datetime ON Adagok(kezdete_datetime);")
cursor.execute("CREATE INDEX vege_datetime ON Adagok(vege_datetime);")
cursor.execute("CREATE INDEX timestamp ON Hutopanelek(timestamp);")

conn.commit