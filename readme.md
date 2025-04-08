## Financial Transaction Processor Application
## Overview
This is a Flask-based web application designed to process financial transactions, apply VAT to goods and services, calculate the net balance after VAT, and compute compound interest on the final balance. It provides an easy interface for submitting transactions and viewing the results.

## Features
VAT Calculation: VAT (5%) is applied to goods and services transactions.

Credit transactions: VAT is subtracted from the amount.

Debit transactions: VAT is added to the amount.

Investment transactions: No VAT is applied.

Net Balance Calculation: The application computes the net balance after VAT adjustments.

Compound Interest: If the net balance is positive, the application computes the compound interest over the specified time period.

Category Breakdown: Provides a breakdown of the totals for each category (goods, services, investment) after VAT adjustments.

Error Handling: Handles edge cases such as negative values, invalid categories, and zero or negative years.

## Requirements
Python 3.x: Ensure you have Python 3.x installed.

Flask: Flask is used to run the application.

## Install Flask
To install Flask, you need to use pip. Run the following command in your terminal or command prompt:

bash
Copy
pip install Flask
Application Structure
The application consists of the following files:

app.py: This is the main backend file containing all the business logic to process transactions, apply VAT, calculate the net balance, and compute compound interest.

templates/index.html: The HTML template that contains the input form for entering transactions and other required data (years, interest rate, VAT rate).

static/: You can add static files such as CSS or JavaScript for styling and interactivity (optional).

## How to Run the Application
Step 1: Set Up the Flask Environment
Install Python 3.x: Download and install Python from python.org.

Create a Virtual Environment (Optional but Recommended):

bash
Copy
python -m venv venv
Activate the Virtual Environment:

## On Windows:

bash
Copy
.\venv\Scripts\activate
On macOS/Linux:

bash
Copy
source venv/bin/activate
Install Flask: After activating the virtual environment, run the following command:

bash
Copy
pip install Flask
Step 2: Run the Application
## Download or Copy the Code:

Save the backend code (app.py) and the frontend HTML form (templates/index.html) in your project directory.

Start the Flask Server:

Run the following command in your terminal or command prompt:

bash
Copy
python app.py
## Access the Application:

The application will be available at http://127.0.0.1:5000/ in your web browser.

Step 3: Submit Transactions and Get Results
Option 1: Frontend (HTML Form)
Open the application in your browser at http://127.0.0.1:5000/.

You’ll see a form where you can enter transaction data.

Transactions: Enter the list of transactions in JSON format (e.g., credit, debit, category, VAT).

Years: Enter the number of years for compound interest.

Interest Rate: Enter the interest rate (default is 5%).

VAT Rate: Enter the VAT rate (default is 5%).

Click Submit to process the transactions and get the results. The results will be displayed below the form.