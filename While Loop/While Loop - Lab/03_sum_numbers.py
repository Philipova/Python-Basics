def read_numbers():
    original_number = int(input())
    total_sum = 0
    
    while total_sum < original_number:
        num = int(input())
        total_sum += num
    
    print(total_sum)


read_numbers()
