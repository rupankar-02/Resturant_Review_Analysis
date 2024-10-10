from database import c


def view_database_contents():
    """View the current contents of the item table."""
    c.execute("SELECT * FROM item")
    rows = c.fetchall()
    for row in rows:
        print(row)

# Call the function
view_database_contents()

