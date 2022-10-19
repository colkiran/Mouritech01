
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///players.sqlite3", echo = True)
base = declarative_base()

class Player(base):

    __tablename__ = "Player"

    playerid = Column(String, primary_key = True)
    plyname = Column(String)
    sport = Column(String)
    achvmnt = Column(String)

    def __init__(self, playerid, plyname, sport, achvmnt):
        self.playerid = playerid
        self.plyname = plyname
        self.sport = sport
        self.achvmnt = achvmnt

base.metadata.create_all(engine)




base.metadata.create_all(engine)
