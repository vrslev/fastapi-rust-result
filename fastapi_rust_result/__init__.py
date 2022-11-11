from fastapi import Depends, FastAPI
from pydantic import BaseModel

from fastapi_rust_result.result import Err, Ok, Result

app = FastAPI()


class User(BaseModel):
    username: str


class InvalidCredentials(BaseModel):
    username: str


GetCurrentUserResult = Result[User, InvalidCredentials]


def get_current_user(
    return_ok: bool,
) -> GetCurrentUserResult:
    if return_ok:
        return Ok(data=User(username="lev"))
    else:
        return Err(error=InvalidCredentials(username="ivan"))


@app.get("/me", response_model=GetCurrentUserResult)
async def me(user: GetCurrentUserResult = Depends(get_current_user)):
    return user
