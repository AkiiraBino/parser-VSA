import os

from pydantic import BaseModel

root_dir = os.getcwd()


class Set(BaseModel):
    dir: str
    path: str
    number: int


class Dataset(BaseModel):
    root: str
    train: Set | None = None
    val: Set | None = None
    test: Set | None = None
