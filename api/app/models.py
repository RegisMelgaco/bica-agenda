from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

# Models
class Calendar(Base):
    __tablename__ = "calendar"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

class Client(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    phone = Column(String(20))

class ConfirmationConfiguration(Base):
    __tablename__ = "confirmation_configuration"
    id = Column(Integer, primary_key=True, index=True)
    calendar_id = Column(Integer, ForeignKey('calendar.id', ondelete='CASCADE', onupdate='CASCADE'))
    advance_min = Column(Integer)
    whatsapp_enabled = Column(Boolean)
    call_enabled = Column(Boolean)
    sms_enabled = Column(Boolean)
    calendar = relationship("Calendar", back_populates="confirmation_configurations")

class Appointment(Base):
    __tablename__ = "appointment"
    id = Column(Integer, primary_key=True, index=True)
    calendar_id = Column(Integer, ForeignKey('calendar.id', ondelete='CASCADE', onupdate='CASCADE'))
    client_id = Column(Integer, ForeignKey('client.id', ondelete='CASCADE', onupdate='CASCADE'))
    start = Column(TIMESTAMP)
    duration_min = Column(Integer)
    notes = Column(String(255))
    calendar = relationship("Calendar", back_populates="appointments")
    client = relationship("Client", back_populates="appointments")

class AppointmentConfirmation(Base):
    __tablename__ = "appointment_confirmation"
    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey('appointment.id', ondelete='CASCADE', onupdate='CASCADE'))
    done = Column(Boolean)
    appointment = relationship("Appointment", back_populates="confirmations")

class AppointmentState(Base):
    __tablename__ = "appointment_state"
    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey('appointment.id', ondelete='CASCADE', onupdate='CASCADE'))
    description = Column(String(100))
    appointment = relationship("Appointment", back_populates="states")

# Relationships
Calendar.confirmation_configurations = relationship("ConfirmationConfiguration", back_populates="calendar")
Calendar.appointments = relationship("Appointment", back_populates="calendar")
Client.appointments = relationship("Appointment", back_populates="client")
Appointment.confirmations = relationship("AppointmentConfirmation", back_populates="appointment")
Appointment.states = relationship("AppointmentState", back_populates="appointment")