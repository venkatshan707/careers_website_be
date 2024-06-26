import sqlalchemy
#import azureconfig

from sqlalchemy import create_engine, MetaData, Column, Integer, String, ForeignKey, Table, text
from sqlalchemy.orm import sessionmaker

import pyodbc

import os

from dotenv import load_dotenv


if load_dotenv('.env') ==True:

  USERNAME:str =os.getenv('user')
  SERVER:str =os.getenv('server')
  DATABASE:str =os.getenv('database')
  PASSWORD:str =os.getenv('password')

  connectionString = f'Driver={{ODBC Driver 18 for SQL Server}};Server={SERVER},1433;Database={DATABASE};Uid={USERNAME};Pwd={PASSWORD};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
  # print(connectionString)
else :
  connectionString = f'Driver={{ODBC Driver 18 for SQL Server}};Server={server},1433;Database={database};Uid={user};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
  # print(connectionString)

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

Session = sessionmaker(bind=engine)
session = Session()
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
        
def load_job_from_db(id):
   with engine.connect() as conn:
        
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})
        row = result.first()
        if row is None:
            return None
        else:
            return row._asdict()
        
def add_application_to_db(id, application):
  with engine.connect() as conn:
          session = Session()
          
          query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
          
          
        #   params = {
        #     'job_id': id,
        #     'full_name': application["full_name"],
        #     'email': application["email"],
        #     'linkedin_url': application["linkedin_url"],
        #     'education': application["education"],
        #     'work_experience': application["experience"],
        #     'resume_url': application["resume_url"]
        # }
          cursor.execute(f"INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (?,?,?,?,?,?,?)", id, application["full_name"], application["email"], application["linkedin_url"], application["education"], application["experience"], application["resume_url"]) 
          print("Data inserted successfully")
          cursor.commit()
          