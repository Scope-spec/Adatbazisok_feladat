import pandas as pd
import sqlite3 as db

conn = db.connect('Database/industrial.db')
df = pd.read_sql_query("SELECT * FROM Adagok", conn)
cursor = conn.cursor()

"""
df['kezdet_datetime'] = df['Kezdet_DATUM'].str.strip().str.replace('.', '-') + ' ' + df['Kezdet_IDO'].str.strip()
df['vege_datetime']   = df['Vege_DATUM'].str.strip().str.replace('.', '-') + ' ' + df['Vege_IDO'].str.strip()
df.to_sql('Adagok', conn, if_exists='replace', index=False)
"""

"""
cursor.execute('ALTER TABLE Adagok DROP COLUMN Kezdet_DATUM')
cursor.execute('ALTER TABLE Adagok DROP COLUMN Kezdet_IDO')
cursor.execute('ALTER TABLE Adagok DROP COLUMN Vege_DATUM')
cursor.execute('ALTER TABLE Adagok DROP COLUMN Vege_IDO')
"""

"""
df['ADAGIDO'] = pd.to_numeric(df['ADAGIDO'])
df['ADAGSZAM'] = pd.to_numeric(df['ADAGSZAM'])
df['ADAGKOZI IDO'] = pd.to_numeric(df['ADAGKOZI IDO'])
"""

conn.commit()
conn.close()