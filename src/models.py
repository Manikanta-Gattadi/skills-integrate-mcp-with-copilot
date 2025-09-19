"""Database models for the application."""
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table
from sqlalchemy.sql.sqltypes import DateTime
from datetime import datetime

Base = declarative_base()

class Activity(Base):
    """Activity model representing an extracurricular activity."""
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    schedule = Column(String, nullable=False)
    max_participants = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Define relationship with participants
    participants = relationship('Participant', back_populates='activity', cascade='all, delete-orphan')

class Participant(Base):
    """Participant model representing a student enrolled in an activity."""
    __tablename__ = 'participants'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    activity_id = Column(Integer, ForeignKey('activities.id'), nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)

    # Define relationship with activity
    activity = relationship('Activity', back_populates='participants')