class Book:

    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def check_book_availability(self):
        '''Check if the book is available to borrow.'''
        return self.quantity > 0

    def borrow_book(self):
        """ 
        Borrow a book and add it to the user's borrowed books list. 
        """
        self.quantity -= 1

    def return_book(self):
        '''
        Return a borrowed book and update the user's borrowed books list
        '''
        self.quantity += 1