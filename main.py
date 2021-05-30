from database import *

print("""

      WELCOME

      [1] -> Show Books
      [2] -> Search Book
      [3] -> Add Book
      [4] -> Delete Books
      [5] -> Update Pressure
      [q] -> Exit
""")
lib = Library()

while True:
    option = input("Select One: ")
    if option == "1":
        lib.show_books()
    elif option == "2":
        title = input("Book Name : ")
        lib.inquire_book(title)
    elif option == "3":
        title = input("Book Name : ")
        author = input("Author Name : ")
        publisher = input("Publisher : ")
        type_of_book = input("Type : ")
        press = input("Book Press : ")
        book = Book(title, author, publisher, type_of_book, press)
        lib.add_book(book)
    elif option == "4":
        title = input("Book Name : ")
        lib.delete_book(title)
    elif option == "5":
        title = input("Book Name : ")
        lib.set_press(title)
    elif option == "q":
        exit()
    else:
        print("error")
