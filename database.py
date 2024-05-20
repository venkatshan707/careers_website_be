import sqlalchemy
import azureconfig

from sqlalchemy import create_engine, MetaData, Column, Integer, String, ForeignKey, Table

import pyodbc

SERVER = azureconfig.server
DATABASE = azureconfig.database
USERNAME = azureconfig.username
PASSWORD = azureconfig.password

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)

SQL_QUERY = """
SELECT * FROM dbo.jobs;
"""


cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
            print(f"{r.CustomerID}\t{r.OrderCount}\t{r.CompanyName}")

# # Azure SQL Database credentials
# from azureconfig import server, database, username, password, driver

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# print("version", sqlalchemy.__version__)

# # Construct the connection string using imported credentials
# conn_str = (f"mssql+pyodbc://"
#             f"{username}:{password}@{server}/{database}"
#             f"?driver={driver}")

# # Create the SQLAlchemy engine
# engine = create_engine(
#     conn_str, echo=True)  # Set echo=True for debugging, it prints SQL queries

# # Define metadata
# metadata = MetaData()

# # Define a sample table
# users = Table('users', metadata, Column('id', Integer, primary_key=True),
#               Column('name', String(50)), Column('email', String(50)))

# # Create all tables defined in metadata
# metadata.create_all(engine)

# # Example usage: insert data into the table
# conn = engine.connect()
# conn.execute(users.insert().values(name='John Doe', email='john@example.com'))

# # Close the connection
# conn.close()
