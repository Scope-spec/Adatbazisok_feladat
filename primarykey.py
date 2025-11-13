import sqlite3 as db

conn = db.connect('Database/industrial.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Adagok_new (
    ADAGSZAM INTEGER PRIMARY KEY,
    ADAGKOZI_IDO INTEGER,
    ADAGIDO INTEGER,
    kezdete_datetime DATETIME,
    vege_datetime DATETIME
);
""")

cursor.execute("""
INSERT INTO Adagok_new (ADAGSZAM, ADAGKOZI_IDO, ADAGIDO, kezdete_datetime, vege_datetime)
SELECT ADAGSZAM, ADAGKOZI_IDO, ADAGIDO, kezdete_datetime, vege_datetime FROM Adagok;
""")

cursor.execute("DROP TABLE Adagok;")
cursor.execute("ALTER TABLE Adagok_new RENAME TO Adagok;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Hutopanelek_new (
    timestamp DATETIME PRIMARY KEY,
    panel1 INTEGER,
    panel2 INTEGER,
    panel3 INTEGER,
    panel4 INTEGER,
    panel5 INTEGER,
    panel6 INTEGER,
    panel8 INTEGER,
    panel9 INTEGER,
    panel10 INTEGER,
    panel11 INTEGER,
    panel12 NTEGER,
    panel13 INTEGER,
    panel14 INTEGER,
    panel15 INTEGER,
);
""")

cursor.execute("""
INSERT INTO Hutopanelek_new (
    timestamp,
    panel1,
    panel2,
    panel3,
    panel4,
    panel5,
    panel6,
    panel8,
    panel9,
    panel10,
    panel11,
    panel12,
    panel13,
    panel14,
    panel15,)
SELECT timestamp,
    panel1,
    panel2,
    panel3,
    panel4,
    panel5,
    panel6,
    panel8,
    panel9,
    panel10,
    panel11,
    panel12,
    panel13,
    panel14,
    panel15 FROM Hutopanelek;
""")

cursor.execute("DROP TABLE Hutopanelek;")
cursor.execute("ALTER TABLE Hutopanelek_new RENAME TO Hutopanelek;")

conn.commit()
conn.close()