from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in "YYYY-MM-DD HH:MM:SS" format
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days_to_add):
    """
    Calculates and displays the future date after adding specified days
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate a future date
    while True:
        try:
            days = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    future_date = calculate_future_date(days)

if __name__ == "__main__":
    main()
