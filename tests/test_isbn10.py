# def validate_isbn10(isbn: str) -> str:
#         isbn = isbn
        
#         isbn_list = list(isbn)
#         multiplier = 10
#         sum = 0
#         for digit in isbn_list:
#             product = int(digit) * multiplier
#             multiplier -= 1
#             sum += product

#         if sum % 11 == 0:
#             return f"ISBN-10 '{isbn}' is valid."
#         else:
#             return f"ISBN-10 '{isbn}' is not valid!"
        
# print(validate_isbn10("0306406153"))


def validate_isbn10(isbn: str) -> bool:

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

print(validate_isbn10("0306406152"))