import sqlalchemy
import azureconfig

from sqlalchemy import create_engine, MetaData, Column, Integer, String, ForeignKey, Table, text
from sqlalchemy.orm import sessionmaker

import pyodbc

import os

from dotenv import load_dotenv
load_dotenv('.env')
USERNAME:str =os.getenv('user')
SERVER:str =os.getenv('server')
DATABASE:str =os.getenv('database')
PASSWORD:str =os.getenv('password')

connectionString = f'Driver={{ODBC Driver 18 for SQL Server}};Server={SERVER},1433;Database={DATABASE};Uid={USERNAME};Pwd={PASSWORD};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
print(connectionString)


conn = pyodbc.connect(connectionString)

SQL_QUERY = """
SELECT * FROM dbo.jobs;
"""

print ("SQLalchemy Version:", sqlalchemy.__version__)

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
# for r in records:
#             print(f"{r.id}\t{r.title}\t{r.location}\t{r.currency} {r.salary}")








# Create an engine
engine = create_engine(f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver=ODBC+Driver+18+for+SQL+Server")


def load_jobs_from_db():
  with engine.connect() as conn: # Giving name to the connection established by the engine as conn
        # Then is connection used to execute SQL commands 
        print ("\n","Interaction with SQL Engine".center(40, '#'),"\n") 
        result = conn.execute(text('SELECT * FROM dbo.jobs'))

        print (f"Type of result :{type(result)}")# type of result is a <class 'sqlalchemy.engine.cursor.CursorResult'>


        #Converting SQLalchemy row in to dictionary
        #Actually our database have column names and values to it. we can think of like key : value pair 
        #we can achieve key value pair, by typecasting each row as dict  
        
        jobs_as_list_of_dict =  [dict(row) for row in result.mappings().all()]# Converting as dictionary
        
        #The expression [dict(row) for row in result.mappings().all()] is a list comprehension that converts 
        #a CursorResult object (returned by a SQLAlchemy database query) into a list of dictionaries, which is particularly useful for JSON serialization
        
        print("Type :  ",type(jobs_as_list_of_dict))#the result_as_dict variable will be a list of dictionaries, where each dictionary represents a row in the users table.
        
        
        # for r in jobs_as_list_of_dict:        
        #     print(f"{r.id}\t{r.title}\t{r.location}\t{r.currency} {r.salary}")
        return jobs_as_list_of_dict  
      # # when we comming out of 'with' our connection will be automatically closed 
        
