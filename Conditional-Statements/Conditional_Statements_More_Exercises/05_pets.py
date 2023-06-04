import math

days = int(input())
food_left = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input()) / 1000 # convert grams to kilograms

total_food_per_day = dog_food_per_day + cat_food_per_day + turtle_food_per_day
total_food_needed = math.ceil(days * total_food_per_day)

if total_food_needed <= food_left:
    print(f"{int(food_left - total_food_needed)} kilos of food left.")
else:
    print(f"{(int(total_food_needed - food_left))} more kilos of food are needed.")
