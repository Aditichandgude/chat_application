from backend.Entities.Base import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR, CHAR, DATETIME, BOOLEAN
from uuid import uuid4
import datetime
from sqlalchemy.orm import relationship

# inside class Otp:
class Otp(Base):
    __tablename__='otp'
    id=Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()))
    user_id=Column(CHAR(36), ForeignKey('user.id'), nullable=False)
    code=Column(VARCHAR(10), nullable=False)
    is_used=Column(BOOLEAN, nullable=False, default=False)
    expires_at=Column(DATETIME, nullable=False)
    created_at=Column(DATETIME, nullable=False, default=datetime.datetime.utcnow)

    user = relationship("user", back_populates="otp")
