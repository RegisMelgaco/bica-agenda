from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

database = os.environ.get("DATABASE_NAME", "postgres")
host = os.environ.get("DATABASE_HOST", "localhost")
user = os.environ.get("DATABASE_USER", "postgres")
password = os.environ.get("DATABASE_PASSWORD", "secr3t")
port = os.environ.get("DATABASE_PORT", "5432")

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

from models import *
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)
    # SessionLocal.add(
    #     User(username="testuser", password_hash=b"", password_salt=b"", balance=1)
    # )
    # SessionLocal.commit()
    print("Initialized the db")