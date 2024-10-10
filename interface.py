# interface.py
from tkinter import *
from analysis import display_data
from database import update_food_data, get_food_data

variables = []

# List of food items
foods = ["Idly", "Dosa", "Vada", "Roti", "Meals", "Veg Biryani",
         "Egg Biryani", "Chicken Biryani", "Mutton Biryani",
         "Ice Cream", "Noodles", "Manchooriya", "Orange juice",
         "Apple Juice", "Pineapple juice", "Banana juice"]


def start_window(cv, classifier):
    """Start the initial window."""
    root1 = Tk()
    root1.title("Restaurant Review Analysis System / Welcome Page")

    label = Label(root1, text="RESTAURANT REVIEW ANALYSIS SYSTEM", bd=2,
                  font=('Arial', 47, 'bold', 'underline'))

    ques = Label(root1, text="Are you a Customer or Owner?")
    cust = Button(root1, text="Customer", font=('Arial', 20), padx=80, pady=20,
                  command=lambda: take_review(cv, classifier, root1))
    owner = Button(root1, text="Owner", font=('Arial', 20), padx=100, pady=20,
                   command=lambda: login(root1, cv, classifier))

    root1.geometry("800x600")  # Set a default window size
    label.pack(pady=20)  # Pack with some padding
    ques.pack(pady=20)
    cust.pack(pady=10)
    owner.pack(pady=10)
    root1.mainloop()


def take_review(cv, classifier, root1):
    """Display the review submission window."""
    root1.withdraw()  # Hide the main window
    root2 = Toplevel()
    root2.title("Restaurant Review Analysis System - Give Review")

    label = Label(root2, text="RESTAURANT REVIEW ANALYSIS SYSTEM", bd=2,
                  font=('Arial', 47, 'bold', 'underline'))

    req1 = Label(root2, text="Select the item(s) you have taken:")

    global variables
    variables = []

    for i in range(len(foods)):
        var = IntVar()
        chk = Checkbutton(root2, text=foods[i], variable=var)
        chk.pack(anchor=W)  # Use pack for simpler layout
        variables.append(var)

    rev_tf = Entry(root2, width=125, borderwidth=5)
    submit_review = Button(root2, text="Submit Review", font=('Arial', 20), padx=100, pady=20,
                           command=lambda: estimate(rev_tf.get(), cv, classifier, root2, root1))

    label.pack(pady=20)  # Pack with padding
    req1.pack(pady=10)  # Pack with padding
    rev_tf.pack(pady=20)
    submit_review.pack(pady=10)  # Ensure the button is packed


def estimate(review_text, cv, classifier, root2, root1):
    """Estimate review sentiment and update database."""
    print("Estimating review...")  # Debugging print statement
    print("Review text:", review_text)  # Print the review text

    from nltk.stem import PorterStemmer
    from nltk.corpus import stopwords
    import re

    # Review processing
    review = re.sub('[^a-zA-Z]', ' ', review_text).lower().split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    review = ' '.join([ps.stem(word) for word in review if word not in all_stopwords])

    # Predict sentiment
    X = cv.transform([review]).toarray()
    res = classifier.predict(X)
    print("Prediction result:", res)  # Debugging print statement

    # Get selected foods
    selected_foods = [foods[i] for i in range(len(foods)) if variables[i].get() == 1]
    print("Selected foods:", selected_foods)  # Debugging print statement

    # Update food data in the database
    update_food_data(selected_foods, res, cv, review)

    # Close the review window and show success message
    root2.destroy()
    root1.deiconify()  # Show the main window again
    display_data()  # Optionally, display updated data


def login(root1, cv, classifier):
    """Function for owner login."""
    root1.withdraw()  # Hide the main window
    root2 = Toplevel()
    root2.title("Owner Login")

    Label(root2, text="Owner Login", font=('Arial', 24)).pack(pady=20)

    # Username entry
    username_label = Label(root2, text="Username")
    username_label.pack()
    username_entry = Entry(root2)
    username_entry.pack(pady=10)

    # Password entry
    password_label = Label(root2, text="Password")
    password_label.pack()
    password_entry = Entry(root2, show='*')
    password_entry.pack(pady=10)

    # Submit button
    submit_button = Button(root2, text="Login",
                           command=lambda: check_login(username_entry.get(), password_entry.get(), root2, root1, cv,
                                                       classifier))
    submit_button.pack(pady=20)


def check_login(username, password, root2, root1, cv, classifier):
    """Check the login credentials."""
    # Replace with actual username and password validation
    if username == "owner" and password == "password":  # Replace with actual credentials
        print("Login successful!")  # Debugging print statement
        root2.destroy()  # Close login window
        # Directly show the dashboard or owner-specific functionality
        show_dashboard(root1, cv, classifier)
    else:
        print("Login failed!")  # Debugging print statement
        error_label = Label(root2, text="Invalid Credentials!", fg="red")
        error_label.pack()


def show_dashboard(root1, cv, classifier):
    """Display the owner dashboard."""
    # Here you can add code to show the dashboard for the owner
    # For demonstration, we'll just show a simple message
    dashboard_window = Toplevel(root1)
    dashboard_window.title("Owner Dashboard")

    Label(dashboard_window, text="Welcome to the Owner Dashboard!", font=('Arial', 24)).pack(pady=20)

    # You can add additional functionalities like displaying food items, statistics, etc.
    display_data()  # Call the function to display data for the owner
    root1.deiconify()  # Show the main window again

