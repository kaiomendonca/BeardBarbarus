from sqlalchemy import Column, String, Integer
from database.connection import Base


class Service(Base):
    __tablename__ = "services"
    
    id = Column(Integer, primary_key=True, index=True)
    name_service = Column(String(100), nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    
    appointment_services = relationship(
        "AppointmentService",
        back_populates="service"
    )