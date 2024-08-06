from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CalendarBase(BaseModel):
    name: str

class CalendarCreate(CalendarBase):
    pass

class Calendar(CalendarBase):
    id: int

    class Config:
        orm_mode: True

class ClientBase(BaseModel):
    name: str
    phone: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    class Config:
        orm_mode: True

class ConfirmationConfigurationBase(BaseModel):
    calendar_id: int
    advance_min: Optional[int]
    whatsapp_enabled: Optional[bool]
    call_enabled: Optional[bool]
    sms_enabled: Optional[bool]

class ConfirmationConfigurationCreate(ConfirmationConfigurationBase):
    pass

class ConfirmationConfiguration(ConfirmationConfigurationBase):
    id: int

    class Config:
        orm_mode: True

class AppointmentBase(BaseModel):
    calendar_id: int
    client_id: int
    start: datetime
    duration_min: Optional[int]
    notes: Optional[str]

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int

    class Config:
        orm_mode: True

class AppointmentConfirmationBase(BaseModel):
    appointment_id: int
    done: Optional[bool]

class AppointmentConfirmationCreate(AppointmentConfirmationBase):
    pass

class AppointmentConfirmation(AppointmentConfirmationBase):
    id: int

    class Config:
        orm_mode: True

class AppointmentStateBase(BaseModel):
    appointment_id: int
    description: str

class AppointmentStateCreate(AppointmentStateBase):
    pass

class AppointmentState(AppointmentStateBase):
    id: int

    class Config:
        orm_mode: True