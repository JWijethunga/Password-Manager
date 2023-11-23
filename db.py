import sqlite3
import tkinter as tk
from tkinter import ttk

"""
database_name = 'users.db'

# Connect to the SQLite database (this will create a new database if it doesn't exist)
def connet_database(dbname):
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()

# Create the 'users' table
def create_user_table(dbname):
    connet_database(dbname)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )   
    ''')
    connection.commit()

def auth_login(dbname,username,passwd):
    connet_database(dbname)
    cursor.execute(f'''
    SELECT password FROM users WHERE username={username}; 
    )
''')
    pw = cursor.fetchone()
    if passwd==pw:
        mainWindow.mainloop()

# Commit the changes and close the connection
connection.commit()
connection.close()
"""

class SQLiteDB:
    def __init__(self, db_name='pwmang.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, data):
        columns = ', '.join(data.keys())
        values = ', '.join([f'"{value}"' for value in data.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.cursor.execute(query)
        self.conn.commit()

    def checkpw(self, table_name,username):
        query = f"SELECT pw FROM {table_name} WHERE username=?"
        self.cursor.execute(query, (username,))
        return self.cursor.fetchone()
    """
    def addData(self,table_name,site,username,password):
        query = f"INSERT INTO {table_name}(site,username,passwd) VALUES ({site,username,password})"
        self.cursor.execute(query)
        self.conn.commit()
    """
    def addData(self, table_name, site, username, password):
        query = f"INSERT INTO {table_name} (site, username, passwd) VALUES (?, ?, ?)"
        values = (site, username, password)

        self.cursor.execute(query, values)
        self.conn.commit()



    def getData(self,table_name):
        query = f"SELECT id,username,passwd FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    #query = f"SELECT pw FROM {table_name} WHERE username={username}"
    #self.cursor.execute(query)
       
       
    def update_data(self, table_name, set_values, condition):
        set_clause = ', '.join([f"{key} = '{value}'" for key, value in set_values.items()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_data(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
"""
# Example usage:
db = SQLiteDB()
db.connect()

# Create a table
db.create_table('users', ['id INTEGER PRIMARY KEY', 'name TEXT', 'email TEXT'])

# Insert data
user_data = {'name': 'John Doe', 'email': 'john@example.com'}
db.insert_data('users', user_data)

# Query data
result = db.query_data('users')
print(result)

# Update data
update_values = {'name': 'Jane Doe'}
db.update_data('users', update_values, 'id = 1')

# Query data after update
result_after_update = db.query_data('users')
print(result_after_update)

# Delete data
db.delete_data('users', 'id = 1')

# Query data after delete
result_after_delete = db.query_data('users')
print(result_after_delete)

# Close the connection
db.close_connection()


"""