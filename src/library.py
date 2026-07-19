from dataclasses import dataclass, field
from book import Book
from typing import Optional, List
from pathlib import Path
import json


@dataclass
class Library:
    store_path: str
    books: List[Book] = field(default_factory=list)

    def __post_init__(self):
        self.load_books()

    def load_books(self):
        try:
            with open(self.store_path, "r") as file:
                data = json.load(file)
                for book in data:
                    book_data = Book(**book)
                    self.books.append(book_data)
                
        except FileNotFoundError as error:
            print("Register for books (library.json) does not exist or not found.", error)
            self.books = []

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




    