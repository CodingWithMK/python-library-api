from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
import re

@dataclass(eq=True, frozen=False)
class Book:
    isbn: str
    title: str
    author: str
    year: int
    genre: Optional[str] = None
    is_borrowed: bool = field(default=False, compare=False)
    borrower_id = Optional[str] = field(default=None, compare=False)
    borrowed_at = Optional[datetime] = field(default=None, compare=False)

    def __post_init__(self):
        """
        Controlling if any of the important book information like isbn, title and author is empty,
        or does not fit with the type of data requested.
        """
        # Clean ISBN
        clean_isbn = self._clean_isbn(self.isbn)

        # Validate ISBN
        if not self._validate_isbn(clean_isbn):
            raise ValueError(f"Invalid ISBN: {self.isbn}.")
        
        # Control other information
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty!")
        elif not self.author or not self.author.strip():
            raise ValueError("Author cannot be empty!")
        
        # Control Checksum
        if len(clean_isbn) == 10:
            if not self._validate_isbn10(clean_isbn):
                raise ValueError(f"Invalid ISBN-10 checksum: {self.isbn}")
            else:
                if not self._validate_isbn13(clean_isbn):
                    raise ValueError(f"Invalid ISBN-13 checksum: {self.isbn}")
        

    @staticmethod
    def _clean_isbn(isbn_string: str) -> str:
        """Cleaning unnecessary characters from ISBN"""
        # Keep digits and 'X' or 'x' only
        clean_isbn = "".join(c for c in isbn_string.upper() if c.isdigit() or c == 'X')
        return clean_isbn

    @staticmethod
    def _validate_isbn(self, isbn: str) -> str:
        self.clean_isbn = self._clean_isbn(isbn)

        if len(self.clean_isbn) == 10:
            return self._validate_isbn10(self.clean_isbn)
        elif len(self.clean_isbn) == 13:
            return self._validate_isbn13(self.clean_isbn)
        else:
            raise ValueError
    
    @staticmethod
    def _validate_isbn10(self, isbn: str) -> str:
        self.isbn = isbn
        
        self.isbn_list = list(self.isbn)
        multiplier = 10
        sum = 0
        for digit in self.isbn_list:
            product = digit * multiplier
            multiplier -= 1
            sum += product

        if sum % 11 == 0:
            return f"ISBN-10 '{self.isbn}' is valid."
        else:
            return f"ISBN-10 '{self.isbn}' is not valid!"
            
    @staticmethod
    def _validate_isbn13(self, isbn: str) -> str:
        self.isbn = isbn

        self.isbn_list = list(self.isbn)
        sum = 0
        multiply_one = self.isbn_list[0:13:2]
        multiply_three = self.isbn_list[1:12:2]

        for digit_one in multiply_one:
            result_one = int(digit_one) * 1
            sum += result_one

        for digit_three in multiply_three:
            result_three = int(digit_three) * 3
            sum += result_three
        
        if sum % 10 == 0:
            return f"ISBN-13 '{self.isbn}' is valid."
        else:
            return f"ISBN-13 '{self.isbn}' is not valid!"

    
    def __str__(self):
        return f"{self.title} from {self.author} published in {self.year} corresponds to genre {self.genre}.\nBorrow Status: {self.is_borrowed}\nBorrowed at: {self.borrowed_at}"       

    def borrow(self, borrower_name: str) -> None:
        """Borrow a book."""
        pass

    def return_book(self) -> None:
        """Return a book."""
        pass 
