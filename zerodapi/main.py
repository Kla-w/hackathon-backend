from enum import Enum
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
#
#
# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
#
#
# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
#
# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)
#
#
# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items


@app.get("/shop/", response_model=List[schemas.Shop])
def read_shops(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shops = crud.get_shops(db, skip=skip, limit=limit)
    return shops


@app.get("/shop/{shop_id}", response_model=schemas.Shop)
def read_shop(shop_id: int, db: Session = Depends(get_db)):
    db_shop = crud.get_shop(db, shop_id=shop_id)
    if db_shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    return db_shop


@app.post("/shop/", response_model=schemas.Shop)
def create_shop(shop: schemas.ShopCreate, db: Session = Depends(get_db)):
    return crud.create_shop(db=db, shop=shop)


@app.delete("/shop/{shop_id}", response_model=schemas.Shop)
def delete_shop(shop_id: int, db: Session = Depends(get_db)):
    db_shop = crud.delete_shop(db, shop_id=shop_id)
    if db_shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    return db_shop


##############################


@app.get("/aisles/", response_model=List[schemas.Aisle])
def read_aisles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    aisles = crud.get_aisles(db, skip=skip, limit=limit)
    return aisles


@app.get("/aisle/{aisle_id}", response_model=schemas.Aisle)
def read_aisle(aisle_id: int, db: Session = Depends(get_db)):
    db_aisle = crud.get_aisle(db, aisle_id=aisle_id)
    if db_aisle is None:
        raise HTTPException(status_code=404, detail="Aisle not found")
    return db_aisle


@app.post("/aisle/", response_model=schemas.Aisle)
def create_aisle_for_shop(aisle: schemas.AisleCreate, db: Session = Depends(get_db)):
    return crud.create_aisle(db=db, aisle=aisle)


@app.delete("/aisle/{aisle_id}", response_model=schemas.Aisle)
def delete_aisle(aisle_id: int, db: Session = Depends(get_db)):
    db_aisle = crud.delete_aisle(db, aisle_id=aisle_id)
    if db_aisle is None:
        raise HTTPException(status_code=404, detail="Aisle not found")
    return db_aisle


##############################


@app.get("/products/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_aisles(db, skip=skip, limit=limit)
    return products


@app.get("/product/{aisle_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@app.post("/product/", response_model=schemas.Product)
def create_product_for_aisle(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@app.delete("/product/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.delete_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


##############################


@app.get("/markets/", response_model=List[schemas.Market])
def read_markets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    markets = crud.get_markets(db, skip=skip, limit=limit)
    return markets


@app.get("/market/{market_id}", response_model=schemas.Market)
def read_market(market_id: int, db: Session = Depends(get_db)):
    db_market = crud.get_market(db, market_id=market_id)
    if db_market is None:
        raise HTTPException(status_code=404, detail="Market not found")
    return db_market


@app.post("/market/", response_model=schemas.Market)
def create_market_for_shop(market: schemas.MarketCreate, db: Session = Depends(get_db)):
    return crud.create_market(db=db, market=market)


@app.delete("/market/{market_id}", response_model=schemas.Market)
def delete_market(market_id: int, db: Session = Depends(get_db)):
    db_market = crud.delete_market(db, market_id=market_id)
    if db_market is None:
        raise HTTPException(status_code=404, detail="Market not found")
    return db_market


##############################


@app.get("/orders/", response_model=List[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders


@app.get("/order/{order_id}", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@app.post("/order/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)


@app.delete("/order/{order_id}", response_model=schemas.Order)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.delete_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


##############################


@app.get("/districts/", response_model=List[schemas.District])
def read_districts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    districts = crud.get_districts(db, skip=skip, limit=limit)
    return districts


@app.get("/district/{district_id}", response_model=schemas.District)
def read_district(district_id: int, db: Session = Depends(get_db)):
    db_district = crud.get_district(db, district_id=district_id)
    if db_district is None:
        raise HTTPException(status_code=404, detail="District not found")
    return db_district


@app.post("/district/", response_model=schemas.District)
def create_district(district: schemas.DistrictCreate, db: Session = Depends(get_db)):
    return crud.create_district(db=db, district=district)


@app.delete("/district/{district_id}", response_model=schemas.District)
def delete_district(district_id: int, db: Session = Depends(get_db)):
    db_district = crud.delete_district(db, district_id=district_id)
    if db_district is None:
        raise HTTPException(status_code=404, detail="District not found")
    return db_district


##############################


@app.get("/tags/", response_model=List[schemas.Tag])
def read_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tags = crud.get_tags(db, skip=skip, limit=limit)
    return tags


@app.get("/tag/{tag_id}", response_model=schemas.Tag)
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = crud.get_tag(db, tag_id=tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag


@app.post("/tag/", response_model=schemas.Tag)
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    return crud.create_tag(db=db, tag=tag)


@app.delete("/tag/{tag_id}", response_model=schemas.Tag)
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = crud.delete_tag(db, tag_id=tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag


##############################


