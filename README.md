Expense Tracker using Python and SQL (SQLite)

Features:
- Add expenses
- View records
- Calculate total expenses
- Exit

Technologies:
- Python
- SQLite (SQL)

Sample SQL Queries:
SELECT * FROM expenses;
SELECT SUM(amount) FROM expenses;
SELECT * FROM expenses WHERE category='food';
SELECT * FROM expenses WHERE category != 'income';
SELECT SUM(amount) FROM expenses WHERE category != 'income';
