from pydantic import BaseModel
from typing import Optional

class StockBase(BaseModel):
    company: str
    description: str
    intial_price: str
    price_2002: str
    price_2007: str
    symbol: str

class StockCreate(StockBase):
    pass 

class Stock(StockBase):

    class config:
        orm_mode=True 
        
