import os
import shutil
from enum import Enum
from pathlib import Path
from typing import List

from fastapi import Depends, FastAPI, Request, HTTPException, File, UploadFile
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine, Base, database

SECRET = "SECRET"
models.Base.metadata.create_all(bind=engine)


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass


users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(schemas.UserDB, database, users)


class OpenAPItag(str, Enum):
    SHOP = "Shop (boutique)"
    AISLE = "Aisle (allée)"
    MARKET = "Market (marché)"
    PRODUCT = "Product (produit)"
    ORDER = "Order (commande)"
    DISTRICT = "District (quartier)"
    TAG = "Tag (tag)"


def on_after_register(user: schemas.UserDB, request: Request):
    print(f"User {user.id} has registered.")


def on_after_forgot_password(user: schemas.UserDB, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")


jwt_authentication = JWTAuthentication(
    secret=SECRET, lifetime_seconds=3600, tokenUrl="/auth/jwt/login"
)

app = FastAPI(redoc_url=None)
fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    schemas.User,
    schemas.UserCreate,
    schemas.UserUpdate,
    schemas.UserDB,
)


app.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
)

app.include_router(
    fastapi_users.get_reset_password_router(SECRET, after_forgot_password=on_after_forgot_password),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def save_upload_file(folder: str, upload_file: UploadFile) -> Path:
    try:
        with os.path.join(folder, upload_file.filename).open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()
    return Path(buffer.name)


@app.get("/shop/", response_model=List[schemas.Shop], tags=[OpenAPItag.SHOP])
def read_shops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shops = crud.get_shops(db, skip=skip, limit=limit)
    return shops


@app.put("/shop/{shop_id}", response_model=schemas.Shop, tags=[OpenAPItag.SHOP])
def read_shop(shop_id: int, db: Session = Depends(get_db)):
    pass


@app.get("/shop/{shop_id}", response_model=schemas.Shop, tags=[OpenAPItag.SHOP])
def read_shop(shop_id: int, db: Session = Depends(get_db)):
    db_shop = crud.get_shop(db, shop_id=shop_id)
    if db_shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    return db_shop


@app.post("/shop/", response_model=schemas.Shop, tags=[OpenAPItag.SHOP])
def create_shop(shop: schemas.ShopCreate, upload_file: UploadFile = File(...), db: Session = Depends(get_db)):
    # shop.photo = str(save_upload_file('./shop/', upload_file))
    print(str(save_upload_file('./shop/', upload_file)))
    return crud.create_shop(db=db, shop=shop)


@app.delete("/shop/{shop_id}", response_model=schemas.Shop, tags=[OpenAPItag.SHOP])
def delete_shop(shop_id: int, db: Session = Depends(get_db)):
    db_shop = crud.delete_shop(db, shop_id=shop_id)
    if db_shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    return db_shop


##############################


@app.get("/aisles/", response_model=List[schemas.Aisle], tags=[OpenAPItag.AISLE])
def read_aisles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    aisles = crud.get_aisles(db, skip=skip, limit=limit)
    return aisles


@app.get("/aisle/{aisle_id}", response_model=schemas.Aisle, tags=[OpenAPItag.AISLE])
def read_aisle(aisle_id: int, db: Session = Depends(get_db)):
    db_aisle = crud.get_aisle(db, aisle_id=aisle_id)
    if db_aisle is None:
        raise HTTPException(status_code=404, detail="Aisle not found")
    return db_aisle


@app.post("/aisle/", response_model=schemas.Aisle, tags=[OpenAPItag.AISLE])
def create_aisle_for_shop(aisle: schemas.AisleCreate, db: Session = Depends(get_db)):
    return crud.create_aisle(db=db, aisle=aisle)


@app.delete("/aisle/{aisle_id}", response_model=schemas.Aisle, tags=[OpenAPItag.AISLE])
def delete_aisle(aisle_id: int, db: Session = Depends(get_db)):
    db_aisle = crud.delete_aisle(db, aisle_id=aisle_id)
    if db_aisle is None:
        raise HTTPException(status_code=404, detail="Aisle not found")
    return db_aisle


##############################


@app.get("/products/", response_model=List[schemas.Product], tags=[OpenAPItag.PRODUCT])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.get("/product/{product_id}", response_model=schemas.Product, tags=[OpenAPItag.PRODUCT])
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@app.post("/product/", response_model=schemas.Product, tags=[OpenAPItag.PRODUCT])
def create_product_for_aisle(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@app.delete("/product/{product_id}", response_model=schemas.Product, tags=[OpenAPItag.PRODUCT])
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.delete_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


##############################


@app.get("/markets/", response_model=List[schemas.Market], tags=[OpenAPItag.MARKET])
def read_markets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    markets = crud.get_markets(db, skip=skip, limit=limit)
    return markets


@app.get("/market/{market_id}", response_model=schemas.Market, tags=[OpenAPItag.MARKET])
def read_market(market_id: int, db: Session = Depends(get_db)):
    db_market = crud.get_market(db, market_id=market_id)
    if db_market is None:
        raise HTTPException(status_code=404, detail="Market not found")
    return db_market


@app.post("/market/", response_model=schemas.Market, tags=[OpenAPItag.MARKET])
def create_market_for_shop(market: schemas.MarketCreate, db: Session = Depends(get_db)):
    return crud.create_market(db=db, market=market)


@app.delete("/market/{market_id}", response_model=schemas.Market, tags=[OpenAPItag.MARKET])
def delete_market(market_id: int, db: Session = Depends(get_db)):
    db_market = crud.delete_market(db, market_id=market_id)
    if db_market is None:
        raise HTTPException(status_code=404, detail="Market not found")
    return db_market


##############################


@app.get("/orders/", response_model=List[schemas.Order], tags=[OpenAPItag.ORDER])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders


@app.get("/order/{order_id}", response_model=schemas.Order, tags=[OpenAPItag.ORDER])
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@app.post("/order/", response_model=schemas.Order, tags=[OpenAPItag.ORDER])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)


@app.delete("/order/{order_id}", response_model=schemas.Order, tags=[OpenAPItag.ORDER])
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.delete_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


##############################


@app.get("/districts/", response_model=List[schemas.District], tags=[OpenAPItag.DISTRICT])
def read_districts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    districts = crud.get_districts(db, skip=skip, limit=limit)
    return districts


@app.get("/district/{district_id}", response_model=schemas.District, tags=[OpenAPItag.DISTRICT])
def read_district(district_id: int, db: Session = Depends(get_db)):
    db_district = crud.get_district(db, district_id=district_id)
    if db_district is None:
        raise HTTPException(status_code=404, detail="District not found")
    return db_district


@app.post("/district/", response_model=schemas.District, tags=[OpenAPItag.DISTRICT])
def create_district(district: schemas.DistrictCreate, db: Session = Depends(get_db)):
    return crud.create_district(db=db, district=district)


@app.delete("/district/{district_id}", response_model=schemas.District, tags=[OpenAPItag.DISTRICT])
def delete_district(district_id: int, db: Session = Depends(get_db)):
    db_district = crud.delete_district(db, district_id=district_id)
    if db_district is None:
        raise HTTPException(status_code=404, detail="District not found")
    return db_district


##############################


@app.get("/tags/", response_model=List[schemas.Tag], tags=[OpenAPItag.TAG])
def read_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tags = crud.get_tags(db, skip=skip, limit=limit)
    return tags


@app.get("/tag/{tag_id}", response_model=schemas.Tag, tags=[OpenAPItag.TAG])
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = crud.get_tag(db, tag_id=tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag


@app.post("/tag/", response_model=schemas.Tag, tags=[OpenAPItag.TAG])
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    return crud.create_tag(db=db, tag=tag)


@app.delete("/tag/{tag_id}", response_model=schemas.Tag, tags=[OpenAPItag.TAG])
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = crud.delete_tag(db, tag_id=tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag


##############################


