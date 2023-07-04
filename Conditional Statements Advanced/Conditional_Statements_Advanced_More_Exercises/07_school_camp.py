def calculate_price(season, group, num_students, num_nights):
    # Define the prices and sports based on the season and group
    if season == "Winter":
        if group == "boys" or group == "girls":
            price_per_night = 9.60
            sport = "Judo" if group == "boys" else "Gymnastics"
        else:  # mixed group
            price_per_night = 10
            sport = "Ski"
    elif season == "Spring":
        if group == "boys" or group == "girls":
            price_per_night = 7.20
            sport = "Tennis" if group == "boys" else "Athletics"
        else:  # mixed group
            price_per_night = 9.50
            sport = "Cycling"
    elif season == "Summer":
        if group == "boys" or group == "girls":
            price_per_night = 15
            sport = "Football" if group == "boys" else "Volleyball"
        else:  # mixed group
            price_per_night = 20
            sport = "Swimming"
    else:
        return "Invalid season"

    # Calculate the total price before discount
    total_price = price_per_night * num_nights * num_students

    # Apply the discount based on the number of students
    if num_students >= 50:
        discount = 0.5
    elif num_students >= 20:
        discount = 0.15
    elif num_students >= 10:
        discount = 0.05
    else:
        discount = 0

    # Calculate the final price after discount
    final_price = total_price - (total_price * discount)

    return f"{sport} {final_price:.2f} lv."


# Read input from the user
season = input()
group = input()
num_students = int(input())
num_nights = int(input())

# Calculate and print the result
result = calculate_price(season, group, num_students, num_nights)
print(result)
