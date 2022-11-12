from pydantic import BaseModel


class Error(Exception):
    def __init__(self, data: BaseModel) -> None:
        self.data = data
        super().__init__()
