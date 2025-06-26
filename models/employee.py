from .db import db
from enum import Enum
from sqlalchemy import Column, Integer, String, Enum as SQLEnum

class PositionEnum(str, Enum):
    MANAGER = "Manager"
    NORMAL = "Normal"
    OWNER = "Owner"


class Employee(db.Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)
    email = Column(String(length=100), unique=True, nullable=False)
    position = Column(SQLEnum(PositionEnum), nullable=False)

    def __repr__(self):
        return f'<Employee(id={self.id}, name={self.name}, position={self.formatted_postiton}, email={self.email})>'

    @property
    def formatted_postiton(self):
        return self.position.value
