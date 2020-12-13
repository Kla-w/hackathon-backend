from typing import List, Optional

from fastapi_users import models
from pydantic import BaseModel
from pydantic.schema import datetime


##############################################

#
# class ItemBase(BaseModel):
#     title: str
#     description: Optional[str] = None
#
#
# class ItemCreate(ItemBase):
#     pass
#
#
# class Item(ItemBase):
#     id: int
#     owner_id: int
#
#     class Config:
#         orm_mode = True
#
#
# ##############################################
#
# class UserBase(BaseModel):
#     email: str
#
#
# class UserCreate(UserBase):
#     password: str
#
#
# class User(UserBase):
#     id: int
#     is_active: bool
#     items: List[Item] = []
#
#     class Config:
#         orm_mode = True

#################################################


class User(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass

#################################################


# class PhotoBase(BaseModel):
#     path: str
#
#
# class PhotoCreate(PhotoBase):
#     pass
#
#
# class Photo(PhotoBase):
#     id: int
#     parent_id: int
#
#     class Config:
#         orm_mode = True

#################################################


class DistrictBase(BaseModel):
    name: str
    location: str


class DistrictCreate(DistrictBase):
    pass


class District(DistrictBase):
    id: int

    class Config:
        orm_mode = True


#################################################


class TagBase(BaseModel):
    label: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True


#################################################


class ProductBase(BaseModel):
    name: str
    description: str
    active: bool
    price: float
    tax: float
    # aisles = Aisle
    # photo: List[Photo] = []
    photo: str
    tags: List[Tag]


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


#################################################


class AisleBase(BaseModel):
    title: str
    active: bool
    # products: List[Product] = []
    # photos_id: List[Photo] = []
    photo: str


class AisleCreate(AisleBase):
    pass


class Aisle(AisleBase):
    id: int
    products: Optional[List[Product]] = None

    class Config:
        orm_mode = True


#################################################


class MarketBase(BaseModel):
    name: str
    description: str

    location: List[District] = []
    # shops: List[Shop] = []


class MarketCreate(MarketBase):
    pass


class Market(MarketBase):
    id: int

    class Config:
        orm_mode = True


#################################################


class ShopBase(BaseModel):
    name: str
    description: str
    # photos: Optional[List[Photo]] = []
    shopType: str
    aisles: List[Aisle] = []
    market: Optional[int] = None


class ShopCreate(ShopBase):
    pass


class Shop(ShopBase):
    id: int
    # markets: Optional[List[Market]] = []
    # aisles_id: int
    photo: Optional[str] = None

    class Config:
        orm_mode = True


#################################################


class OrderBase(BaseModel):
    title: str
    order_date: datetime
    order_withdrawal: datetime
    approved: bool

    products: List[Product] = []


class OrderCreate(MarketBase):
    pass


class Order(MarketBase):
    id: int

    class Config:
        orm_mode = True
