
import sqlalchemy  as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from prettytable import PrettyTable

Base = declarative_base()

engine = db.create_engine("sqlite:///players.sqlite3")
connection = engine.connect()
metadata = db.MetaData()

class Player(Base):

    __tablename__ = "Player"

    playerid = db.Column(db.String, primary_key = True)
    plyname = db.Column(db.String)
    sport = db.Column(db.String)
    achvmnt = db.Column(db.String)

Session = sessionmaker(bind=engine)
session = Session()

result = session.query(Player).with_entities(Player.playerid, Player.plyname).filter(Player.playerid == 'PLY003').all()

for rec in result:
    print(rec.playerid, rec.plyname)
