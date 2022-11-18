from pydantic import BaseModel

from fastapi_rust_result.core.error import Error


class User(BaseModel):
    username: str


class InvalidCredentials(BaseModel):
    username: str


class SomethingElse(BaseModel):
    wha: str


def get_current_user(return_ok: bool) -> User:
    if return_ok:
        return User(username="lev")
    else:
        raise Error(InvalidCredentials(username="ivan"))
