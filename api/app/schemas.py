from pydantic import BaseModel
from typing import Optional

class StockBase(BaseModel):
    id : int
    company: str
    description: str
    initial_price: float
    price_2002: float
    price_2007: float
    symbol: str

class StockCreate(StockBase):
    pass 

class Stock(StockBase):

    class config:
        orm_mode=True 
        
