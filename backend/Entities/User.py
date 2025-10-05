from backend.Entities.Base import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, CHAR, DATE, ENUM, DATETIME
from uuid import uuid4
import datetime

class User(Base):
    __tablename__='user'
    id=Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()))
    username=Column(VARCHAR(256), nullable=False, unique=True)
    name=Column(VARCHAR(256), nullable=False)
    email=Column(VARCHAR(256), nullable=False, unique=True)
    password=Column(VARCHAR(256), nullable=False)
    profile_picture=Column(VARCHAR(256), nullable=True)
    date_of_birth=Column(DATE, nullable=False)
    gender=Column(ENUM('male', 'female', 'other'), nullable=False)
    created_at=Column(DATETIME, nullable=False, default=datetime.datetime.utcnow)
    updated_at=Column(DATETIME, nullable=True)
