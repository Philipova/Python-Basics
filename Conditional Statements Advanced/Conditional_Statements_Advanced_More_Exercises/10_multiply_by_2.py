while True:
    number = float(input())

    if number < 0:
        print("Negative number!")
        break

    if number > 0:
        result = number * 2
        print("Result: {:.2f}".format(result))
