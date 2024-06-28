from pydantic import BaseModel
from datetime import datetime

class EmotionBase(BaseModel):
    date: datetime
    emotion: str
    intensity: int
    journal_entry: str

class EmotionCreate(EmotionBase):
    pass

class Emotion(EmotionBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
