


class Book:
    def __init__(self, isbn: str, title: str, author: str):
        """Represents all information for a book."""
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author} -> ISBN: {self.isbn}"
    
    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r})"

    def display_book_info(self) -> str:
        print(f"Book ISBN: {self.isbn}\nBook title: {self.title}\n")

    def borrow_book(self):
        if not self.is_borrowed:
            is_borrowed = True
        else:
            raise ValueError(f"{self.title} is already borrowed. Please search for another book to borrow.")
        
    def return_book(self):
        if self.is_borrowed:
            is_borrowed = False
        else:
            raise ValueError(f"{self.title} was not borrowed.")
        

    

    