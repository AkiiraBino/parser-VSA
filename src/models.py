import os
import typing as t

from pydantic import BaseModel, computed_field, model_validator


class Set(BaseModel):
    dir: str
    number: int

    _folder_name: str = ""

    @computed_field()
    @property
    def path(self) -> str:
        return os.path.join(os.getcwd(), self.dir)

    @property
    def folder_name(self):
        return self._folder_name


class Dataset(BaseModel):
    root: str
    train: Set | None = None
    val: Set | None = None
    test: Set | None = None

    images: str
    labels: str

    @model_validator(mode="after")
    def set_path(self) -> t.Self:
        for item, _type in self.__dict__.items():
            if isinstance(_type, Set):
                self.__dict__[item]._folder_name = self.__dict__[item].dir
                self.__dict__[item].dir = os.path.join(
                    self.root, self.__dict__[item].dir
                )
        return self

    @model_validator(mode="after")
    def check_sets(self) -> t.Self:
        if not any(
            True for _type in self.__dict__.values() if isinstance(_type, Set)
        ):
            raise ValueError("At least one set must be selected")
        return self

    @computed_field()
    @property
    def sets(self) -> list[Set]:
        return [
            self.__dict__[key]
            for key in self.__dict__
            if isinstance(self.__dict__[key], Set)
        ]
