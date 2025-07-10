print("Finance Tracking")

try:
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your monthly expenses: "))

    savings = monthly_income - monthly_expenses

    print(f"\nYour savings this month are {savings}")

    if savings > 10000:
        status = "Saving Well"

    elif 5000 <= savings <= 9999:
        status = "Average"

    else:
        status = "Try to Save"

    print(f"Status {status}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")
