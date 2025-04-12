from typing import TypedDict

condition = True

class Book:
    def __init__(self, title: str, author: str, publicationyear: int, Genre: str, Readstatus: bool):
        self.title = title
        self.author = author
        self.publicationyear = publicationyear
        self.genre = Genre
        self.read = Readstatus

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.publicationyear}, genre='{self.genre}', read={self.read})"

books = []

while condition:
    print("\n1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")
    inputfromuser = input("Select the option (1-6): ")
    
    if inputfromuser == "1":
        booktitle = input("Enter the book title: ")
        bookauthor = input("Enter the author name: ")
        try:
            bookyear = int(input("Enter the publication year: "))
        except ValueError:
            print("Invalid year. Please enter a number.")
            continue
        bookgenre = input("Enter the Genre of the book: ")
        bookstatus = input("Enter the read status? (yes or no): ").lower() == "yes"
        books.append(Book(booktitle, bookauthor, bookyear, bookgenre, bookstatus))
        print("Book added successfully!")
        
    elif inputfromuser == "2":
        booktitle = input("Enter the book title to remove: ")
        found_books = [b for b in books if b.title == booktitle]
        if found_books:
            for book in found_books:
                books.remove(book)
            print(f"Removed {len(found_books)} book(s) with title '{booktitle}'")
        else:
            print("Book not found")
            
    elif inputfromuser == "3":
        booktitle = input("Enter the book title to search: ")
        found_books = [b for b in books if b.title == booktitle]
        if found_books:
            print("Found books:")
            for book in found_books:
                print(book)
        else:
            print("Book not found")
            
    elif inputfromuser == "4":
        if books:
            print("All books:")
            for book in books:
                print(book)
        else:
            print("No books in the list")
            
    elif inputfromuser == "5":
        print(f"Total books: {len(books)}")
        read_count = sum(1 for book in books if book.read)
        print(f"Books read: {read_count}")
        print(f"Books unread: {len(books) - read_count}")
        
    elif inputfromuser == "6":
        condition = False
        print("Exiting.....")
        
    else:
        print("Invalid option. Please select 1-6.")