import math

# Read inputs from the user
area = int(input())
grapes_per_sqm = float(input())
required_wine = int(input())
num_workers = int(input())

# Calculate the total amount of grapes and wine produced
total_grapes = area * grapes_per_sqm
wine_production = 0.4 * total_grapes / 2.5

# Check if enough wine is produced
if wine_production < required_wine:
    insufficient_wine = math.floor(required_wine - wine_production)
    print(f"It will be a tough winter! More {insufficient_wine} liters wine needed.")
else:
    total_wine = math.floor(wine_production)
    print(f"Good harvest this year! Total wine: {total_wine} liters.")

    # Calculate the remaining wine and wine per worker
    remaining_wine = math.ceil(total_wine - required_wine)
    wine_per_worker = math.ceil(remaining_wine / num_workers)
    print(f"{remaining_wine} liters left -> {wine_per_worker} liters per person.")
