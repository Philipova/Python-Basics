n = int(input())  # read the number of kilometers
time_of_day = input()  # read the time of day

# calculate the cost for each transport option
taxi_cost = 0.7 + (0.79 if time_of_day == 'day' else 0.9) * n
bus_cost = 0.09 * n if n >= 20 else float('inf')
train_cost = 0.06 * n if n >= 100 else float('inf')

# determine the cheapest option
cheapest_cost = min(taxi_cost, bus_cost, train_cost)

# print the result
print('{:.2f}'.format(cheapest_cost))
