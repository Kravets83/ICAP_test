from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
    is_active: bool
    created_at: int
    updated_at: int

    class Config:
        from_attributes = True


class UserInDB(User):
    password: str
