import pandas as pd
import sqlite3 as db

conn = db.connect('Database/industrial.db')
df = pd.read_sql_query("SELECT * FROM Hutopanelek", conn)
cursor = conn.cursor()

df['timestamp'] = df['Panel hőfok 1 [°C] Time']

df = df.drop(columns=[col for col in df.columns if col.endswith('Time')])
df.to_sql('Hutopanelek', conn, if_exists='replace', index=False)

valuey_cols = [col for col in df.columns if 'ValueY' in col]
for col in valuey_cols:
    df[col] = df[col].str.replace(",", ".", regex=False)
df[valuey_cols] = df[valuey_cols].apply(pd.to_numeric, errors='coerce')

df.to_sql('Hutopanelek', conn, if_exists='replace', index=False)

print(df)
conn.close()