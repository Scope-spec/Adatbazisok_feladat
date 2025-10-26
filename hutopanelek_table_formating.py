import pandas as pd
import sqlite3 as db

conn = db.connect('Database/industrial.db')
df = pd.read_sql_query("SELECT * FROM Hutopanelek", conn)
cursor = conn.cursor()



conn.close()