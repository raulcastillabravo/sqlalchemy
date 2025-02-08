from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Sales(Base):
    __tablename__ = "sales"

    client_id = Column(
        Integer, ForeignKey("client.client_id", ondelete="CASCADE"), primary_key=True
    )
    product_id = Column(
        Integer, ForeignKey("product.product_id", ondelete="CASCADE"), primary_key=True
    )
    sold_date = Column(TIMESTAMP, server_default=func.now())
