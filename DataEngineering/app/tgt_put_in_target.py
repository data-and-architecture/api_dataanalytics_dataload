
from sqlalchemy import create_engine, Table, Column, Integer, MetaData, JSON ,Computed,Identity,String,Float
from sqlalchemy.dialects.postgresql import JSONB, insert 
import json

from database import engine



class data_load_in_postgres:
    def __init__(self) -> None:
        pass
    
    def load_json(self,data: json):
        metadata = MetaData() 
        # reflect the database schema to the metadata 
        metadata.reflect(bind=engine) 
        #Create table through table class
        nasdaq_stocks_bronze = Table(
                        'nasdaq_stocks_bronze', metadata, 
                        Column('id', Integer),
                        Column('symbol',String),
                        Column('company',String),
                        Column('description',String),
                        Column('initial_price',Float),
                        Column('price_2002',Float),
                        Column('price_2007',Float) ,
                        extend_existing=True
                    ) 
        
        metadata.create_all(engine) 

        # get the table object 
        table_name = 'nasdaq_stocks_bronze'
        

        # delete statement preparation 
        # Can implement CDC operations using natural keys and update all
        dele = nasdaq_stocks_bronze.delete()
        # Insert statement preparation
        insert_stmt = insert(nasdaq_stocks_bronze)
        # Execution
        conn = engine.connect()
        conn.execute(dele)
        conn.execute(insert_stmt,data)
        conn.commit() 
        
        # Can implement audit logics