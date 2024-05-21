import sqlalchemy
import azureconfig

from sqlalchemy import create_engine, MetaData, Column, Integer, String, ForeignKey, Table, text

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


cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
            print(f"{r.id}\t{r.title}\t{r.location}\t{r.currency} {r.salary}")








# Create an engine
engine = create_engine(f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver=ODBC+Driver+18+for+SQL+Server")


with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM dbo.jobs'))
        for r in result.fetchall():
            print(f"{r.id}\t{r.title}\t{r.location}\t{r.currency} {r.salary}")
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

# Close the connection
conn.close()
