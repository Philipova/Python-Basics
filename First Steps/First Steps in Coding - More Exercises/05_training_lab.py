import math

# read the dimensions of the classroom
w = float(input())
h = float(input())

# calculate the available space in the classroom
door_width = 1.6 # in meters
chair_width = 1.2 # in meters
corridor_width = max(1.0, (w - door_width - chair_width) / 2)
desk_width = 0.7 # in meters
desk_length = 1.2 # in meters
desk_space = 0.8 # in meters
rows = math.floor(((h * 100) - 100) /70)
seats_per_row = math.floor((w * 100) / 120)

# calculate the total number of workstations
total_seats = rows * seats_per_row - 3

# print the result
print(total_seats)
