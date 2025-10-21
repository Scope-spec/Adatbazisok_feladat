import pandas as pd
import sqlite3 as db

df1 = pd.read_csv('Data_Files/Adagok.csv', sep=';')
df2 = pd.read_csv('Data_Files/Hutopanelek.csv', sep=';')

conn = db.connect('Database/industrial.db')
df1.to_sql('Adagok', conn, if_exists='replace', index=False)
df2.to_sql('Hutopanelek', conn, if_exists='replace', index=False)

conn.commit()
conn.close()