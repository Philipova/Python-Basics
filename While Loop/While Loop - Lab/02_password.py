username = input()
password = input()
entry = input()

while entry != password:
    entry = input()
    continue

if entry == password:
    print(f"Welcome {username}!")
  
