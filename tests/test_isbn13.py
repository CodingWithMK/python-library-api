def validate_isbn13(isbn: str) -> str:
    isbn = isbn

    isbn_list = list(isbn)
    sum = 0
    multiply_one = isbn_list[0:13:2]
    multiply_three = isbn_list[1:12:2]

    for digit_one in multiply_one:
        result_one = int(digit_one) * 1
        sum += result_one

    for digit_three in multiply_three:
        result_three = int(digit_three) * 3
        sum += result_three

    if sum % 10 == 0:
        return f"ISBN-13 '{isbn}' is valid."
    else:
        return f"ISBN-13 '{isbn}' is not valid!"
    
print(validate_isbn13("9780306406157"))

        