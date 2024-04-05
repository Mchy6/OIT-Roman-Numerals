def check_input(r_numeral) -> tuple:

    r_numeral_upper = r_numeral.upper()

    # Check if all the characters are valid Roman numerals
    roman_numerals = "IVXLCDM"

    for i in range(len(r_numeral_upper)):
        if r_numeral_upper[i] not in roman_numerals:
            return False, r_numeral[i] + " is not a valid character."
        
    # Check if the string is empty
    if len(r_numeral_upper) == 0:
        return False, "Empty string is not a valid Roman numeral."
        
    i_list: list[int] = _convert_to_int_list(r_numeral_upper)

    repeated: int = 1
    for i in range(len(i_list) - 1):

        # Increment repeated if the current character is the same as the next character
        if i < (len(i_list) - 1) and i_list[i] == i_list[i + 1]:
            repeated += 1
        else:
            repeated = 1
            
        # Characters I, X, C, and M
        if i_list[i] % 2 == 0:
            # Check subtractive notation is being used properly (ex: IL is not valid)
            if i_list[i] + 2 < i_list[i + 1]:
                return False, r_numeral_upper[i + 1] + " cannot be preceded by " + r_numeral_upper[i]

            # Check if current character is repeated more than three times
            if repeated > 3:
                return False, r_numeral_upper[i] + " cannot be repeated more than three times."
            
        # Characters V, L, and D
        else:
            # Check subtractive notation is not being used with these characters as subtrahends
            if i_list[i] < i_list[i + 1]:
                return False, r_numeral_upper[i + 1] + " cannot be preceded by " + r_numeral_upper[i]
            
            # Check if current character is repeated more than once
            if repeated > 1:
                return False, r_numeral_upper[i] + " cannot be repeated more than once."

    return True, ""

# Expects a valid Roman numeral uppercase string
# Returns the decimal equivalent of the Roman numeral
def rn_to_decimal(r_numeral) -> int:

    i_list: list[int] = _convert_to_int_list(r_numeral.upper())
    result_list: list[int] = []

    # Convert i_list to corresponding decimal values
    for i in range(len(i_list)):
        if i_list[i] == 0:
            result_list.append(1)
        if i_list[i] == 1:
            result_list.append(5)
        if i_list[i] == 2:
            result_list.append(10)
        if i_list[i] == 3:
            result_list.append(50)
        if i_list[i] == 4:
            result_list.append(100)
        if i_list[i] == 5:
            result_list.append(500)
        if i_list[i] == 6:
            result_list.append(1000)

        # Handle subtractive notation
        if i < (len(i_list) - 1) and i_list[i] < i_list[i + 1]:
            result_list[i] *= -1

    return sum(result_list)

# Expects an uppercase string including only valid Roman numeral characters
# Returns a list of integers representing the Roman numeral
def _convert_to_int_list(r_numeral) -> list[int]:
    decimal_list = []
    for char in r_numeral:
        if char == "I":
            decimal_list.append(0)
        elif char == "V":
            decimal_list.append(1)
        elif char == "X":
            decimal_list.append(2)
        elif char == "L":
            decimal_list.append(3)
        elif char == "C":
            decimal_list.append(4)
        elif char == "D":
            decimal_list.append(5)
        elif char == "M":
            decimal_list.append(6)

    return decimal_list