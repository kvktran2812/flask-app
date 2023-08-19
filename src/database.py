import sqlite3
import uuid

con = sqlite3.connect(f"mydatabase.db")
cur = con.cursor()

cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

res = cur.execute("SELECT * FROM movie")
result = res.fetchall()

con.commit()

print(result)
