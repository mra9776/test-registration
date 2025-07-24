import uuid

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel


# Shared properties
class UserBase(SQLModel):
    # email: EmailStr = Field(unique=True, index=True, max_length=255)
    # is_active: bool = True
    # is_superuser: bool = False
    social_number: str = Field(max_length=10, unique=True)
    full_name: str | None = Field(default=None, max_length=255)
    mobile: str | None = Field(default=None, max_length=255)


# Properties to receive via API on creation
class UserCreate(UserBase):
    pass
    # password: str = Field(min_length=8, max_length=40)

class UserCreateResponse(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class UserRegister(SQLModel):
    # email: EmailStr = Field(max_length=255)
    # password: str = Field(min_length=8, max_length=40)
    social_number: str = Field(max_length=10, unique=True)
    full_name: str | None = Field(default=None, max_length=255)
    mobile: str | None = Field(default=None, max_length=255)


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    items: list["Item"] = Relationship(back_populates="owner", cascade_delete=True)

# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: uuid.UUID

# Shared properties
class ItemBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)


# Database model, database table inferred from class name
class Item(ItemBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    owner_id: uuid.UUID = Field(
        foreign_key="user.id", nullable=False, ondelete="CASCADE"
    )
    owner: User | None = Relationship(back_populates="items")


# Properties to receive on item creation
class ItemCreate(ItemBase):
    pass
