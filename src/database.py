import sqlite3

bd = sqlite3.connect('Scores.sqlite')

cur = bd.cursor()
cur.execute("""
        CREATE TABLE Scores(
            name TEXT,
            score INTEGER
        );
    """)
cur.close()