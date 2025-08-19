test = "  hello  "
stripped = test.strip()
print(stripped)

isbn = " 978-0-13-601970-1 "
result = isbn.split("-")
print(type(result))
print(result)

def clean_isbn(isbn_string: str) -> str:
    # Sadece sayıları ve X'i tut
    return "".join(c for c in isbn_string.upper() if c.isdigit() or c == 'X')

print(clean_isbn("ISBN: 0-306-40615-X"))