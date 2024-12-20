import os 
import psycopg2
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def load_data_from_postgres(query):
    
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        df = pd.read_sql_query(query, connection)

        connection.close()

        return df
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def load_data_using_sqlalchemy(query):
    
    try:

        connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

        engine = create_engine(connection_string)

        df = read_sql_query(query, engine)
    
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None