required_book = input()

books = input()
num_books = 0
book_found = False
while books != "No More Books":
    if books == required_book:
        book_found = True
        break

    num_books += 1
    books = input()


if book_found:
    print(f"You checked {num_books} books and found it.")

else:
    print("The book you search is not here!")
    print(f"You checked {num_books} books.")
  
