from dotenv import load_dotenv
from pathlib import Path
import os


from src_json_read import load_json
from tgt_put_in_target import data_load_in_postgres


def main():
    load_dotenv()
    FILE_PATH = os.getenv('FILE_APTH')

    JSON_FILE_PATH =Path(FILE_PATH+'/stock.json')

    #Reading JSON formated data
    lj = load_json()
    data = lj.read(JSON_FILE_PATH)
    print(data)

    dl= data_load_in_postgres()
    dl.load_json(data)


if __name__=='__main__':
    main()
