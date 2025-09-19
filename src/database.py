"""Database configuration and connection setup."""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Get database URL from environment variable or use SQLite as fallback
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./activities.db')

# Create database engine
engine = create_engine(DATABASE_URL)

# Create database session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database by creating all tables."""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()