from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    photo_url: str
    category: str
    is_monthly_offer: bool
    is_available: bool
    is_pickup_available: bool
    description: str
    price: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    created_at: int
    updated_at: int

    class Config:
        from_attributes = True
