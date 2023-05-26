# read input values from the console
mackerel_price = float(input())
sprat_price = float(input())
bonito_weight = float(input())
saffron_weight = float(input())
mussels_weight = int(input())

# calculate the prices of bonito and saffron
bonito_price = 1.6 * mackerel_price
saffron_price = 1.8 * sprat_price

# calculate the total cost of the purchase
total_cost = (bonito_price * bonito_weight) + (saffron_price * saffron_weight) + (7.5 * mussels_weight)

# print the total cost formatted to two decimal places
print(f"{total_cost:.2f}")
