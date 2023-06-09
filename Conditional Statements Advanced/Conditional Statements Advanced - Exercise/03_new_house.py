def calculate_flower_cost(flower_type, num_flowers, budget):
    flower_prices = {
        "Roses": 5,
        "Dahlias": 3.80,
        "Tulips": 2.80,
        "Narcissus": 3,
        "Gladiolus": 2.50
    }

    discounts = {
        "Roses": (80, 0.10),
        "Dahlias": (90, 0.15),
        "Tulips": (80, 0.15)
    }

    increases = {
        "Narcissus": 0.15,
        "Gladiolus": 0.20
    }

    price_per_flower = flower_prices[flower_type]
    total_cost = num_flowers * price_per_flower

    if flower_type in discounts:
        threshold, discount_percentage = discounts[flower_type]
        if num_flowers > threshold:
            total_cost -= total_cost * discount_percentage

    if flower_type in increases:
        threshold = 120 if flower_type == "Narcissus" else 80
        increase_percentage = increases[flower_type]
        if num_flowers < threshold:
            total_cost += total_cost * increase_percentage

    remaining_amount = budget - total_cost

    if remaining_amount >= 0:
        output = f"Hey, you have a great garden with {num_flowers} {flower_type} and {remaining_amount:.2f} leva left."
    else:
        necessary_amount = abs(remaining_amount)
        output = f"Not enough money, you need {necessary_amount:.2f} leva more."

    return output


flower_type = input()
num_flowers = int(input())
budget = int(input())

result = calculate_flower_cost(flower_type, num_flowers, budget)
print(result)
