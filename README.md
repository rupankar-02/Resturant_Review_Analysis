### Restaurant Review Analysis System

The **Restaurant Review Analysis System** is a desktop-based application built using Python's Tkinter library for the graphical user interface (GUI). It allows restaurant owners and customers to interact with the system in two distinct roles:

- **Customer**: Users can submit reviews for the food items they have consumed. The system uses Natural Language Processing (NLP) techniques to analyze the sentiment of the submitted review, classify it as positive or negative, and update the restaurant’s internal data accordingly.
  
- **Owner**: The restaurant owner can log in to access a dashboard that displays an analysis of the customer reviews, showing overall sentiment for different food items. This helps the owner keep track of customer satisfaction and make informed business decisions.

### Key Features:
- **Customer Review Submission**: Customers can select multiple food items, submit a review, and the system will analyze and classify the sentiment using machine learning models (like a sentiment classifier).
- **Owner Dashboard**: Owners can log in using a secure login page and view aggregated data on customer feedback, allowing them to evaluate the performance of their menu items.
- **Sentiment Analysis**: The app preprocesses customer reviews by removing stopwords and stemming words. A machine learning model then predicts the sentiment of the review.
- **Database Management**: Food item data is stored in a SQLite database, tracking the number of customers, positive reviews, and overall sentiment for each dish.

This project demonstrates a practical application of NLP and machine learning in the restaurant industry, allowing restaurant owners to better understand customer feedback through an easy-to-use interface.
