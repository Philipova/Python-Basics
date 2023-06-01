days_off = int(input())

working_days = 365 - days_off
play_time = working_days * 63 + days_off * 127
norm = 30000

if play_time > norm:
    diff = play_time - norm
    hours = diff // 60
    minutes = diff % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    diff = norm - play_time
    hours = diff // 60
    minutes = diff % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
    
