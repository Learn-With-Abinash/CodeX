import datetime


def main():
    # Ask for user inputs
    try:
        monthly_income = float(input("Enter your total monthly income: "))
    except ValueError:
        print("Invalid monthly income.")
        return

    try:
        target_amount = float(input("Enter your target saving amount: "))
    except ValueError:
        print("Invalid target amount.")
        return

    item = input("What do you want to buy? ")

    date_str = input("When do you plan to buy it? (YYYY-MM-DD): ")
    try:
        target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    today = datetime.date.today()
    if target_date <= today:
        print("The target date must be in the future.")
        return

    delta_days = (target_date - today).days

    # Calculate required savings
    per_day = target_amount / delta_days
    per_week = per_day * 7
    per_month = per_day * 30  # approximate

    print(f"\nTo buy {item} by {target_date}:")
    print(f"You need to save approximately ${per_day:.2f} per day.")
    print(f"That's about ${per_week:.2f} per week.")
    print(f"Or roughly ${per_month:.2f} per month.")


if __name__ == "__main__":
    main()
