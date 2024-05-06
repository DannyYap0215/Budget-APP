import sqlite3

con = sqlite3.connect("database.db")

c = con.cursor()

# c.execute("""CREATE TABLE Users(
#             Name text,
#             Age integer,
#             Income integer
#             )""")

c.execute("INSERT INTO Users VALUES ('Danny', 19, 4000)")

c.execute("SELECT * FROM Users WHERE Age = ?", (19,))

con.commit()

con.close()