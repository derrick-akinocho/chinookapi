#database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Creates an instance of SQLAlchemy Engine for the "chinook.db" database.
engine = create_engine("sqlite:///../chinook.db", echo=True)

# Creates a session to interact with the database.
session = Session(bind=engine)