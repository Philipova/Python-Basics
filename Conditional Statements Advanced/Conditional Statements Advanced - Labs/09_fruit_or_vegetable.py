# Define the lists of fruits and vegetables
fruits = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetables = ['tomato', 'cucumber', 'pepper', 'carrot']

# Read the product name from the user
product_name = input()

# Check if the product is a fruit
if product_name in fruits:
    print('fruit')
# Check if the product is a vegetable
elif product_name in vegetables:
    print('vegetable')
# If it's neither a fruit nor a vegetable, it's unknown
else:
    print('unknown')
