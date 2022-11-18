from functools import lru_cache
from typing import Any, Literal, TypeVar, Union

from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, create_model
from pydantic.typing import get_args

from fastapi_rust_result.core.auth import (
    InvalidCredentials,
    SomethingElse,
    User,
    get_current_user,
)
from fastapi_rust_result.core.error import Error


@lru_cache
def _create_model_for_error(type: type[BaseModel]) -> type[BaseModel]:
    return create_model(
        f"{type.__name__}Error",
        data=(type, ...),
        code=(Literal[type.__name__], ...),  # pyright: ignore
    )


T = TypeVar("T", bound=BaseModel)


def error_schema(err_type: type[T]) -> dict[str | int, dict[str, Any]]:
    models = tuple(_create_model_for_error(type) for type in get_args(err_type))
    return {400: {"model": Union[models]}}  # pyright: ignore


async def app_error_handler(_: Request, exc: Error):
    return JSONResponse(
        status_code=400,
        content={"code": type(exc.data).__name__, "data": exc.data.dict()},
    )


app = FastAPI(exception_handlers={Error: app_error_handler})


@app.get(
    "/me",
    response_model=User,
    responses=error_schema(InvalidCredentials | SomethingElse),
)
async def me(user: User = Depends(get_current_user)):
    return user
