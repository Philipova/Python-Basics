budget = float(input())
season = input()

if budget <= 100:
    car_type = "Cabrio" if season == "Summer" else "Jeep"
    price = budget * 0.35 if season == "Summer" else budget * 0.65
    car_class = "Economy class"
elif budget <= 500:
    car_type = "Cabrio" if season == "Summer" else "Jeep"
    price = budget * 0.45 if season == "Summer" else budget * 0.8
    car_class = "Compact class"
else:
    car_type = "Jeep"
    price = budget * 0.9
    car_class = "Luxury class"

price_formatted = "{:.2f}".format(price)

print(car_class)
print(f"{car_type} - {price_formatted}")
