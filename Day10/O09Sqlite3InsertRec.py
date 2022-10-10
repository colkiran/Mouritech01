
import sqlite3

conn = sqlite3.connect("players.sqlite3")

cursor = conn.cursor()

# query = "insert into player values ('Pl002', 'Mike Tyson', 'Boxing', '85 ')"
# query = "insert into player values ('Pl003', 'Lionel Messi', 'Soccer', '3 golden Boot')"
# query = "insert into player values ('Pl001', 'Sachin', 'Cricket', '100 centuries')"
# query = "insert into player values ('Pl004', 'Roger Fedrer', 'Tennis', '30 Grand Slams')"
# query = "insert into player values ('Pl005', 'Lewis Hamilton', 'Formula one', '7 Championships')"


cursor.execute(query)

conn.commit()

conn.close()
