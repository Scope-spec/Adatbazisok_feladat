import sqlite3

conn = sqlite3.connect('Database/industrial.db')
cursor = conn.cursor()

try:
    cursor.execute("BEGIN TRANSACTION;")

    cursor.execute("""
        INSERT INTO Adagok (ADAGSZAM, ADAGIDO, ADAGIDO, kezdet_datetime, vege_datetime)
        VALUES (999, 0, 123, '2025-11-12 12:00:00', '2025-11-12 13:00:00')
    """)

    cursor.execute("""
        INSERT INTO Hutopanelek (timestamp, Panel hőfok 1 [°C] ValueY, Panel hőfok 2 [°C] ValueY)
        VALUES ('2025-11-12 12:30:00', 42.5, 39.8)
    """)

    conn.commit()
    print("Tranzakció sikeresen végrehajtva.")

except Exception as e:
    conn.rollback()
    print("Hiba történt, tranzakció visszavonva:", e)

finally:
    conn.close()