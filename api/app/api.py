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
def get_calendar(calendar_id: int, db: Session = Depends(get_db)):
    calendar = crud.get_calendar(db=db, calendar_id=calendar_id)
    if calendar is None:
        raise HTTPException(status_code=404, detail=strings.CALENDAR_NOT_FOUND)
    return calendar

@app.get("/calendars/", response_model=list[schemas.Calendar])
def get_calendars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    calendars = crud.get_calendars(db, skip=skip, limit=limit)
    return calendars

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

# CRUD Endpoints for Client
@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db=db, client=client)

@app.get("/clients/{client_id}", response_model=schemas.Client)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = crud.get_client(db=db, client_id=client_id)
    if client is None:
        raise HTTPException(status_code=404, detail=strings.CLIENT_NOT_FOUND)
    return client

@app.get("/clients/", response_model=list[schemas.Client])
def get_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients

@app.put("/clients/{client_id}", response_model=schemas.Client)
def update_client(client_id: int, client: schemas.ClientBase, db: Session = Depends(get_db)):
    client = crud.update_client(db=db, client_id=client_id, client=client)
    if client is None:
        raise HTTPException(status_code=404, detail=strings.CLIENT_NOT_FOUND)
    return client

@app.delete("/clients/{client_id}", response_model=schemas.Client)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = crud.delete_client(db=db, client_id=client_id)
    if client is None:
        raise HTTPException(status_code=404, detail=strings.CLIENT_NOT_FOUND)
    return client

# CRUD Endpoints for ConfirmationConfiguration
@app.post("/confirmation_configurations/", response_model=schemas.ConfirmationConfiguration)
def create_confirmation_configuration(confirmation_configuration: schemas.ConfirmationConfigurationCreate, db: Session = Depends(get_db)):
    return crud.create_confirmation_configuration(db=db, confirmation_configuration=confirmation_configuration)

@app.get("/confirmation_configurations/{confirmation_configuration_id}", response_model=schemas.ConfirmationConfiguration)
def get_confirmation_configuration(confirmation_configuration_id: int, db: Session = Depends(get_db)):
    confirmation_configuration = crud.get_confirmation_configuration(db=db, confirmation_configuration_id=confirmation_configuration_id)
    if confirmation_configuration is None:
        raise HTTPException(status_code=404, detail=strings.CONFIRMATION_CONFIGURATION_NOT_FOUND)
    return confirmation_configuration

@app.get("/confirmation_configurations/", response_model=list[schemas.ConfirmationConfiguration])
def get_confirmation_configurations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    confirmation_configurations = crud.get_confirmation_configurations(db, skip=skip, limit=limit)
    return confirmation_configurations

@app.get("/calendar_confirmation_configuration/{calendar_id}", response_model=schemas.ConfirmationConfiguration)
def get_calendar_confirmation_configuration(calendar_id: int, db: Session = Depends(get_db)):
    confirmation_configuration = crud.get_calendar_confirmation_configuration(db=db, calendar_id=calendar_id)
    if confirmation_configuration is None:
        raise HTTPException(status_code=404, detail=strings.CONFIRMATION_CONFIGURATION_NOT_FOUND)
    return confirmation_configuration

@app.put("/confirmation_configurations/{confirmation_configuration_id}", response_model=schemas.ConfirmationConfiguration)
def update_confirmation_configuration(confirmation_configuration_id: int, confirmation_configuration: schemas.ConfirmationConfigurationBase, db: Session = Depends(get_db)):
    confirmation_configuration = crud.update_confirmation_configuration(db=db, confirmation_configuration_id=confirmation_configuration_id, confirmation_configuration=confirmation_configuration)
    if confirmation_configuration is None:
        raise HTTPException(status_code=404, detail=strings.CONFIRMATION_CONFIGURATION_NOT_FOUND)
    return confirmation_configuration

@app.put("/calendar_confirmation_configuration/{calendar_id}", response_model=schemas.ConfirmationConfiguration)
def update_calendar_confirmation_configuration(calendar_id: int, confirmation_configuration: schemas.ConfirmationConfigurationBase, db: Session = Depends(get_db)):
    confirmation_configuration = crud.update_calendar_confirmation_configuration(db=db, calendar_id=calendar_id, confirmation_configuration=confirmation_configuration)
    if confirmation_configuration is None:
        raise HTTPException(status_code=404, detail=strings.CONFIRMATION_CONFIGURATION_NOT_FOUND)
    return confirmation_configuration

@app.delete("/confirmation_configurations/{confirmation_configuration_id}", response_model=schemas.ConfirmationConfiguration)
def delete_confirmation_configuration(confirmation_configuration_id: int, db: Session = Depends(get_db)):
    confirmation_configuration = crud.delete_confirmation_configuration(db=db, confirmation_configuration_id=confirmation_configuration_id)
    if confirmation_configuration is None:
        raise HTTPException(status_code=404, detail=strings.CONFIRMATION_CONFIGURATION_NOT_FOUND)
    return confirmation_configuration

@app.delete("/calendar_confirmation_configuration/{calendar_id}", response_model=schemas.ConfirmationConfiguration)
def delete_calendar_confirmation_configuration(calendar_id: int, db: Session = Depends(get_db)):
    confirmation_configuration = crud.delete_calendar_confirmation_configuration(db=db, calendar_id=calendar_id)
    if confirmation_configuration is None:
        raise HTTPException(status_code=404, detail=strings.CONFIRMATION_CONFIGURATION_NOT_FOUND)
    return confirmation_configuration

# CRUD Endpoints for Appointment
@app.post("/appointments/", response_model=schemas.Appointment)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    return crud.create_appointment(db=db, appointment=appointment)

@app.get("/appointments/{appointment_id}", response_model=schemas.Appointment)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = crud.get_appointment(db=db, appointment_id=appointment_id)
    if appointment is None:
        raise HTTPException(status_code=404, detail=strings.APPOINTMENT_NOT_FOUND)
    return appointment

@app.get("/appointments/", response_model=list[schemas.Appointment])
def get_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointments = crud.get_appointments(db, skip=skip, limit=limit)
    return appointments

@app.get("/calendar_appointments/", response_model=schemas.Appointment)
def get_calendar_appointments(calendar_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointments = crud.get_calendar_appointments(db=db, calendar_id=calendar_id, skip=skip, limit=limit)
    return appointments

@app.get("/client_appointments/", response_model=schemas.Appointment)
def get_client_appointments(client_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointments = crud.get_client_appointments(db=db, client_id=client_id, skip=skip, limit=limit)
    return appointments

@app.put("/appointments/{appointment_id}", response_model=schemas.Appointment)
def update_appointment(appointment_id: int, appointment: schemas.AppointmentBase, db: Session = Depends(get_db)):
    appointment = crud.update_appointment(db=db, appointment_id=appointment_id, appointment=appointment)
    if appointment is None:
        raise HTTPException(status_code=404, detail=strings.APPOINTMENT_NOT_FOUND)
    return appointment

@app.delete("/appointments/{appointment_id}", response_model=schemas.Appointment)
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = crud.delete_appointment(db=db, appointment_id=appointment_id)
    if appointment is None:
        raise HTTPException(status_code=404, detail=strings.APPOINTMENT_NOT_FOUND)
    return appointment

# CRUD Endpoints for AppointmentConfirmation
@app.post("/appointment_confirmations/", response_model=schemas.AppointmentConfirmation)
def create_appointment_confirmation(appointment_confirmation: schemas.AppointmentConfirmationCreate, db: Session = Depends(get_db)):
    return crud.create_appointment_confirmation(db=db, appointment_confirmation=appointment_confirmation)

@app.get("/appointment_confirmations/{appointment_confirmation_id}", response_model=schemas.AppointmentConfirmation)
def get_appointment_confirmation(appointment_confirmation_id: int, db: Session = Depends(get_db)):
    appointment_confirmation = crud.get_appointment_confirmation(db=db, appointment_confirmation_id=appointment_confirmation_id)
    if appointment_confirmation is None:
        raise HTTPException(status_code=404, detail=strings.APPOINTMENT_CONFIRMATION_NOT_FOUND)
    return appointment_confirmation

@app.get("/appointment_confirmations/", response_model=list[schemas.AppointmentConfirmation])
def get_appointment_confirmations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointment_confirmations = crud.get_appointment_confirmations(db, skip=skip, limit=limit)
    return appointment_confirmations

@app.get("/appointment_appointment_confirmation/{appointment_id}", response_model=schemas.AppointmentConfirmation)
def get_appointment_appointment_confirmation(appointment_id: int, db: Session = Depends(get_db)):
    appointment_confirmation = crud.get_appointment_appointment_confirmation(db=db, appointment_id=appointment_id)
    if appointment_confirmation is None:
        raise HTTPException(status_code=404, detail=strings.APPOINTMENT_CONFIRMATION_NOT_FOUND)
    return appointment_confirmation

@app.put("/appointment_confirmations/{appointment_confirmation_id}", response_model=schemas.AppointmentConfirmation)
def update_appointment_confirmation(appointment_confirmation_id: int, appointment_confirmation: schemas.AppointmentConfirmationBase, db: Session = Depends(get_db)):
    appointment_confirmation = crud.update_appointment_confirmation(db=db, appointment_confirmation_id=appointment_confirmation_id, appointment_confirmation=appointment_confirmation)
    if appointment_confirmation is None:
        raise HTTPException(status_code=404, detail=strings.APPOINTMENT_CONFIRMATION_NOT_FOUND)
    return appointment_confirmation

@app.put("/appointment_appointment_confirmation/{appointment_id}", response_model=schemas.AppointmentConfirmation)
def update_appointment_appointment_confirmation(appointment_id: int, appointment_confirmation: schemas.AppointmentConfirmationBase, db: Session = Depends(get_db)):
    appointment_confirmation = crud.update_appointment_appointment_confirmation(db=db, appointment_id=appointment_id, appointment_confirmation=appointment_confirmation)
    if appointment_confirmation is None:
        raise HTTPException(status_code=404, detail=strings.APPOINTMENT_CONFIRMATION_NOT_FOUND)
    return appointment_confirmation

@app.delete("/appointment_confirmations/{appointment_confirmation_id}", response_model=schemas.AppointmentConfirmation)
def delete_appointment_confirmation(appointment_confirmation_id: int, db: Session = Depends(get_db)):
    appointment_confirmation = crud.delete_appointment_confirmation(db=db, appointment_confirmation_id=appointment_confirmation_id)
    if appointment_confirmation is None:
        raise HTTPException(status_code=404, detail=strings.APPOINTMENT_CONFIRMATION_NOT_FOUND)
    return appointment_confirmation

@app.delete("/appointment_appointment_confirmation/{appointment_id}", response_model=schemas.AppointmentConfirmation)
def delete_appointment_appointment_confirmation(appointment_id: int, db: Session = Depends(get_db)):
    appointment_confirmation = crud.delete_appointment_appointment_confirmation(db=db, appointment_id=appointment_id)
    if appointment_confirmation is None:
        raise HTTPException(status_code=404, detail=strings.APPOINTMENT_CONFIRMATION_NOT_FOUND)
    return appointment_confirmation

# CRUD Endpoints for AppointmentState
@app.post("/appointment_states/", response_model=schemas.AppointmentState)
def create_appointment_state(appointment_state: schemas.AppointmentStateCreate, db: Session = Depends(get_db)):
    return crud.create_appointment_state(db=db, appointment_state=appointment_state)

@app.get("/appointment_states/{appointment_state_id}", response_model=schemas.AppointmentState)
def get_appointment_state(appointment_state_id: int, db: Session = Depends(get_db)):
    appointment_state = crud.get_appointment_state(db=db, appointment_state_id=appointment_state_id)
    if appointment_state is None:
        raise HTTPException(status_code=404, detail=strings.APPOINTMENT_NOT_FOUND)
    return appointment_state

@app.get("/appointment_states/", response_model=list[schemas.AppointmentState])
def get_appointment_states(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointment_states = crud.get_appointment_states(db, skip=skip, limit=limit)
    return appointment_states

@app.get("/appointment_appointment_states/", response_model=schemas.AppointmentState)
def get_appointment_appointment_states(appointment_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointment_states = crud.get_appointment_appointment_states(db=db, appointment_id=appointment_id, skip=skip, limit=limit)
    return appointment_states

@app.put("/appointment_states/{appointment_state_id}", response_model=schemas.AppointmentState)
def update_appointment_state(appointment_state_id: int, appointment_state: schemas.AppointmentStateBase, db: Session = Depends(get_db)):
    appointment_state = crud.update_appointment_state(db=db, appointment_state_id=appointment_state_id, appointment_state=appointment_state)
    if appointment_state is None:
        raise HTTPException(status_code=404, detail=strings.APPOINTMENT_NOT_FOUND)
    return appointment_state

@app.delete("/appointment_states/{appointment_state_id}", response_model=schemas.AppointmentState)
def delete_appointment_state(appointment_state_id: int, db: Session = Depends(get_db)):
    appointment_state = crud.delete_appointment_state(db=db, appointment_state_id=appointment_state_id)
    if appointment_state is None:
        raise HTTPException(status_code=404, detail=strings.APPOINTMENT_NOT_FOUND)
    return appointment_state

@app.get("/heathcheck")
async def root():
    return "OK"

if __name__ == "__main__":
    import uvicorn
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)