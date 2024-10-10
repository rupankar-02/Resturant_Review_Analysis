# database.py
import sqlite3

# Global connection object
conn = sqlite3.connect('Restaurant_food_data.db')
c = conn.cursor()

# List of food items
foods = [
    "Idly", "Dosa", "Vada", "Roti", "Meals", "Veg Biryani", "Egg Biryani",
    "Chicken Biryani", "Mutton Biryani", "Ice Cream", "Noodles",
    "Manchooriya", "Orange juice", "Apple Juice", "Pineapple juice", "Banana juice"
]


def init_db_data():
    """Initialize the database with food items if not already present."""
    for food in foods:
        c.execute("SELECT * FROM item WHERE Item_name = :item_name", {'item_name': food})
        if not c.fetchone():  # Check if the item already exists
            c.execute(
                "INSERT INTO item VALUES(:item_name, :no_of_customers, :no_of_positives, \
                :no_of_negatives, :pos_perc, :neg_perc)",
                {
                    'item_name': food,
                    'no_of_customers': "0",
                    'no_of_positives': "0",
                    'no_of_negatives': "0",
                    'pos_perc': "0.0%",
                    'neg_perc': "0.0%"
                }
            )
    conn.commit()


def update_food_data(selected_foods, res, cv, review):
    """Update the food review data based on sentiment analysis result."""
    for food in selected_foods:
        c.execute("SELECT * FROM item WHERE Item_name=:item_name", {'item_name': food})
        record = c.fetchone()

        if record:  # Ensure the record exists before updating
            n_cust = int(record[1]) + 1
            n_pos = int(record[2]) + (1 if res[0] == 1 else 0)
            n_neg = int(record[3]) + (1 if res[0] == 0 else 0)
            pos_percent = round((n_pos / n_cust) * 100, 1)
            neg_percent = round((n_neg / n_cust) * 100, 1)

            c.execute(
                """UPDATE item SET No_of_customers=:no_of_customers, No_of_positive_reviews=:no_of_positives, 
                No_of_negative_reviews=:no_of_negatives, Positive_percentage=:pos_perc, 
                Negative_percentage=:neg_perc WHERE Item_name=:item_name""",
                {
                    'no_of_customers': str(n_cust),
                    'no_of_positives': str(n_pos),
                    'no_of_negatives': str(n_neg),
                    'pos_perc': str(pos_percent) + "%",
                    'neg_perc': str(neg_percent) + "%",
                    'item_name': food
                }
            )
    conn.commit()


def get_food_data():
    """Fetch all food data for analysis."""
    c.execute("SELECT * FROM item")
    return c.fetchall()
