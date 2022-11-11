from typing import Any, ClassVar, Generic, TypeAlias, TypeVar

from pydantic import BaseConfig
from pydantic.generics import GenericModel

OkT = TypeVar("OkT")
ErrT = TypeVar("ErrT")


class Ok(GenericModel, Generic[OkT]):
    data: OkT
    error: ClassVar[None] = None

    class Config(BaseConfig):
        @staticmethod
        def schema_extra(
            schema: Any, model: Any
        ) -> None:  # pyright: ignore[reportIncompatibleVariableOverride]
            schema["properties"]["error"] = {"type": None}


class Err(GenericModel, Generic[ErrT]):
    data: ClassVar[None] = None
    error: ErrT

    class Config(BaseConfig):
        @staticmethod
        def schema_extra(
            schema: Any, model: Any
        ) -> None:  # pyright: ignore[reportIncompatibleVariableOverride]
            schema["properties"]["data"] = {"type": None}


Result: TypeAlias = Ok[OkT] | Err[ErrT]

__all__ = ["Result", "Ok", "Err"]
