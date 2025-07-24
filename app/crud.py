import uuid
from typing import Any

import sqlalchemy
from sqlmodel import Session, select
import sqlalchemy.ext

# from app.core.security import get_password_hash, verify_password
from app.models import Item, ItemCreate, User, UserCreate


def create_user(*, session: Session, user_create: UserCreate) -> User:
    db_obj = User.model_validate(
        user_create,
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def create_item(*, session: Session, item_in: ItemCreate, owner_id: uuid.UUID) -> Item:
    db_item = Item.model_validate(item_in, update={"owner_id": owner_id})
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

def get_user_by_social_number(*, session: Session, social_number: str) -> User | None:
    statement = select(User).where(User.social_number == social_number)
    session_user = session.exec(statement).first()
    return session_user
