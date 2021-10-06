import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()

    
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        name TEXT NOT NULL,
        sex INTEGER NOT NULL,
        old INTEGER DEFAULT 1,
        score INTEGER DEFAULT 1
    )""")
    
    cur.execute("INSERT INTO users(name,sex, old, score) VALUES('Aksi', 'Women', 25, 100)")
    con.commit()
    #cur.execute("DROP TABLE users")