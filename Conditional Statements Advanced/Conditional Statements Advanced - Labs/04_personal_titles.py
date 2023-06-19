ages = float(input())
gender = input()
if gender == "m":
    if ages >= 16:
        print("Mr.")
    else: # elif ages < 16
        print("Master")
elif gender == "f": #else
    if ages >= 16:
        print("Ms.")
    else:  # elif ages < 16
        print("Miss")
      
