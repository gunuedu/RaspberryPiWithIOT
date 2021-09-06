from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text

engine = create_engine('sqlite:////home/pi/test.db', echo=True, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)
class Student(Base):
    __tablename__ = 'Student'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    birth = Column(String)
    gender = Column(String)

        def __init__(self, id=1, name=None, birth=None, gender=None):
            self.id = id
            self.name = name
            self.birth = birth
            self.gender = gender

        def __repr__(self):
            return '<%r, %r, %r>' % (self.name,self.birth,self.gender)

def show():
    row = db_session.execute("SELECT * from student").fetchall()
    print(row)

def showall():
    row = db_session.query(Student).all()
    print(row)

def showitem(item):
    row = db_session.execute("SELECT * from student where name like "+"'%"+item+"%'").fetchall()
    print(row)
