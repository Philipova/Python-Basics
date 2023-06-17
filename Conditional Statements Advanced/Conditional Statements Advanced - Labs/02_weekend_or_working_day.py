# Importing necessary library
import calendar

# Taking input from user
day = input()

# Converting day to title case
day = day.title()

# Checking if the input is a valid day of the week
if day in calendar.day_name:

    # Checking if the day is a working day or a weekend
    if day in calendar.day_name[0:5]:
        print("Working day")
    else:
        print("Weekend")
else:
    print("Error")
