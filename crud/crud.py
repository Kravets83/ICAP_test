from sqlalchemy.orm import Session
from models.user import User
from models.product import Product
from schemas.user import UserCreate, UserUpdate
from schemas.product import ProductCreate, ProductUpdate
def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get User by ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Get User by Username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Create Product
def create_product(db: Session, product: ProductCreate, user_id: int):
    db_product = Product(**product.dict(), owner_id=user_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Get Products
def get_products(db: Session, category: str = None):
    products_query = db.query(Product)
    if category:
        if category == "offer_of_the_month":
            products_query = products_query.filter(Product.is_offer_of_the_month == True)
        elif category == "available":
            products_query = products_query.filter(Product.is_available == True)
        elif category == "pickup_available":
            products_query = products_query.filter(Product.is_pickup_available == True)
    return products_query.all()

# Get Product by ID
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

# Update Product
def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

# Delete Product
def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return {"message": "Product deleted"}