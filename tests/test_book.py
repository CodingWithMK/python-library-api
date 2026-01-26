import pytest
from datetime import datetime
from book import Book

# --- Fixture: Test için hazır Book nesnesi ---
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

# --- Test: Book Oluşturma ---
def test_book_creation(sample_book):
    """Test if book is created correctly"""
    # TODO: Assert'lerle kontrol et:
    # - isbn doğru mu?
    # - title doğru mu?
    # - is_borrowed False mu?
    assert sample_book.isbn == "0306406152"
    # TODO: Diğer assert'leri ekle
    pass

# --- Test: ISBN Validasyonu ---
def test_invalid_isbn():
    """Test invalid ISBN raises ValueError"""
    # TODO: pytest.raises kullanarak hata kontrolü yap
    with pytest.raises(ValueError):
        Book(isbn="invalid", title="Test", author="Author", year=2020)

# --- Test: Borrow İşlemi ---
def test_borrow_book(sample_book):
    """Test borrowing a book"""
    # TODO: Implement
    # 1. borrow_book çağır
    # 2. is_borrowed True mu?
    # 3. borrower_id doğru mu?
    # 4. borrowed_at None değil mi?
    pass

# --- Test: Aynı Kitabı İki Kez Ödünç Alma ---
def test_borrow_already_borrowed_book(sample_book):
    """Test borrowing an already borrowed book raises error"""
    # TODO: Implement
    # 1. İlk ödünç alma
    # 2. İkinci ödünç almada ValueError bekliyoruz
    pass

# --- Test: İade İşlemi ---
def test_return_book(sample_book):
    """Test returning a book"""
    # TODO: Implement
    pass

# --- Test: Ödünç Alınmamış Kitabı İade Etme ---
def test_return_not_borrowed_book(sample_book):
    """Test returning a book that was not borrowed"""
    # TODO: Implement
    pass