from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    sqlalchemy_string:str = "postgresql://rv:rv@postgress_pg-database_1/fastapi"

settings = Settings()