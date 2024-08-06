from sqlalchemy.orm import Session
from typing import Optional
import models
import schemas

def create_calendar(db: Session, calendar: schemas.CalendarCreate) -> models.Calendar:
    db_calendar = models.Calendar(name=calendar.name)
    db.add(db_calendar)
    db.commit()
    db.refresh(db_calendar)
    return db_calendar

def read_calendar(db: Session, calendar_id: int) -> Optional[models.Calendar]:
    return db.query(models.Calendar).filter(models.Calendar.id == calendar_id).first()

def update_calendar(db: Session, calendar_id: int, calendar: schemas.CalendarBase) -> Optional[models.Calendar]:
    db_calendar = db.query(models.Calendar).filter(models.Calendar.id == calendar_id).first()
    if db_calendar is None:
        return None
    db_calendar.name = calendar.name
    db.commit()
    db.refresh(db_calendar)
    return db_calendar

def delete_calendar(db: Session, calendar_id: int) -> Optional[models.Calendar]:
    db_calendar = db.query(models.Calendar).filter(models.Calendar.id == calendar_id).first()
    if db_calendar is None:
        return None
    db.delete(db_calendar)
    db.commit()
    return db_calendar