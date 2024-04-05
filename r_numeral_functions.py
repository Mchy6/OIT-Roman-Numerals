def check_input(r_numeral) -> tuple:
    
    roman_numerals = "IVXLCDM"

    r_numeral_upper = r_numeral.upper()

    for i in range(len(r_numeral_upper)):
        if r_numeral_upper[i] not in roman_numerals:
            return False, r_numeral[i] + " is not a valid character."
        
    if len(r_numeral_upper) == 0:
        return False, "Empty string is not a valid Roman numeral."
        
    i_list: list[int] = _convert_to_int_list(r_numeral_upper)

def rn_to_decimal(r_numeral) -> int:
    ...

# Expects a valid Roman numeral uppercase string
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