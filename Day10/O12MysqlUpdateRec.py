

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="players", port=3306)

cursor = conn.cursor()

query = "update player set acheivement = '85 Knock Outs' where plyid = 'Pl002'"

# delete query
# delete from table_name where condition
# delete from player where plyid = 'ply004'

cursor.execute(query)

conn.commit()

conn.close()


