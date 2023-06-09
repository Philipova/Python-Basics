def calculate_vacation(budget, season):
    if budget <= 1000:
        accommodation = "Camp"
        if season == "Summer":
            location = "Alaska"
            price = budget * 0.65
        else:
            location = "Morocco"
            price = budget * 0.45
    elif budget <= 3000:
        accommodation = "Hut"
        if season == "Summer":
            location = "Alaska"
            price = budget * 0.8
        else:
            location = "Morocco"
            price = budget * 0.6
    else:
        accommodation = "Hotel"
        if season == "Summer":
            location = "Alaska"
        else:
            location = "Morocco"
        price = budget * 0.9

    return f"{location} - {accommodation} - {price:.2f}"


# Read input from the user
budget = float(input())
season = input()

# Calculate and print the vacation details
result = calculate_vacation(budget, season)
print(result)
