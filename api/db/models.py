from email.policy import default
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .db import Base

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False, unique=True)
    type = Column(String, index=True, nullable=False)
    cost = Column(Float, index=True, nullable=False)
    isavailable = Column(Boolean, index=True, default=True)
