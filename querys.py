import pandas as pd
import sqlite3 as db

conn = db.connect('Database/industrial.db')

query = """
SELECT ADAGSZAM, 
       (SELECT AVG(panel1) 
        FROM Hutopanelek s 
        WHERE s.timestamp BETWEEN a.kezdet_datetime AND a.vege_datetime) AS atlag_homerseklet
FROM Adagok a
"""

conn.execute("""CREATE TABLE IF NOT EXISTS Adagok_atlagok (
    ADAGSZAM INTEGER,
    atlag_homerseklet REAL
)
""")
conn.execute("""
INSERT INTO Adagok_atlagok (ADAGSZAM, atlag_homerseklet)
SELECT ADAGSZAM,
       AVG(panel1)
FROM Adagok a
JOIN Hutopanelek s 
  ON s.timestamp BETWEEN a.kezdet_datetime AND a.vege_datetime
GROUP BY ADAGSZAM
""")

query = """
SELECT ADAGSZAM, 'Rendben' AS statusz FROM Adagok_atlagok WHERE atlag_homerseklet < 45
UNION
SELECT ADAGSZAM, 'Túlmelegedés' FROM Adagok_atlagok WHERE atlag_homerseklet >= 45
"""

conn.commit()

df = pd.read_sql_query(query, conn)
print(df)
conn.close()
