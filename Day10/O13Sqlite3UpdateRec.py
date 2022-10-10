

import sqlite3

conn = sqlite3.connect("players.sqlite3")

cursor = conn.cursor()

query = "update player set acheivement = '85 Knock Outs' where plyid = 'Pl002'"

cursor.execute(query)

conn.commit()

conn.close()


