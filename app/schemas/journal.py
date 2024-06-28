from pydantic import BaseModel
from datetime import datetime

class JournalBase(BaseModel):
    date: datetime
    content: str

class JournalCreate(JournalBase):
    pass

class Journal(JournalBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
