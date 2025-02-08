from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    schedule = Column(DateTime, nullable=False)
    instructor_id = Column(Integer, ForeignKey("instructors.id"))
    max_capacity = Column(Integer, nullable=False)
