import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, Table
from sqlalchemy.orm import relationship

from .database import Base

association_products_orders = Table('association_products_orders', Base.metadata,
                                    Column('products_id', Integer, ForeignKey('products.id')),
                                    Column('orders_id', Integer, ForeignKey('orders.id'))
                                    )

association_products_tags = Table('association_products_tags', Base.metadata,
                                  Column('products_id', Integer, ForeignKey('products.id')),
                                  Column('tags_id', Integer, ForeignKey('tags.id'))
                                  )

# association_photos_products = Table('association_photos_products', Base.metadata,
#                                     Column('photos_id', Integer, ForeignKey('photos.id')),
#                                     Column('products_id', Integer, ForeignKey('products.id'))
#                                     )
#
# association_photos_aisles = Table('association_photos_aisles', Base.metadata,
#                                   Column('photos_id', Integer, ForeignKey('photos.id')),
#                                   Column('aisles_id', Integer, ForeignKey('aisles.id'))
#                                   )
#
# association_photos_shops = Table('association_photos_shop', Base.metadata,
#                                  Column('photos_id', Integer, ForeignKey('photos.id')),
#                                  Column('shops_id', Integer, ForeignKey('shops.id'))
#                                  )


class Shop(Base):
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    shopType = Column(String, index=True)

    photo = Column(String, index=True, nullable=True)
    # photos_id = Column(Integer, ForeignKey("photos.id"))
    # photos = relationship("Photo", back_populates="shop")

    # type_id = Column(Integer, ForeignKey("types.id"))
    # shopType = relationship("Type", back_populates="items")

    aisles = relationship("Aisle", back_populates="shops")

    # market = Column(ForeignKey('markets.id'), nullable=True)
    market = Column(Integer, ForeignKey('markets.id'), nullable=True)


class Aisle(Base):
    __tablename__ = "aisles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    active = Column(Boolean, default=True)

    shops_id = Column(Integer, ForeignKey('shops.id'))
    shops = relationship("Shop", back_populates="aisles")

    # products_id = Column(Integer, ForeignKey("products.id"))

    products = relationship("Product", back_populates="aisles")
    # products = relationship("Product", back_populates="aisles")

    # photos_id = Column(Integer, ForeignKey("photos.id"))
    # photos = relationship("Photo", back_populates="aisle")
    photo = Column(String, index=True, nullable=True)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    active = Column(Boolean, default=True)
    price = Column(Float, index=True)
    tax = Column(Float, index=True)

    # photo_id = Column(Integer, ForeignKey("photos.id"))
    # photos = relationship("Photo", back_populates="product")
    photo = Column(String, index=True, nullable=True)

    # aisles_id = Column(Integer, ForeignKey("aisles.id"))
    # aisles = relationship("Aisle", back_populates="products")

    aisles_id = Column(Integer, ForeignKey('aisles.id'))
    aisles = relationship("Aisle", back_populates="products")

    tags = relationship("Tag", secondary=association_products_tags, back_populates="parents")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, index=True)
    parents = relationship("Product", secondary=association_products_tags, back_populates="tags")


class Market(Base):
    __tablename__ = "markets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

    # location = Column(String, index=True)

    location_id = Column(Integer, ForeignKey('districts.id'))
    location = relationship("District")

    # shops_id = Column(Integer, ForeignKey("shops.id"))
    # shops = relationship("Market", backref="market")
    shops = relationship("Shop")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, index=True)
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    order_withdrawal = Column(DateTime, default=datetime.datetime.utcnow)
    approved = Column(Boolean, default=False)

    products = relationship("Product", secondary=association_products_orders)


# class Type(Base):
#     __tablename__ = "types"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#
#     owner_id = Column(Integer, ForeignKey("users.id"))
#
#     owner = relationship("User", back_populates="items")


# class Photo(Base):
#     __tablename__ = "photos"
#
#     id = Column(Integer, primary_key=True, index=True)
#     path = Column(String, index=True)
#
#     aisle = relationship("Aisle", secondary=association_photos_aisles, back_populates="photos")
#     shop = relationship("Shop", secondary=association_photos_shops, back_populates="photos")
#     product = relationship("Product", secondary=association_photos_products, back_populates="photos")


class District(Base):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, index=True)
