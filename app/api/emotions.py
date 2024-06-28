from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.emotion import EmotionCreate, Emotion
from app.models.emotion import Emotion as EmotionModel
from app.core.security import verify_token
from app.database import get_db

router = APIRouter()

@router.post("/emotions", response_model=Emotion)
def create_emotion(emotion: EmotionCreate, user_id: int = Depends(verify_token), db: Session = Depends(get_db)):
    db_emotion = EmotionModel(**emotion.dict(), user_id=user_id)
    db.add(db_emotion)
    db.commit()
    db.refresh(db_emotion)
    return db_emotion

@router.get("/emotions", response_model=List[Emotion])
def read_emotions(user_id: int = Depends(verify_token), db: Session = Depends(get_db)):
    return db.query(EmotionModel).filter(EmotionModel.user_id == user_id).all()
