from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Update these with your local PostgreSQL credentials
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/retail_banking"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Helper to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
