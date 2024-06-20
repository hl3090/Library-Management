class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        self.books.append({
            'title': title,
            'author': author,
            'year': year,
            'borrowed': False
        })
        print(f"Book '{title}' by {author} added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                status = "Borrowed" if book['borrowed'] else "Available"
                print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {status}")

    def borrow_book(self, title):
        for book in self.books:
            if book['title'] == title:
                if book['borrowed']:
                    print(f"Book '{title}' is already borrowed.")
                else:
                    book['borrowed'] = True
                    print(f"Book '{title}' borrowed successfully.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book['title'] == title:
                if book['borrowed']:
                    book['borrowed'] = False
                    print(f"Book '{title}' returned successfully.")
                else:
                    print(f"Book '{title}' is not borrowed.")
                return
        print(f"Book '{title}' not found in the library.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add book")
        print("2. Remove book")
        print("3. List books")
        print("4. Borrow book")
        print("5. Return book")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter book year: ")
            library.add_book(title, author, year)
        elif choice == "2":
            title = input("Enter book title: ")
            library.remove_book(title)
        elif choice == "3":
            library.list_books()
        elif choice == "4":
            title = input("Enter book title: ")
            library.borrow_book(title)
        elif choice == "5":
            title = input("Enter book title: ")
            library.return_book(title)
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()