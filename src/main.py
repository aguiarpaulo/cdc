import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

data = "data/organizations.csv"
df = pd.read_csv(data)

# connect to db
engine = create_engine("postgresql://username:password@postgres/database")

# Database Session, make the queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
