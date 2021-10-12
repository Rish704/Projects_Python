# add check for returning
class library:
    def __init__(self, booklist):
        self.books = booklist

    def available(self):
        print("Available books are: ")
        for books in self.books:
            print(" " + books)

    def borrow(self, bookname):
        if bookname in self.books:
            print(f"You have been issued the book {bookname}")
            self.books.remove(bookname)
        else:
            print("The book is not available")

    def returnbook(self, bookname):
        self.books.append(bookname)
        print(f"{bookname} has been returned")


class students:
    def request(self):
        self.book = input("The book to be borrowed: ")
        return self.book

    def returnbook(self):
        self.book = input("The book to be returned: ")
        return self.book


if __name__ == "__main__":
    centralLibrary = library(["Algorithms", "Data Structures", "Good sites", "R.D. Sharma"])
    s = students()
    print("--------Welcome to the central library---------")
    while True:
        welcome = '''
        Enter your choice below
        1. Display all books
        2. Request book
        3. Add/Return book
        4. Exit the portal'''
        print(welcome)
        a = int(input("Input: "))
        if a == 1:
            centralLibrary.available()
        elif a == 2:
            centralLibrary.borrow(s.request())
        elif a == 3:
            centralLibrary.returnbook(s.returnbook())
        elif a == 4:
            print("Thanks for choosing central library. Visit again!!")
            exit()
        else:
            print("Invalid choice")