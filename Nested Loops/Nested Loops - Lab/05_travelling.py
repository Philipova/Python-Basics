destination = input()
# Докато дестинацията не е End
while destination != "End":
    needed_money = float(input())
    current_money = 0
    # Докато текущите пари са по-малко от нужните за пътуването
    while current_money < needed_money:
        saved_money = float(input())
        current_money += saved_money
    print(f"Going to {destination}!")
    destination = input()
          
