from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.journal import JournalCreate, Journal
from app.models.journal import Journal as JournalModel
from app.core.security import verify_token
from app.database import get_db

router = APIRouter()

@router.post("/journals", response_model=Journal)
def create_journal(journal: JournalCreate, user_id: int = Depends(verify_token), db: Session = Depends(get_db)):
    db_journal = JournalModel(**journal.dict(), user_id=user_id)
    db.add(db_journal)
    db.commit()
    db.refresh(db_journal)
    return db_journal

@router.get("/journals", response_model=List[Journal])
def read_journals(user_id: int = Depends(verify_token), db: Session = Depends(get_db)):
    return db.query(JournalModel).filter(JournalModel.user_id == user_id).all()
