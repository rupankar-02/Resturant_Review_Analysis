# analysis.py
from tkinter import *
from database import get_food_data


def display_data():
    """Display food data in a new window."""
    root4 = Toplevel()
    root4.title("Restaurant Review Analysis System/View Details")

    label = Label(root4, text="RESTAURANT REVIEW ANALYSIS SYSTEM", bd=2,
                  font=('Arial', 47, 'bold', 'underline'))

    label2 = Label(root4, text="VIEW DETAILS", font=('Helvetica', 30, 'bold', 'underline'))
    req = Label(root4, text="Here are the food items with their reviews", font=('Helvetica', 20, 'bold'))

    food_data = get_food_data()

    text_area = Text(root4, height=20, width=100)
    text_area.insert(END,
                     f"{'Item':<20}{'Customers':<15}{'Positive':<10}{'Negative':<10}{'Positive %':<10}{'Negative %':<10}\n")

    for rec in food_data:
        text_area.insert(END, f"{rec[0]:<20}{rec[1]:<15}{rec[2]:<10}{rec[3]:<10}{rec[4]:<10}{rec[5]:<10}\n")

    text_area.grid(row=3, column=0, columnspan=4, padx=20)

    root4.attributes("-zoomed", True)
    label.grid(row=0, column=0, columnspan=4)
    label2.grid(row=1, column=0, columnspan=4)
    req.grid(row=2, column=0, columnspan=4)
