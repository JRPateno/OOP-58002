import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\sayom\OneDrive\Documents\Database3.accdb:')
    print("Database is connected")

    user_id = 6
    record = connection.cursor()
    record.execute('delete from Table1 WHERE id=?')
    record.commit()
    print("Data is deleted")

except pyodbc.Error as e:
    print("Error in connection")