from sqlalchemy import Column, String,Float,Integer , BigInteger
from app.database import Base


class Stock(Base):
    __tablename__='nasdaq_stocks'

    symbol = Column(String,primary_key=True)
    company = Column(String)
    description = Column(String)
    intial_price = Column(Float)
    price_2002 = Column(Float)
    price_2007 = Column(Float)
