from fastapi import FastAPI
from routes.product import router as product_router
from routes.user import router as user_router
# from fastapi_users.authentication import JWTAuthentication
from database import SessionLocal

app = FastAPI()


database = SessionLocal()

app.include_router(product_router, prefix="/api/v1/products")
app.include_router(user_router, prefix="/api/v1/users")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
