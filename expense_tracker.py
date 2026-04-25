import sqlite3

# Connect to database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount INTEGER,
    category TEXT,
    date TEXT,
    description TEXT
)
""")

# Add expense
def add_expense():
    amount = int(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    desc = input("Enter description: ")

    cursor.execute("INSERT INTO expenses (amount, category, date, description) VALUES (?, ?, ?, ?)",
                   (amount, category, date, desc))
    conn.commit()
    print("Expense added!")

# View expenses
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Total expense
def total_expense():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    print("Total Expense:", total)

# Menu
while True:
    print("\n1.Add 2.View 3.Total 4.Exit")
    choice = input("Choose: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_expense()
    elif choice == '4':
        break