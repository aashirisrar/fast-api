from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database setup
SQLALCHEMY_DATABASE_URL = "postgresql://aashir:admin@localhost/fast_api"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get a DB session
def get_database_session():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
