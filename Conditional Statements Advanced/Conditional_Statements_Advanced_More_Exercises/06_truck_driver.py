season = input()
kilometers_per_month = float(input())

rate_per_km = 0.0

if season == "Spring" or season == "Autumn":
    if kilometers_per_month <= 5000:
        rate_per_km = 0.75
    elif 5000 < kilometers_per_month <= 10000:
        rate_per_km = 0.95
    elif 10000 < kilometers_per_month <= 20000:
        rate_per_km = 1.45
elif season == "Summer":
    if kilometers_per_month <= 5000:
        rate_per_km = 0.90
    elif 5000 < kilometers_per_month <= 10000:
        rate_per_km = 1.10
    elif 10000 < kilometers_per_month <= 20000:
        rate_per_km = 1.45
elif season == "Winter":
    if kilometers_per_month <= 5000:
        rate_per_km = 1.05
    elif 5000 < kilometers_per_month <= 10000:
        rate_per_km = 1.25
    elif 10000 < kilometers_per_month <= 20000:
        rate_per_km = 1.45

salary = kilometers_per_month * rate_per_km * 4  # Calculate salary for the entire season
salary_after_taxes = salary - (salary * 0.10)  # Deduct 10% for taxes

print(f'{salary_after_taxes:.2f}')
