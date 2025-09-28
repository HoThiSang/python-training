class User:
    def __init__(self, user_id, user_name, age):
        self.user_id = user_id
        self.user_name = user_name
        self.age = age
        self.borrowed_books = []

    def borrow_book(self, book):
        ''' 
        Borrow a book and update its availability.
        '''
        if not book.check_book_availability():
            print(f"The book '{book.title}' is not available.")
        elif book in self.borrowed_books:
            print(f"You have already borrowed the book '{book.title}'.")
        else:
            book.borrow_book()
            self.borrowed_books.append(book)
            print(f"You have successfully borrowed the book '{book.title}'.")

    def return_book(self, book):
        '''
        Return a borrowed book and update its availability.
        '''
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book() 
            print(f"{book.title} has returned")
        else:
            print(f"{book.title} does not have borrowed.")


    def display_borrowed_book(self):
        '''
        Display list of borrowed book
        '''
        print(f"Books borrowed by {self.user_name}:")
        for i, book in enumerate(self.borrowed_books, start=1):
            print(f"{i}. {book.title} - Author: {book.author} - Book ID: {book.book_id}")