import sqlite3

bd = sqlite3.connect('Scores.sqlite')

cur = bd.cursor()
cur.execute("""
        CREATE TABLE if not exists Scores(
            name TEXT,
            score INTEGER
        );
    """)

cur.execute("""
SELECT name AS Player, score AS Result FROM Scores
ORDER BY score DESC
LIMIT 3 
""")

results = cur.fetchall()
print(results)

cur.close()