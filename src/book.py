from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
import re

@dataclass(eq=True, frozen=True)
class Book:
    isbn: str
    title: str
    author: str
    year: int
    genre: Optional[str] = None
    is_borrowed = bool = field(default=False, compare=False)
    borrower_id = Optional[str] = field(default=None, compare=False)
    borrowed_at = Optional[datetime] = field(default=None, compare=False)

    def __post_init__(self, isbn: str):
        """
        Controlling if any of the important book information like isbn, title and author is empty,
        or does not fit with the type of data requested.
        """
        self._isbn = isbn

        regex = "^(?=(?:[^0-9]*[0-9]){10}(?:(?:[^0-9]*[0-9]){3})?$)[\\d-]+$"

        # Compiling Regex
        compiled = re.compile(regex)

        if (self._isbn == None):
            raise ValueError
        
        # Return ISBN if mathces Regex format
        if (re.search(compiled, self._isbn)):
            return isbn
        
        else:
            return f"{self._isbn} is not valid."
        

    
    def _clean_isbn(self, isbn_string: str) -> str:
        """Cleaning unnecessary characters from ISBN"""
        self._isbn = isbn_string

        self._isbn.strip()
        self._isbn.split("-")
        self._isbn.split(" ")





        

    def validate_isbn(self, isbn: str) -> bool:
        pass

    
    def _validate_isbn10(self, isbn: str) -> str:
        self.isbn = isbn
        
        self.isbn.split("-")
        self.isbn_list = list(self.isbn)
        for digit in self.isbn_list:
            pass
            

    def _validate_isbn13(self, isbn: str) -> str:
        self.isbn = isbn

        self.isbn.split("-")
        self.isbn_list = list(self.isbn)
        for digit in self.isbn_list:
            pass
