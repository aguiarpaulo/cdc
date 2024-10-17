import pandas as pd
import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

data = "../data/organizations.csv"
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

# Use the inspector to check if the table already exists
inspector = inspect(engine)
table_name = 'organizations'

# Check if the table already exists in the database
if not inspector.has_table(table_name):
    # If the table does not exist, create it
    df.to_sql('organizations', con=engine, if_exists='replace', index=False)
    print("Table created and data inserted successfully!")
else:
    print(f"The table '{table_name}' already exists. No action was taken.")