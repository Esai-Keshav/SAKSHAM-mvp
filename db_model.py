from sqlalchemy import Column, Integer, String, Boolean, DateTime, VARCHAR, TEXT, UUID
from datetime import datetime
from config import Base, engine


class Chathistory(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(VARCHAR, index=True)
    user_chat = Column(
        TEXT,
        nullable=False,
    )
    chatbot = Column(
        TEXT,
        nullable=False,
    )
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"{self.user_chat}"


Base.metadata.create_all(bind=engine)
