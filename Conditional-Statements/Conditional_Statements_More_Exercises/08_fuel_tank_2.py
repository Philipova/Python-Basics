fuel_type = input()  # read the fuel type from the user
fuel_amount = float(input())  # read the amount of fuel from the user and convert it to a float
has_card = input()  # read whether the user has a discount card

# set the fuel prices
gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

# set the discount amounts
gasoline_discount = 0.18
diesel_discount = 0.12
gas_discount = 0.08

# calculate the cost of fuel based on the fuel type and the price per liter
if fuel_type == "Gasoline":
    fuel_cost = fuel_amount * gasoline_price
    if has_card == "Yes":
        fuel_cost -= fuel_amount * gasoline_discount
elif fuel_type == "Diesel":
    fuel_cost = fuel_amount * diesel_price
    if has_card == "Yes":
        fuel_cost -= fuel_amount * diesel_discount
elif fuel_type == "Gas":
    fuel_cost = fuel_amount * gas_price
    if has_card == "Yes":
        fuel_cost -= fuel_amount * gas_discount
else:
    print("Invalid fuel type")

# calculate the discount based on the amount of fuel purchased
if fuel_amount >= 20 and fuel_amount <= 25:
    fuel_cost *= 0.92  # 8% discount
elif fuel_amount > 25:
    fuel_cost *= 0.9  # 10% discount

# print the final cost of fuel
print("{:.2f} lv.".format(fuel_cost))
