from sqlalchemy.orm import Session

from . import models, schemas


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()
#
#
# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()
#
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()
#
#
# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()
#
#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

######################################


def get_shops(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Shop).offset(skip).limit(limit).all()


def get_shop(db: Session, shop_id: int):
    return db.query(models.Shop).filter(models.Shop.id == shop_id).first()


def create_shop(db: Session, shop: schemas.ShopCreate):
    db_shop = models.Shop(**shop.dict())
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)
    return db_shop


def delete_shop(db: Session, shop_id: int):
    return db.query(models.Shop).filter(models.Shop.id == shop_id).delete()

######################################


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).delete()

######################################


def get_aisles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Aisle).offset(skip).limit(limit).all()


def get_aisle(db: Session, aisle_id: int):
    return db.query(models.Aisle).filter(models.Aisle.id == aisle_id).first()


def create_aisle(db: Session, aisle: schemas.AisleCreate):
    db_aisle = models.Aisle(**aisle.dict())
    db.add(db_aisle)
    db.commit()
    db.refresh(db_aisle)
    return db_aisle


def delete_aisle(db: Session, aisle_id: int):
    return db.query(models.Aisle).filter(models.Aisle.id == aisle_id).delete()

######################################


def get_markets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Market).offset(skip).limit(limit).all()


def get_market(db: Session, market_id: int):
    return db.query(models.Market).filter(models.Market.id == market_id).first()


def create_market(db: Session, market: schemas.MarketCreate):
    db_market = models.Market(**market.dict())
    db.add(db_market)
    db.commit()
    db.refresh(db_market)
    return db_market


def delete_market(db: Session, market_id: int):
    return db.query(models.Market).filter(models.Market.id == market_id).delete()

######################################


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()


def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).delete()

######################################


def get_districts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.District).offset(skip).limit(limit).all()


def get_district(db: Session, district_id: int):
    return db.query(models.District).filter(models.District.id == district_id).first()


def create_district(db: Session, district: schemas.DistrictCreate):
    db_district = models.District(**district.dict())
    db.add(db_district)
    db.commit()
    db.refresh(db_district)
    return db_district


def delete_district(db: Session, district_id: int):
    return db.query(models.District).filter(models.District.id == district_id).delete()

######################################


def get_tags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tag).offset(skip).limit(limit).all()


def get_tag(db: Session, tag_id: int):
    return db.query(models.Tag).filter(models.Tag.id == tag_id).first()


def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = models.Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def delete_tag(db: Session, tag_id: int):
    return db.query(models.Tag).filter(models.Tag.id == tag_id).delete()

######################################
