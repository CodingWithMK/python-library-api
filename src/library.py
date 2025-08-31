from dataclasses import dataclass
from book import Book
from typing import Optional, List


@dataclass
class Library:
    store_path: str
    books: List


    