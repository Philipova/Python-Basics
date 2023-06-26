# Define the prices for each fruit for weekdays and weekends
weekday_prices = {"banana": 2.50, "apple": 1.20, "orange": 0.85, "grapefruit": 1.45, "kiwi": 2.70, "pineapple": 5.50, "grapes": 3.85}
weekend_prices = {"banana": 2.70, "apple": 1.25, "orange": 0.90, "grapefruit": 1.60, "kiwi": 3.00, "pineapple": 5.60, "grapes": 4.20}

# Read input from the user
fruit = input()
day_of_week = input()
quantity = float(input())

# Calculate the price based on the day of the week
if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    prices = weekday_prices
elif day_of_week in ["Saturday", "Sunday"]:
    prices = weekend_prices
else:
    print("error")
    exit()

# Calculate the total price
if fruit in prices:
    price_per_unit = prices[fruit]
    total_price = price_per_unit * quantity
    print("{:.2f}".format(total_price))
else:
    print("error")
