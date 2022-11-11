from typing import ClassVar, Generic, TypeAlias, TypeVar

from pydantic import BaseConfig
from pydantic.generics import GenericModel

_OkT = TypeVar("_OkT")


class Ok(GenericModel, Generic[_OkT]):
    data: _OkT
    error: ClassVar[None] = None

    class Config(BaseConfig):
        @staticmethod
        def schema_extra(schema, model):  # pyright: ignore
            schema["properties"]["error"] = {"type": None}


_ErrT = TypeVar("_ErrT")


class Err(GenericModel, Generic[_ErrT]):
    data: ClassVar[None] = None
    error: _ErrT

    class Config(BaseConfig):
        @staticmethod
        def schema_extra(schema, model):  # pyright: ignore
            schema["properties"]["data"] = {"type": None}


Result: TypeAlias = Ok[_OkT] | Err[_ErrT]
