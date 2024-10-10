from database import init_db_data  # Ensure that database.py is in the same directory

import sqlite3

# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('Restaurant_food_data.db')
c = conn.cursor()

# Create the item table
c.execute('''
    CREATE TABLE IF NOT EXISTS item (
        Item_name TEXT PRIMARY KEY,
        No_of_customers INTEGER,
        No_of_positive_reviews INTEGER,
        No_of_negative_reviews INTEGER,
        Positive_percentage TEXT,
        Negative_percentage TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")

init_db_data()  # Call the function to initialize the database with food items

