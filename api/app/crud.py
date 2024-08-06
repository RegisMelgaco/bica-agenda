from sqlalchemy.orm import Session
from typing import Optional
import models
import schemas

# Calendar

def create_calendar(db: Session, calendar: schemas.CalendarCreate) -> models.Calendar:
    db_calendar = models.Calendar(name=calendar.name)
    db.add(db_calendar)
    db.commit()
    db.refresh(db_calendar)
    return db_calendar

def get_calendar(db: Session, calendar_id: int) -> Optional[models.Calendar]:
    return db.query(models.Calendar).filter(models.Calendar.id == calendar_id).first()

def get_calendars(db: Session, skip: int = 0, limit: int = 100) -> list[models.Calendar]:
    return db.query(models.Calendar).offset(skip).limit(limit).all()

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

# Client

def create_client(db: Session, client: schemas.ClientCreate) -> models.Client:
    db_client = models.Client(name=client.name, phone=client.phone)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client(db: Session, client_id: int) -> Optional[models.Client]:
    return db.query(models.Client).filter(models.Client.id == client_id).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100) -> list[models.Client]:
    return db.query(models.Client).offset(skip).limit(limit).all()

def update_client(db: Session, client_id: int, client: schemas.ClientBase) -> Optional[models.Client]:
    db_client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if db_client is None:
        return None
    db_client.name = client.name
    db_client.phone = client.phone
    db.commit()
    db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int) -> Optional[models.Client]:
    db_client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if db_client is None:
        return None
    db.delete(db_client)
    db.commit()
    return db_client

# Confirmation Configuration

def create_confirmation_configuration(db: Session, confirmation_configuration: schemas.ConfirmationConfigurationCreate) -> models.ConfirmationConfiguration:
    db_confirmation_configuration = models.ConfirmationConfiguration(
        calendar_id = confirmation_configuration.calendar_id,
        advance_min = confirmation_configuration.advance_min,
        whatsapp_enabled = confirmation_configuration.whatsapp_enabled,
        call_enabled = confirmation_configuration.call_enabled,
        sms_enabled = confirmation_configuration.sms_enabled
    )
    db.add(db_confirmation_configuration)
    db.commit()
    db.refresh(db_confirmation_configuration)
    return db_confirmation_configuration

def get_confirmation_configuration(db: Session, confirmation_configuration_id: int) -> Optional[models.ConfirmationConfiguration]:
    return db.query(models.ConfirmationConfiguration).filter(models.ConfirmationConfiguration.id == confirmation_configuration_id).first()

def get_confirmation_configurations(db: Session, skip: int = 0, limit: int = 100) -> list[models.ConfirmationConfiguration]:
    return db.query(models.ConfirmationConfiguration).offset(skip).limit(limit).all()

def get_calendar_confirmation_configuration(db: Session, calendar_id: int) -> Optional[models.ConfirmationConfiguration]:
    return db.query(models.ConfirmationConfiguration).filter(models.ConfirmationConfiguration.calendar_id == calendar_id).first()

def update_confirmation_configuration(db: Session, confirmation_configuration_id: int, confirmation_configuration: schemas.ConfirmationConfigurationBase) -> Optional[models.ConfirmationConfiguration]:
    db_confirmation_configuration = db.query(models.ConfirmationConfiguration).filter(models.ConfirmationConfiguration.id == confirmation_configuration_id).first()
    if db_confirmation_configuration is None:
        return None
    db_confirmation_configuration.calendar_id = confirmation_configuration.calendar_id
    db_confirmation_configuration.advance_min = confirmation_configuration.advance_min
    db_confirmation_configuration.whatsapp_enabled = confirmation_configuration.whatsapp_enabled
    db_confirmation_configuration.call_enabled = confirmation_configuration.call_enabled
    db_confirmation_configuration.sms_enabled = confirmation_configuration.sms_enabled
    db.commit()
    db.refresh(db_confirmation_configuration)
    return db_confirmation_configuration

def update_calendar_confirmation_configuration(db: Session, calendar_id: int, confirmation_configuration: schemas.ConfirmationConfigurationBase) -> Optional[models.ConfirmationConfiguration]:
    db_confirmation_configuration = db.query(models.ConfirmationConfiguration).filter(models.ConfirmationConfiguration.calendar_id == calendar_id).first()
    if db_confirmation_configuration is None:
        return None
    db_confirmation_configuration.calendar_id = confirmation_configuration.calendar_id
    db_confirmation_configuration.advance_min = confirmation_configuration.advance_min
    db_confirmation_configuration.whatsapp_enabled = confirmation_configuration.whatsapp_enabled
    db_confirmation_configuration.call_enabled = confirmation_configuration.call_enabled
    db_confirmation_configuration.sms_enabled = confirmation_configuration.sms_enabled
    db.commit()
    db.refresh(db_confirmation_configuration)
    return db_confirmation_configuration

def delete_confirmation_configuration(db: Session, confirmation_configuration_id: int) -> Optional[models.ConfirmationConfiguration]:
    db_confirmation_configuration = db.query(models.ConfirmationConfiguration).filter(models.ConfirmationConfiguration.id == confirmation_configuration_id).first()
    if db_confirmation_configuration is None:
        return None
    db.delete(db_confirmation_configuration)
    db.commit()
    return db_confirmation_configuration

def delete_calendar_confirmation_configuration(db: Session, calendar_id: int) -> Optional[models.ConfirmationConfiguration]:
    db_confirmation_configuration = db.query(models.ConfirmationConfiguration).filter(models.ConfirmationConfiguration.calendar_id == calendar_id).first()
    if db_confirmation_configuration is None:
        return None
    db.delete(db_confirmation_configuration)
    db.commit()
    return db_confirmation_configuration

# Appointment

def create_appointment(db: Session, appointment: schemas.AppointmentCreate) -> models.Appointment:
    db_appointment = models.Appointment(
        calendar_id = appointment.calendar_id,
        client_id = appointment.client_id,
        start = appointment.start,
        duration_min = appointment.duration_min,
        notes = appointment.notes
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def get_appointment(db: Session, appointment_id: int) -> Optional[models.Appointment]:
    return db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()

def get_appointments(db: Session, skip: int = 0, limit: int = 100) -> list[models.Appointment]:
    return db.query(models.Appointment).offset(skip).limit(limit).all()

def get_calendar_appointments(db: Session, calendar_id: int, skip: int = 0, limit: int = 100) -> list[models.Appointment]:
    return db.query(models.Appointment).filter(models.Appointment.calendar_id == calendar_id).offset(skip).limit(limit).all()

def get_client_appointments(db: Session, client_id: int, skip: int = 0, limit: int = 100) -> list[models.Appointment]:
    return db.query(models.Appointment).filter(models.Appointment.client_id == client_id).offset(skip).limit(limit).all()

def update_appointment(db: Session, appointment_id: int, appointment: schemas.AppointmentBase) -> Optional[models.Appointment]:
    db_appointment = db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
    if db_appointment is None:
        return None
    db_appointment.calendar_id = appointment.calendar_id
    db_appointment.client_id = appointment.client_id
    db_appointment.start = appointment.start
    db_appointment.duration_min = appointment.duration_min
    db_appointment.notes = appointment.notes
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def delete_appointment(db: Session, appointment_id: int) -> Optional[models.Appointment]:
    db_appointment = db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
    if db_appointment is None:
        return None
    db.delete(db_appointment)
    db.commit()
    return db_appointment

# Appointment Confirmation

def create_appointment_confirmation(db: Session, appointment_confirmation: schemas.AppointmentConfirmationCreate) -> models.AppointmentConfirmation:
    db_appointment_confirmation = models.AppointmentConfirmation(
        appointment_id = appointment_confirmation.appointment_id,
        done = appointment_confirmation.done
    )
    db.add(db_appointment_confirmation)
    db.commit()
    db.refresh(db_appointment_confirmation)
    return db_appointment_confirmation

def get_appointment_confirmation(db: Session, appointment_confirmation_id: int) -> Optional[models.AppointmentConfirmation]:
    return db.query(models.AppointmentConfirmation).filter(models.AppointmentConfirmation.id == appointment_confirmation_id).first()

def get_appointment_confirmations(db: Session, skip: int = 0, limit: int = 100) -> list[models.AppointmentConfirmation]:
    return db.query(models.AppointmentConfirmation).offset(skip).limit(limit).all()

def get_appointment_appointment_confirmation(db: Session, appointment_id: int) -> Optional[models.AppointmentConfirmation]:
    return db.query(models.AppointmentConfirmation).filter(models.AppointmentConfirmation.appointment_id == appointment_id).first()

def update_appointment_confirmation(db: Session, appointment_confirmation_id: int, appointment_confirmation: schemas.AppointmentConfirmationBase) -> Optional[models.AppointmentConfirmation]:
    db_appointment_confirmation = db.query(models.AppointmentConfirmation).filter(models.AppointmentConfirmation.id == appointment_confirmation_id).first()
    if db_appointment_confirmation is None:
        return None
    db_appointment_confirmation.appointment_id = appointment_confirmation.appointment_id
    db_appointment_confirmation.done = appointment_confirmation.done
    db.commit()
    db.refresh(db_appointment_confirmation)
    return db_appointment_confirmation

def update_appointment_appointment_confirmation(db: Session, appointment_id: int, appointment_confirmation: schemas.AppointmentConfirmationBase) -> Optional[models.AppointmentConfirmation]:
    db_appointment_confirmation = db.query(models.AppointmentConfirmation).filter(models.AppointmentConfirmation.appointment_id == appointment_id).first()
    if db_appointment_confirmation is None:
        return None
    db_appointment_confirmation.appointment_id = appointment_confirmation.appointment_id
    db_appointment_confirmation.done = appointment_confirmation.done
    db.commit()
    db.refresh(db_appointment_confirmation)
    return db_appointment_confirmation

def delete_appointment_confirmation(db: Session, appointment_confirmation_id: int) -> Optional[models.AppointmentConfirmation]:
    db_appointment_confirmation = db.query(models.AppointmentConfirmation).filter(models.AppointmentConfirmation.id == appointment_confirmation_id).first()
    if db_appointment_confirmation is None:
        return None
    db.delete(db_appointment_confirmation)
    db.commit()
    return db_appointment_confirmation

def delete_appointment_appointment_confirmation(db: Session, appointment_id: int) -> Optional[models.AppointmentConfirmation]:
    db_appointment_confirmation = db.query(models.AppointmentConfirmation).filter(models.AppointmentConfirmation.appointment_id == appointment_id).first()
    if db_appointment_confirmation is None:
        return None
    db.delete(db_appointment_confirmation)
    db.commit()
    return db_appointment_confirmation

# Appointment State

def create_appointment_state(db: Session, appointment_state: schemas.AppointmentStateCreate) -> models.AppointmentState:
    db_appointment_state = models.AppointmentState(
        appointment_id = appointment_state.appointment_id,
        done = appointment_state.done
    )
    db.add(db_appointment_state)
    db.commit()
    db.refresh(db_appointment_state)
    return db_appointment_state

def get_appointment_state(db: Session, appointment_state_id: int) -> Optional[models.AppointmentState]:
    return db.query(models.AppointmentState).filter(models.AppointmentState.id == appointment_state_id).first()

def get_appointment_states(db: Session, skip: int = 0, limit: int = 100) -> list[models.AppointmentState]:
    return db.query(models.AppointmentState).offset(skip).limit(limit).all()

def get_appointment_appointment_states(db: Session, appointment_id: int, skip: int = 0, limit: int = 100) -> list[models.AppointmentState]:
    return db.query(models.AppointmentState).filter(models.AppointmentState.appointment_id == appointment_id).offset(skip).limit(limit).all()

def update_appointment_state(db: Session, appointment_state_id: int, appointment_state: schemas.AppointmentStateBase) -> Optional[models.AppointmentState]:
    db_appointment_state = db.query(models.AppointmentState).filter(models.AppointmentState.id == appointment_state_id).first()
    if db_appointment_state is None:
        return None
    db_appointment_state.appointment_id = appointment_state.appointment_id
    db_appointment_state.done = appointment_state.done
    db.commit()
    db.refresh(db_appointment_state)
    return db_appointment_state

def delete_appointment_state(db: Session, appointment_state_id: int) -> Optional[models.AppointmentState]:
    db_appointment_state = db.query(models.AppointmentState).filter(models.AppointmentState.id == appointment_state_id).first()
    if db_appointment_state is None:
        return None
    db.delete(db_appointment_state)
    db.commit()
    return db_appointment_state