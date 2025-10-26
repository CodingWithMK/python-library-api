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
    borrower_id: Optional[str] = field(default=None, compare=False)
    borrowed_at: Optional[datetime] = field(default=None, compare=False)
    returned_at: Optional[datetime] = field(default=None, compare=False)

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
    def _validate_isbn(self, isbn: str) -> bool:
        clean_isbn = self._clean_isbn(isbn)

        if len(clean_isbn) == 10:
            return self._validate_isbn10(clean_isbn)
        elif len(clean_isbn) == 13:
            return self._validate_isbn13(clean_isbn)
        else:
            raise ValueError
    
    @staticmethod
    def _validate_isbn10(isbn: str) -> bool:

        if len(isbn) != 10:
            return False

        # Checksum calculation
        total = 0
        for digit, char in enumerate(isbn):
            if digit == 9 and char == "X": # Controling if last character is 'X'
                value = 10
            elif char.isdigit():
                value = int(char)
            else:
                return False

            weight = 10 - digit
            total += value * weight


        # Mod 11 Control: Is total value divisible by 11
        return total % 11 == 0
            
    @staticmethod
    def _validate_isbn13(isbn: str) -> bool:
        
        total = sum(int(digit) * (3 if num % 2 == 1 else 1) for num, digit in enumerate(isbn))
        
        return total % 10 == 0

    
    def __str__(self):
        return f"{self.title} from {self.author} published in {self.year} corresponds to genre {self.genre}.\nBorrow Status: {self.is_borrowed}\nBorrowed at: {self.borrowed_at}"

    def validate_year(self):
        """Validate publication year of the book."""
        if not isinstance(self.year, int):
            raise ValueError(f"Year {self.year} of publishment not valid. Must be an integer. Please check and try again.")
        elif self.year <= 0:
            raise ValueError(f"Year of Publishment cannot be zero.")
        elif self.year < 1450 or self.year > datetime.now().year:
            raise ValueError(f"The book {self.title} from {self.year} is out of publishment range.")
        else:
            return self.year
          

    def borrow_book(self, borrower_name: str) -> None:
        """Borrow a book."""
        if not isinstance(borrower_name, str) or not borrower_name.strip():
            raise ValueError("Borrower name cannot be empty. Please check and try again.")
        
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            raise ValueError(f"{self.title} is already borrowed by {borrower_name}.")
        
        self.borrower_id = borrower_name
        self.borrowed_at = datetime.now()


    def return_book(self) -> None:
        """Return a book."""
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            raise ValueError(f"{self.title} was not borrowed. Borrow now.")
        
        self.returned_at = datetime.now()
        
    
