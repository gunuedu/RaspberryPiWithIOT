import sqlite3

db = sqlite3.connect("test.db")
db.row_factory = sqlite3.Row
cur = db.cursor()
query = cur.execute("select * from student")
for row in query.fetchall():
    print(row["id"],row["name"],row["birth"], row["gender"])

cur.close()
db.close()
