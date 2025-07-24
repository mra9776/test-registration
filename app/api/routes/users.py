import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import col, delete, func, select

from app import crud
from app.api.deps import (
    # CurrentUser,
    SessionDep,
    # get_current_active_superuser,
)
from app.core.config import settings
from app.models import (
    User,
    UserCreate,
    UserCreateResponse,
    UserPublic,
    UserRegister,
)

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/signup", response_model=UserCreateResponse)
def register_user(session: SessionDep, user_in: UserRegister) -> Any:
    """
    Create new user without the need to be logged in.
    """
    # user = crud.get_user_by_email(session=session, email=user_in.email)
    if len(user_in.social_number) != 10:
        raise HTTPException(
            status_code=400,
            detail="social number not valid",
        )
    user_create = UserCreate.model_validate(user_in)
    user = crud.get_user_by_social_number(session=session, social_number=user_create.social_number)
    if user:
        raise HTTPException(
            status_code=409,
            detail="social number already used",
        )
    user = crud.create_user(session=session, user_create=user_create)
    return UserCreateResponse.model_validate(user)

