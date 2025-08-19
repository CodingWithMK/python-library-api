def validate_isbn10(isbn: str) -> str:
        isbn = isbn
        
        isbn_list = list(isbn)
        multiplier = 10
        sum = 0
        for digit in isbn_list:
            product = int(digit) * multiplier
            multiplier -= 1
            sum += product

        if sum % 11 == 0:
            return f"ISBN-10 '{isbn}' is valid."
        else:
            return f"ISBN-10 '{isbn}' is not valid!"
        
print(validate_isbn10("0306406153"))