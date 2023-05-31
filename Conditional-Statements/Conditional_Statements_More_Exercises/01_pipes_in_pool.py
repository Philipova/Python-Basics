# Read input from the user
V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

# Calculate how much water each pipe contributes in H hours
water_from_pipe_1 = P1 * H
water_from_pipe_2 = P2 * H

# Calculate the total amount of water in the pool
total_water = water_from_pipe_1 + water_from_pipe_2

# Check if the pool has overflowed
if total_water > V:
    excess_water = total_water - V
    print(f"For {H} hours the pool overflows with {excess_water} liters.")
else:
    # Calculate the percentage of the pool that is full and how much each pipe contributed
    percent_full = (total_water / V) * 100
    percent_from_pipe_1 = (water_from_pipe_1 / total_water) * 100
    percent_from_pipe_2 = (water_from_pipe_2 / total_water) * 100

    # Print the results
    print(f"The pool is {percent_full:.2f}% full. Pipe 1: {percent_from_pipe_1:.2f}%. Pipe 2: {percent_from_pipe_2:.2f}%.")
