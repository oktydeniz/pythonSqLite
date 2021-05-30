import sqlite3


class Book:
    def __init__(self, title, author, publisher, type_of_book, printing):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.type_of_book = type_of_book
        self.printing = printing

    def __str__(self):
        return f" Title : {self.title} Author :  {self.author} Type of Book :{self.type_of_book}" \
               f" Printing : {self.printing} Publisher : {self.publisher}"


class Library(object):
    def __init__(self):
        self.open_sql()

    def open_sql(self):
        self.connection = sqlite3.connect("library.db")
        self.cursor = self.connection.cursor()
        query = "CREATE TABLE IF NOT EXISTS Books(title TEXT,author TEXT,publisher TEXT, type_of_book TEXT," \
                "printing INT ) "
        self.cursor.execute(query)
        self.connection.commit()

    def close_sql(self):
        self.connection.close()

    def show_books(self):
        query = "SELECT * FROM Books "
        self.cursor.execute(query)
        books_list = self.cursor.fetchall()
        if len(books_list) == 0:
            print("DB is empty")
        else:
            for i in books_list:
                book = Book(i[0], i[1], i[2], i[3], i[4])
                print(book)

    def inquire_book(self, title):
        query = "SELECT * FROM Books where title=?"
        self.cursor.execute(query, (title,))
        books = self.cursor.fetchall()
        if len(books) == 0:
            print("not found")
        else:
            book = Book(books[0][0], books[0][1], books[0][2], books[0][3], books[0][4])
            print(book)

    def add_book(self, book):
        query = "INSERT INTO Books Values(?,?,?,?,?)"
        self.cursor.execute(query, (book.title, book.author, book.publisher, book.type_of_book, book.printing))
        self.connection.commit()

    def delete_book(self, title):
        query = "DELETE FROM Books where title=?"
        self.cursor.execute(query, (title,))
        self.connection.commit()

    def set_press(self, title):
        query = "SELECT * FROM Books WHERE title=?"
        self.cursor.execute(query, (title,))
        books = self.cursor.fetchall()
        if len(books) != 0:
            press = books[0][4]
            press += 1
            query2 = "UPDATE Books SET printing =? WHERE title=?"
            self.cursor.execute(query2, (press, title))
            self.connection.commit()
        else:
            print("not found")
