import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()


cur.execute('''
CREATE TABLE phones
(ContactName varchar(255), phone varchar(128) UNIQUE)
''')

# cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()


conn.close()