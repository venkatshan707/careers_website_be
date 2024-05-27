import sqlalchemy
import azureconfig

from sqlalchemy import create_engine, MetaData, Column, Integer, String, ForeignKey, Table, text
from sqlalchemy.orm import sessionmaker

import pyodbc

SERVER = azureconfig.server
DATABASE = azureconfig.database
USERNAME = azureconfig.username
PASSWORD = azureconfig.password

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'


conn = pyodbc.connect(connectionString)

SQL_QUERY = """
SELECT * FROM dbo.jobs;
"""

print ("SQLalchemy Version:", sqlalchemy.__version__)

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
            print(f"{r.id}\t{r.title}\t{r.location}\t{r.currency} {r.salary}")








# Create an engine
engine = create_engine(f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver=ODBC+Driver+18+for+SQL+Server")


with engine.connect() as conn: # Giving name to the connection established by the engine as conn
        # Then is connection used to execute SQL commands 
        print ("\n","Interaction with SQL Engine".center(40, '#'),"\n") 
        result = conn.execute(text('SELECT * FROM dbo.jobs'))

        print (f"Type of result :{type(result)}")# type of result is a <class 'sqlalchemy.engine.cursor.CursorResult'>


        #Converting SQLalchemy row in to dictionary
        #Actually our database have column names and values to it. we can think of like key : value pair 
        #we can achieve key value pair, by typecasting each row as dict  
        
        result_as_dict =result.mappings().all()# Converting as dictionary

        """The mappings() method of the CursorResult object returns a RowProxy object, which is a row-level collection of 
        result columns. The all() method then converts this RowProxy object into a list of dictionaries, where each dictionary
         represents a row in the result set."""

        print(type(result_as_dict))#the result_as_dict variable will be a list of dictionaries, where each dictionary represents a row in the users table.
        
        
        for r in result_as_dict:        
            print(f"{r.id}\t{r.title}\t{r.location}\t{r.currency} {r.salary}")
# when we comming out of 'with' our connection will be automatically closed 

