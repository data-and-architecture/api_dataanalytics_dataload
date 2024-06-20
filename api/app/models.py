from sqlalchemy import Column, String,Float,Integer , BigInteger
from app.database import Base


class Stock(Base):
    __tablename__='nasdaq_stocks'

    id     = Column(Integer,primary_key=True)
    symbol = Column(String)
    company = Column(String)
    description = Column(String)
    initial_price = Column(Float)
    price_2002 = Column(Float)
    price_2007 = Column(Float)
