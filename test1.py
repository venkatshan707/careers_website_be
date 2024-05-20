import pyodbc

# Get a list of all available ODBC drivers
drivers = pyodbc.drivers()
print("Available ODBC drivers:")
for driver in drivers:
    print(driver)
