budget = float(input())
category = input()
group_size = int(input())

ticket_price_vip = 499.99
ticket_price_normal = 249.99

if group_size <= 4:
    transport_percentage = 0.75
elif group_size <= 9:
    transport_percentage = 0.60
elif group_size <= 24:
    transport_percentage = 0.50
elif group_size <= 49:
    transport_percentage = 0.40
else:
    transport_percentage = 0.25

if category == "VIP":
    ticket_price = ticket_price_vip
else:
    ticket_price = ticket_price_normal

total_ticket_price = group_size * ticket_price
transport_cost = transport_percentage * budget

if budget >= total_ticket_price + transport_cost:
    remaining_money = budget - (total_ticket_price + transport_cost)
    print(f"Yes! You have {remaining_money:.2f} leva left.")
else:
    needed_money = (total_ticket_price + transport_cost) - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")
