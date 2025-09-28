from book import Book
from user import User

class Library:
    list_users = []
    list_books = []

    def add_new_user(self, user):
        '''Add new user'''
        self.list_users.append(user)

    def add_new_book(self, book):
        '''
        Add a new book to the library collection.
        '''
        self.list_books.append(book)

    def search_book(self, query):
        """Find book by title"""
        books = [book for book in self.list_books if query.lower() in book.title.lower()]
        if len(books) == 1:
            print(f"Book: {books[0].title}\nAuther: {books[0].author}\nQuantity: {books[0].quantity}")
        if not books:
            print("Not found book")

    def add_book(self):
        '''Add new book'''
        book_id = input("Enter book ID (it is a series number and character like this : 978-ABC): ").strip()
        title = input("Enter book name: ").strip()
        author = input("Enter author name: ").strip()
        quantity = int(input("Enter quantity of book: "))
        new_book = Book(book_id, title, author, quantity)
        self.add_new_book(new_book)
        print("Add new book successfully")

    def display_books(self):
        '''display list of books'''
        for i, book in enumerate(self.list_books, start=1):
            print(f"{i}. {book.title} - author: {book.author} - Book ID: {book.book_id}")


def main():
    '''Main function'''
    library = Library()

    book1 = Book("978-ABC", "Clean Code", "Robert C. Martin", 20)
    book2 = Book("978-AER", "Coding Covention", "Robert C. Martin", 3)

    user1 = User(1, 'Alexander', 30)

    library.add_new_book(book1)
    library.add_new_book(book2)
    library.add_new_user(user1)
    user1.borrow_book(book1)

    while True:
        print('''====== WELCOME TO LIBRARY MANAGEMENT SYSTEM ======
        1. View list of books
        2. Add new book
        3. Search book
        4. Borrow book
        5. Return book
        6. Exit
        ''')

        try:
            choice = int(input("What do you want to do? "))
        except ValueError:
            print("Please enter a number from 1 to 6.")
            continue
        match choice:
            case 1:
                print("====== LIST OF BOOKS ======")
                library.display_books()

            case 2:
                print("====== ADD NEW BOOK ======")
                library.add_book()

            case 3:
                query = input("Enter book's title: ")
                print("===================Result==============")
                library.search_book(query)

            case 4:
                try:
                    user_id = int(input("Enter your ID: "))
                    user = next((u for u in library.list_users if u.user_id == user_id), None)
                    if not user:
                        print(f"Not found user with ID {user_id}")
                    else:
                        library.display_books()
                        book_id_input = input("Enter the 'Book ID' of the book from the list above: ").strip()
                        book = next((b for b in library.list_books if b.book_id == book_id_input), None)
                        if book:
                            user.borrow_book(book)
                        else:
                            print("Book not found.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer ID.")

            case 5:
                try:
                    user_id = int(input("Enter your ID: "))
                    user = next((u for u in library.list_users if u.user_id == user_id), None)
                    if not user:
                        print(f"Not found user with ID {user_id}")
                    else:
                        user.display_borrowed_book()
                        book_id_input = input("Enter 'Book ID' from the list above: ").strip()
                        book = next((b for b in library.list_books if b.book_id == book_id_input), None)
                        user.return_book(book)
                except ValueError:
                    print("Invalid input. Please enter a valid integer ID.")

            case 6:
                print("Goodbye!")
                break

            case _:
                print("Invalid choice. Please select 1-6.")

        cont = input("\nDo you want to exit? (type 'exit' to quit, press Enter to continue): ")
        if cont.strip().lower() == 'exit':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
