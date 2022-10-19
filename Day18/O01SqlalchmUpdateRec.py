import sqlalchemy
from sqlalchemy import create_engine, text, MetaData, Column, String, update
from sqlalchemy.ext.declarative import  declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///players.sqlite3")
metadata = MetaData(bind=engine)

class Player(Base):

    __tablename__ = "Player"

    playerid = Column(String, primary_key = True)
    plyname = Column(String)
    sport = Column(String)
    achvmnt = Column(String)

connection = engine.connect()

updtQry = update(Player)
updtQry = updtQry.values({'plyname': 'Sachin Ramesh Tendulkar'})
updtQry = updtQry.where(Player.playerid == 'PLY001')
connection.execute(updtQry)


# fetch the updated Data from the database
Player =  sqlalchemy.Table('Player', metadata, autoload=True, autoload_with=engine)
query = sqlalchemy.select([Player])

result = connection.execute(query)
print(Player.columns.keys())

for rec in result.fetchall():
   print(rec)



