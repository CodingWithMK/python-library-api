import unittest
from datetime import datetime
from src.book import Book

class TestBook(unittest.TestCase):
    
    def setUp(self):
        """Runs before every test - prepares fixture"""
        self.sample_book = Book(
            isbn="0306406152",
            title="Test Book",
            author="Test Author",
            year=2020,
            genre="Fiction"
        )
    
    def tearDown(self):
        """Runs after tests - Clean up"""
        pass
    
    # --- Test: Create book ---
    def test_book_creation(self):
        """Test if book is created correctly"""
        self.assertEqual(self.sample_book.isbn, "0306406152")
        self.assertEqual(self.sample_book.title, "Test Book")
        self.assertFalse(self.sample_book.is_borrowed)
        # TODO: Add other assertions
    
    # --- Test: Invalid ISBN ---
    def test_invalid_isbn(self):
        """Test invalid ISBN raises ValueError"""
        with self.assertRaises(ValueError):
            Book(isbn="invalid", title="Test", author="Author", year=2020)
    
    # --- Test: Borrow book ---
    def test_borrow_book(self):
        """Test borrowing a book"""
        # TODO: Implement
        pass
    
    # --- Test: Borrow book second time ---
    def test_borrow_already_borrowed(self):
        """Test borrowing an already borrowed book"""
        # TODO: Implement
        pass

if __name__ == '__main__':
    unittest.main()