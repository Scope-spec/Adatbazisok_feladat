import sqlite3 as db

source_db = 'Database/industrial.db'
backup_db = 'Database/industrial.db.bak'

conn = db.connect('Database/industrial.db')
backup = db.connect('Database/industrial.db.bak')

conn.close()
backup.close()