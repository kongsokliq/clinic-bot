import sqlite3

conn = sqlite3.connect("clinic.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    age TEXT,
    gender TEXT,
    diagnosis TEXT,
    treatment TEXT
)
""")

conn.commit()

conn.close()

print("Database Ready")