from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class cctv(Base):
    __tablename__ = 'cctv'

    id = Column(INT, autoincrement=True, primary_key=True)
    image = Column(LONGBLOB)
    road_id = Column(INT)


class MySQLConnector:
    def __init__(self):
        mysql_engine = create_engine('')
        DBSession = sessionmaker(bind=mysql_engine)
        self.session = DBSession()

    def addCCTV(self, image, road_id):
        new_cctv = cctv(image=image, road_id=road_id)
        self.session.add(new_cctv)
        self.session.commit()

    def updateCCTV(self, m_id, image):
        data = {"image": image}
        self.session.query(cctv).filter_by(id=m_id).update(data)
        self.session.commit()

    def closeConnect(self):
        self.session.close()


if __name__ == "__main__":
    obj = MySQLConnector()
    obj.addCCTV("asd".encode(), 1)
