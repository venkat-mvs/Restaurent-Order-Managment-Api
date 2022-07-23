from sqlalchemy import Boolean, Column, ForeignKey, Integer, PrimaryKeyConstraint, String, Float, UniqueConstraint

from .db import Base

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False, unique=True)
    type = Column(String, index=True, nullable=False)
    cost = Column(Float, index=True, nullable=False)
    isavailable = Column(Boolean, index=True, default=True)

class Table(Base):
    __tablename__ = "table_slots"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    seats = Column(Integer, index=True, nullable=False)
    isoccupied = Column(Boolean, index=True, nullable=False)

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    phone_number = Column(String, unique=True, index=True, nullable=False)

    __table_args__ = (UniqueConstraint('phone_number', name='phone_number_unique'),)


class Orders(Base):
    __tablename__ = "orders"

    table_id = Column(Integer, ForeignKey('table_slots.id'), index=True)
    item_id = Column(Integer, ForeignKey('item.id'), index=True)
    # customer_id = Column(Integer, ForeignKey('customer.id'), index=True)
    quantity_ordered = Column(Integer, nullable=False)

    __table_args__ = (PrimaryKeyConstraint('table_id', 'item_id', name='order_unique'), )

