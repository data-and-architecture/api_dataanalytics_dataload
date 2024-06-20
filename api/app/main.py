from fastapi import FastAPI , HTTPException , Query , Depends
from sqlalchemy.orm import Session
from typing import List
from starlette import status

import app.curd as crud
import app.models as models
import app.schemas as schemas
from app.database import sessionLocal, engine

#models.Base.metadata.create_all(bind=engine)

app = FastAPI(    
    title="NASDAQ"
    ,version="0.1"
)


def init_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/stock/{symbol}',response_model=schemas.Stock, status_code=200 )
def get_stock(symbol:str , db: Session = Depends(init_db)) -> models.Stock:
    db_stock = crud.get_stock(db,symbol=symbol)
    if db_stock is None:
        raise HTTPException(
            status_code=400, detail=f"No stock{symbol} found."
        )
    return db_stock

@app.get('/stock', response_model=list[schemas.Stock], status_code=200)
def get_stockall(db: Session = Depends(init_db)) -> list[models.Stock]:
    db_stock_list = crud.get_stock_all(db)
    if db_stock_list is None:
        raise HTTPException(
            status_code=400, detail=f"No stock found."
        )
    return db_stock_list


    


