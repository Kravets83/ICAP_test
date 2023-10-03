from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base, engine


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    photo_url = Column(String)
    category = Column(String)
    is_offer = Column(Boolean)
    is_available = Column(Boolean)
    is_pickup = Column(Boolean)
    description = Column(String)
    price = Column(Float)
