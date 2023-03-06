import uuid
from .database import Base
from sqlalchemy import TIMESTAMP, Column,Integer, String, text
from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = 'user_clickers'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    click_count = Column(Integer, unique=True)
    first_click_date = Column(TIMESTAMP(timezone=True),
                              nullable=False, server_default=text("now()"))
