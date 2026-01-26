import pytest
from datetime import datetime
from src.book import Book

# --- Fixture: Test-Ready book object ---
@pytest.fixture
def sample_book():
    """Create a sample book for testing"""
    return Book(
        isbn="0306406152",
        title="Test Book",
        author="Test Author",
        year=2020,
        genre="Fiction"
    )

# --- Test: Create book ---
def test_book_creation(sample_book):
    """Test if book is created correctly"""
    assert sample_book.isbn == "0306406152"
    assert sample_book.title == "Test Book"
    assert sample_book.author == "Test Author"
    assert sample_book.year == 2020
    assert sample_book.genre == "Fiction"

# --- Test: ISBN Validation ---
def test_invalid_isbn():
    """Test invalid ISBN raises ValueError"""
    with pytest.raises(ValueError):
        Book(isbn="0306406153", title="Test", author="Author", year=2020)

# --- Test: borrow book ---
def test_borrow_book(sample_book):
    """Test borrowing a book"""
    sample_book.borrow_book("Jack")
    assert sample_book.is_borrowed == True
    assert sample_book.borrower_id == "Jack"
    assert sample_book.borrowed_at == "2026-01-26"

# --- Test: Try to boorow book twice ---
def test_borrow_already_borrowed_book(sample_book):
    """Test borrowing an already borrowed book raises error"""
    sample_book.borrow_book("Jack")
    assert sample_book.borrow_book("Mesut")


# --- Test: Return book ---
def test_return_book(sample_book):
    """Test returning a book"""
    sample_book.return_book()
    assert sample_book.is_borrowed == False
    assert sample_book.returned_at == "2026-01-26"
    assert sample_book.borrower_id == None
    assert sample_book.borrowed_at == None

# --- Test:Returning a not borrowed book ---
def test_return_not_borrowed_book(sample_book):
    """Test returning a book that was not borrowed"""
    assert sample_book.return_book()