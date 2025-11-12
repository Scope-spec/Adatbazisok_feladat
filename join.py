import sqlite3
import pandas as pd

conn = sqlite3.connect('Database/industrial.db')

query = """
SELECT 
    a.ADAGSZAM,
    a.kezdet_datetime,
    a.vege_datetime,
    AVG(s.panel1) AS atlag_homerseklet
FROM Adagok a
JOIN Hutopanelek s 
    ON s.timestamp BETWEEN a.kezdet_datetime AND a.vege_datetime
GROUP BY a.ADAGSZAM
"""

df = pd.read_sql_query(query, conn)
print(df)
conn.close()