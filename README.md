# OIT-Roman-Numerals
OIT Code Challenge: Decimal to Roman Numeral Converter

## Process
### Structure
* I want there to be an easy way to use the program, so it's been clear from the start that I want to have a `main.py` file to run and a seperate file that includes the functions.
* After some deliberation, I've decided to use 3 different functions in my `r_numeral_functions.py` file
* `check_input` and `rn_to_decimal` could probably be combined into one function with slightly improved efficiency, but that would violate single-responsibility rule.
### Why `_convert_to_int_list`?
`_convert_to_int_list` returns a list of integers representing the Roman numeral. 0 corresponds with I, 1 corresponds with V, etc. It is used in both `check_input` and `rn_to_decimal`.
* To check for subtractive notation, it is necessary to be able to compare two roman numerals with < or >, and (e.g.) `C < D` doesn't work.
* To solve this, I could directly translate each character to its corresponding value (e.g. I:1, V:5, etc.), but that creates two problems:
    1. The actual value of the roman numeral can be altered by subtractive notation, so we need to check for subtractive notation before translating each character to its value
    2. The numerical distance between each character is not constant, so converting it to these int values would make it difficult to check that subtractive notation is written properly
* Converting to an int list avoids both of those problems. Characters are not prematurely translated to their values and checking if subtractive notation is done properly is simple.
* Having an int list also has the added bonus of easily determining between roman numerals with a leading number 1 (I, X, C, M) and a leading number 5 (V, L, D). This is done by checking if the int list value is odd or even.

## Handwritten Notes

## Misc.
Time spent:
Runtime/executable version: Python
No additional dependencies
