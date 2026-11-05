# ORM - Object-relational mapping
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    customer = Column(String)
    total = Column(Float)


engine = create_engine("sqlite:///baza_nowa.db")
Base.metadata.create_all(engine)
