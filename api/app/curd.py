from sqlalchemy.orm import Session
from fastapi import FastAPI , HTTPException , Query , Depends
from starlette import status

import app.models as models 
import app.schemas as schemas

def get_stock(db: Session,symbol: str):
    return db.query(models.Stock).filter(models.Stock.symbol==symbol).first()

def get_stock_all(db:Session):
    #return {"stocks",db.query(models.Stock).all()}
    return db.query(models.Stock).all()


def stock_sent(stock:schemas.StockCreate , db:Session):
    new_stock=models.Stock(**stock.model_dump())
    db.add(new_stock)
    db.commit()
    db.refresh()
    return [new_stock]

def delete_stock(id:int,db:Session):
    deleted_stock = db.query(models.Stock).filter(models.Stock.id==id)
    if deleted_stock.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id : {id} requested does not available")
    deleted_stock.delete(synchronize_session=False)
    db.commit()
    return ['done']
