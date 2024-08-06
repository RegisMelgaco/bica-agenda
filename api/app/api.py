from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db, init_db
import schemas
import crud
import strings

app = FastAPI()

# CRUD Endpoints for Calendar
@app.post("/calendars/", response_model=schemas.Calendar)
def create_calendar(calendar: schemas.CalendarCreate, db: Session = Depends(get_db)):
    return crud.create_calendar(db=db, calendar=calendar)

@app.get("/calendars/{calendar_id}", response_model=schemas.Calendar)
def read_calendar(calendar_id: int, db: Session = Depends(get_db)):
    calendar = crud.read_calendar(db=db, calendar_id=calendar_id)
    if calendar is None:
        raise HTTPException(status_code=404, detail=strings.CALENDAR_NOT_FOUND)
    return calendar

@app.put("/calendars/{calendar_id}", response_model=schemas.Calendar)
def update_calendar(calendar_id: int, calendar: schemas.CalendarBase, db: Session = Depends(get_db)):
    calendar = crud.update_calendar(db=db, calendar_id=calendar_id, calendar=calendar)
    if calendar is None:
        raise HTTPException(status_code=404, detail=strings.CALENDAR_NOT_FOUND)
    return calendar

@app.delete("/calendars/{calendar_id}", response_model=schemas.Calendar)
def delete_calendar(calendar_id: int, db: Session = Depends(get_db)):
    calendar = crud.delete_calendar(db=db, calendar_id=calendar_id)
    if calendar is None:
        raise HTTPException(status_code=404, detail=strings.CALENDAR_NOT_FOUND)
    return calendar

@app.get("/heathcheck")
async def root():
    return "OK"

if __name__ == "__main__":
    import uvicorn
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)