from sqlalchemy import Column, DateTime, ForeignKey, Integer, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))
    reservation_date = Column(DateTime, default=func.now())
