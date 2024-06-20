import requests
from requests.exceptions import HTTPError

from database import sessionLocal, engine
from tgt_put_in_target import data_load_in_postgres

URL='http://fastAPIContainer:80/stock'

def init_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_data_from_url():

    try:
        response = requests.get(URL)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        print("Success!")

    response.encoding = "utf-8"
    return response.json()


def main():
    data = get_data_from_url()
    dl= data_load_in_postgres()
    dl.load_json(data)


if __name__ =="__main__":
    main()


    


