from sqlalchemy import (Column, Integer, Boolean,
                        VARCHAR, text, TIMESTAMP, Text,
                        String, ForeignKey)
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    joined_on = Column(TIMESTAMP(timezone=True), nullable=False,
                        server_default=text('CURRENT_TIMESTAMP'))

    # posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(VARCHAR(255), nullable=False)
    content = Column(Text, nullable=False)
    published = Column(Boolean, server_default='1', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,
                        server_default=text('CURRENT_TIMESTAMP'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # owner = relationship("User", back_populates="posts")

