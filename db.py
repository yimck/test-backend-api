# import sqlite3

# con = sqlite3.connect("sample.db")
# cur = con.cursor()

# cur.execute("CREATE TABLE item(name, ingredients, price)")

# def insert(item):
#     sql_statement = "INSERT INTO item VALUES(?, ?, ?)"
#     cur.execute(sql_statement, item)
#     con.commit()
#     con.close()