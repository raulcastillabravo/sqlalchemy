from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = "product"

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(255), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
