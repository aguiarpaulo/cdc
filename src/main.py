import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

data = "data/organizations.csv"
df = pd.read_csv(data)

# get the variables in the .env
HOSTNAME = os.getenv('HOSTNAME')
PORT = os.getenv('PORT')
DATABASE = os.getenv('DATABASE')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
# connect to db
DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
engine = create_engine(DATABASE_URL)

# Database Session, make the queries
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

df.to_sql('organizations', con=engine, if_exists='replace', index=False)
#Base = declarative_base()
#def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()
print(f"{HOSTNAME}")
