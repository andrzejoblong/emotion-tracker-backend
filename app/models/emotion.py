from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Emotion(Base):
    __tablename__ = "emotions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime)
    emotion = Column(String)
    intensity = Column(Integer)
    journal_entry = Column(String, nullable=True)

    user = relationship("User", back_populates="emotions")
