from fastapi_users import FastAPIUsers, models
from fastapi_users.db import SQLAlchemyUserDatabase
from database import Base
from schemas.user import User, UserCreate, UserUpdate, UserInDB


user_db = SQLAlchemyUserDatabase(UserInDB, database=Base)

fastapi_users = FastAPIUsers(
    user_db,
    User,
    UserCreate,
    UserUpdate,
    UserInDB,
)
