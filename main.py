from r_numeral_functions import check_input
from r_numeral_functions import rn_to_decimal

while True:
    r_numeral: str = input("\nEnter a Roman numeral: ")

    is_roman_numeral: bool = check_input(r_numeral)[0]

    if is_roman_numeral:
        print("The Roman numeral", r_numeral.upper(), "is equal to", rn_to_decimal(r_numeral), "in decimal.")
    else:
        print(check_input(r_numeral)[1])

    continue_loop = input("\nEnter another Roman numeral? (y/n): ")
    if continue_loop == "n":
        break
    elif continue_loop != "y":
        print("Invalid input. Exiting program.")
        break