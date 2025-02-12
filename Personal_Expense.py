# Step 1: Add expense

from datetime import datetime

expenses = []

def add_expense():
    while True:
        date_input = input('Enter date of expense (YYYY-MM-DD): ')
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d").date()
            break
        except ValueError:
            print('Invalid date format. Please enter again.')

    category = input('Enter the expense category: ')

    while True:
        try:
            amount = float(input('Enter amount spent $: '))
            break  # Exit loop once valid input is received
        except ValueError:
            print('Invalid input. Please enter a number.')

    description = input('Enter description: ')

    expense = {
        'date': date.strftime("%Y-%m-%d"),
        'category': category,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)
    print('Expense added!')

# Debug statement to check function existence
print("Calling add_expense() now...")
add_expense()

# Step 2: View expense

def view_expense():
    if not expenses:
        print('No expenses to view')
        return
    
    for expense in expenses:
        if 'date' not in expense or 'category' not in expense or 'amount' not in expense or 'description' not in expense:
            print(f'Missing expense')
            continue
            
    print(f"\nDate: {expense['date']}")
    print(f"\nCategory: {expense['category']}")
    print(f"\nAmount: {expense['amount']}")
    print(f"\nDescription: {expense['description']}")

# Step 3: Set and track the budget:
def budget_tracker():
    monthly_budget = float(input('Enter your budget: '))
    total = sum(expense['amount'] for expense in expenses)

    if total > monthly_budget:
        print('You have exceeded your budget!')
    else:
        remaining_balance = monthly_budget - total
        print(f"You have ${remaining_balance:.2f} left for the month.")
        
# Step 4: Save and load expenses
import csv

def save_expenses():
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
        for expense in expenses:
            writer.writerow([expense['date'],
                            expense['category'], 
                            expense['amount'],
                            expense['description']
                            ])

def load_expenses():
    global expenses
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            expenses = []
            for row in reader:
                if len(row) == 4:
                    expense = {
                        'date': row[0],
                        'category': row[1],
                        'amount': float(row[2]),
                        'description': row[3]
                    }
                    expenses.append(expense)
        print("Expenses loaded successfully!")
    except FileNotFoundError:
        print("No existing expense file found. Starting with an empty list.")
        expenses = []
    except Exception as e:
        print(f"An error occurred while loading expenses: {e}")
        expenses = []
        
#Step 5: Create an interactive menu
def display_menu():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Track Budget")
    print("4. Save Expenses")
    print("5. Load Expenses")
    print("6. Exit")

def main():
    load_expenses()
    while True:
        display_menu()
        enter_number = input("Enter your number (1-5): ")

        if enter_number == '1':
            add_expense()
        elif enter_number == '2':
            view_expense()
        elif enter_number == '3':
            budget_tracker()
        elif enter_number == '4':
            save_expenses()
        elif enter_number == '5':
            load_expenses()
        elif enter_number == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()