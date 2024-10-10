# app.py
from preprocessing import preprocess_data
from database import init_db_data
from interface import start_window


def main():
    # Preprocess data and train the Naive Bayes model
    cv, classifier = preprocess_data()

    # Initialize database with food items
    init_db_data()

    # Start the GUI
    start_window(cv, classifier)


if __name__ == "__main__":
    main()
