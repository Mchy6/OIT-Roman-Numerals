# OIT-Roman-Numerals
OIT Code Challenge: Decimal to Roman Numeral Converter

## Process
### Structure
* I want there to be an easy way to use the program, so it's been clear from the start that I want to have a `main.py` file to run and a seperate file that includes the functions
* After some deliberation, I've decided to use 3 different functions in my `r_numeral_functions.py` file
* `check_input` and `rn_to_decimal` could probably be combined into one function with slightly improved efficiency, but that would violate single-responsibility rule 
### Why `convert_to_int_list`?
`convert_to_int_list` returns a list of integers representing the Roman numeral. 0 corresponds with I, 1 corresponds with V, etc. It is used in both `check_input` and `rn_to_decimal`.
* To check for subtractive notation, it is necessary to be able to compare two roman numerals with < or >, and `C < D` (e.g.) doesn't work.
* To solve this, I could directly translate each character to its corresponding value (e.g. I:1, V:5, etc.), but that creates two problems:
    1. The actual value of the roman numeral can be altered by subtractive notation, so we need to check for subtractive notation before translating each character to its value
    2. The numerical distance between each character is not constant, so converting it to these int values would make it difficult to check that subtractive notation is written properly

## Handwritten Notes
