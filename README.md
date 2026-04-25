# Expense Tracker using Python and SQL (SQLite)

## Description
This project is a simple Expense Tracker application developed using Python and SQLite. It allows users to record daily expenses, view stored data, and calculate total spending using SQL queries.

## Features
- Add expenses with amount, category, date, and description
- View all stored records
- Calculate total expenses
- Filter expenses by category
- Exclude income while calculating total expenses

## Technologies Used
- Python
- SQLite (SQL)

## Database Details
Table: expenses  
Columns:
- id (Primary Key)
- amount
- category
- date
- description

## Sample SQL Queries
```sql
SELECT * FROM expenses;
SELECT SUM(amount) FROM expenses;
SELECT * FROM expenses WHERE category = 'food';
SELECT * FROM expenses WHERE category != 'income';
SELECT SUM(amount) FROM expenses WHERE category != 'income';

