import sqlite3
# Connect (or create) the database file
connection = sqlite3.connect("users.db") #creates a database file named users.db
cursor = connection.cursor() #a cursor is your tool to run SQL commands 

# Create the users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

connection.commit() #saves changes into database
connection.close() #close connection to database

print("✅ Database and users table created.")