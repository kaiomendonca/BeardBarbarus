from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from database.connection import Base
import Enum

class UserRole(enum.Enum):
    ADMIN = "admin"
    PROFESSIONAL = "professional"
    CLIENT = "client"
    
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.CLIENT, nullable=False)
    
    appointments_as_client = relationship(
        "Appointment",
        back_populates= "client"
        foreign_keys = "Appointment.user_id"
    )
    
    appointments_as_professional = relationship(
        "Appointment",
        back_populates = "professional"
        foreign_keys = "Appointment.professional_id"
    )
    

