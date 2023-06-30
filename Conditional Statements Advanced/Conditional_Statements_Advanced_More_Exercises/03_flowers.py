def calculate_bouquet_price(chrysanthemums, roses, tulips, season, is_holiday):
    prices = {
        "Spring": {"chrysanthemums": 2.00, "roses": 4.10, "tulips": 2.50},
        "Summer": {"chrysanthemums": 2.00, "roses": 4.10, "tulips": 2.50},
        "Autumn": {"chrysanthemums": 3.75, "roses": 4.50, "tulips": 4.15},
        "Winter": {"chrysanthemums": 3.75, "roses": 4.50, "tulips": 4.15}
    }

    bouquet_price = 0
    bouquet_price += chrysanthemums * prices[season]["chrysanthemums"]
    bouquet_price += roses * prices[season]["roses"]
    bouquet_price += tulips * prices[season]["tulips"]

    if is_holiday == "Y":
        bouquet_price *= 1.15

    if season in ["Spring", "Summer"] and tulips > 7:
        bouquet_price *= 0.95

    if season == "Winter" and roses >= 10:
        bouquet_price *= 0.9

    total_flowers = chrysanthemums + roses + tulips
    if total_flowers > 20:
        bouquet_price *= 0.8

    bouquet_price += 2  # adding the price for arranging the bouquet

    return bouquet_price


# Reading input from the user
chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
is_holiday = input()

# Calculating the bouquet price
bouquet_price = calculate_bouquet_price(chrysanthemums, roses, tulips, season, is_holiday)

# Printing the result
print(f"{bouquet_price:.2f}")
