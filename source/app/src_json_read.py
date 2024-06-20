
import typing
import json
from pathlib import Path

class load_json:
    def __init__(self) -> None:
        pass

    def read(self,path: Path) -> None:
        file = open(path)
        data = json.load(file)
        file.close()
        return data

# can add source read count for audit table. 