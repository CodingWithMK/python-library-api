from dataclasses import dataclass
from book import Book
from typing import Optional, List


@dataclass
class Library:
    store_path: str
    books: List[Book] = None

    def add_book(self, book: Book):
        if self.books is None:
            self.books = []
        self.books.append(book)

    def remove_book(self, book: Book):
        if self.books is not None:
            self.books.remove(book)

    def list_books(self):
        if self.books is not None:
            self.books

    def find_book(self):
        pass

    def load_books(self):
        if self.books is not None:
            for book in self.books:
                print(book, "\n")

    def save_books(self):
        pass




    