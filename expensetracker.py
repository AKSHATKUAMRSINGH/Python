# Initialize an empty dictionary to store expenses
expenses = {}

# Function to add an expense to the expense tracker
def add_expense(date, item, cost, category):
    if date not in expenses:
        expenses[date] = []
    expenses[date].append((item, cost, category))

# Function to calculate the total expenses for a given date
def calculate_total_expenses(date):
    total = sum(float(cost) for _, cost, _ in expenses[date])
    return total

# Function to view all expenses for a specific date
def view_expenses(date):
    if date in expenses:
        print(f"Expenses for {date}:")
        for item, cost, category in expenses[date]:
            print(f"{item}: ${cost} ({category})")
        total = calculate_total_expenses(date)
        print(f"Total expenses for {date}: ${total:.2f}")
    else:
        print(f"No expenses recorded for {date}.")

# Function to set and display the budget
def set_budget():
    budget = float(input("Enter your monthly budget: $"))
    return budget

def view_budget(budget):
    print(f"Monthly budget: ${budget:.2f}")

# Function to check if expenses have exceeded the budget
def check_budget(budget, date):
    total_expenses = calculate_total_expenses(date)
    if total_expenses > budget:
        print(f"You have exceeded your budget for {date}.")
    else:
        print(f"You are within budget for {date}.")

# Function to save expenses to a text file
def save_expenses():
    with open("expenses.txt", "w") as file:
        for date, items in expenses.items():
            for item, cost, category in items:
                file.write(f"{date},{item},{cost},{category}\n")

# Function to load expenses from a text file
def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                date, item, cost, category = line.strip().split(",")
                cost = float(cost)
                if date not in expenses:
                    expenses[date] = []
                expenses[date].append((item, cost, category))
    except FileNotFoundError:
        # If the file doesn't exist, expenses will be empty initially
        pass

# Function to edit an expense for a specific date
def edit_expense(date, item_to_edit, new_item, new_cost, new_category):
    if date in expenses:
        for i, (item, cost, category) in enumerate(expenses[date]):
            if item == item_to_edit:
                expenses[date][i] = (new_item, new_cost, new_category)
                print("Expense edited successfully.")
                save_expenses()
                return
        print("Expense not found.")
    else:
        print("No expenses recorded for this date.")

# Function to delete an expense for a specific date
def delete_expense(date, item_to_delete):
    if date in expenses:
        for item, cost, category in expenses[date]:
            if item == item_to_delete:
                expenses[date] = [(i, c, cat) for i, c, cat in expenses[date] if i != item_to_delete]
                if not expenses[date]:
                    del expenses[date]  # Remove the date entry if no expenses remain
                print("Expense deleted successfully.")
                save_expenses()
                return
        print("Expense not found.")
    else:
        print("No expenses recorded for this date.")

# Function to generate and display a monthly report
def generate_monthly_report():
    report = {}
    for date in expenses.keys():
        year, month, _ = date.split("-")
        month_year = f"{year}-{month}"
        if month_year not in report:
            report[month_year] = 0
        report[month_year] += calculate_total_expenses(date)

    print("\nMonthly Expense Report:")
    print("Month-Year\tTotal Expenses")
    print("-" * 40)
    for month_year, total in report.items():
        print(f"{month_year}\t${total:.2f}")

# Function to generate and display a summary of expenses by category
def generate_category_summary(date):
    categories = {}
    if date in expenses:
        for _, cost, category in expenses[date]:
            if category not in categories:
                categories[category] = 0
            categories[category] += cost
        print("\nExpense Summary by Category for", date)
        print("Category\tTotal Expenses")
        print("-" * 40)
        for category, total in categories.items():
            print(f"{category}\t${total:.2f}")
    else:
        print(f"No expenses recorded for {date}.")

# Main program loop
def main():
    # Load expenses data from the file when the program starts
    load_expenses()

    budget = set_budget()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses for a Date")
        print("3. Set/View Budget")
        print("4. Check Budget for a Date")
        print("5. Edit Expense for a Date")
        print("6. Delete Expense for a Date")
        print("7. Generate Monthly Report")
        print("8. Generate Category Summary for a Date")
        print("9. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            item = input("Enter the item: ")
            cost = float(input("Enter the cost: $"))
            category = input("Enter the category: ")
            add_expense(date, item, cost, category)
            print("Expense added successfully.")
            save_expenses()

        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            view_expenses(date)

        elif choice == "3":
            view_budget(budget)

        elif choice == "4":
            date = input("Enter the date (YYYY-MM-DD): ")
            check_budget(budget, date)

        elif choice == "5":
            date = input("Enter the date (YYYY-MM-DD): ")
            item_to_edit = input("Enter the item to edit: ")
            new_item = input("Enter the new item: ")
            new_cost = float(input("Enter the new cost: $"))
            new_category = input("Enter the new category: ")
            edit_expense(date, item_to_edit, new_item, new_cost, new_category)

        elif choice == "6":
            date = input("Enter the date (YYYY-MM-DD): ")
            item_to_delete = input("Enter the item to delete: ")
            delete_expense(date, item_to_delete)

        elif choice == "7":
            generate_monthly_report()

        elif choice == "8":
            date = input("Enter the date (YYYY-MM-DD): ")
            generate_category_summary(date)

        elif choice == "9":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
