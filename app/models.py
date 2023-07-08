from sqlalchemy import (Column, Integer, Boolean,
                        VARCHAR, text, TIMESTAMP, Text)

from database import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(VARCHAR(255), nullable=False)
    content = Column(Text, nullable=False)
    published = Column(Boolean, server_default='1', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,
                        server_default=text('CURRENT_TIMESTAMP'))
