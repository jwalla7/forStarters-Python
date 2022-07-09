from collections import deque

class RomanNumerals:
    roman_string = ""

    def __init__(self):
        self

    @staticmethod
    def romanNumeralsInt(s: str) -> int:
        roman_numerals_dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        s = s[::-1]
        rn_sum = roman_numerals_dictionary[s[0]]

        for value in range(1, len(s)):
            if roman_numerals_dictionary[s[value]] < roman_numerals_dictionary[s[value - 1]]:
                rn_sum -= roman_numerals_dictionary[s[value]]
            else:
                rn_sum += roman_numerals_dictionary[s[value]]
        print(str(rn_sum))
        return rn_sum

    @staticmethod
    def romanNumeralsStr(self: int) -> str:
        roman_numerals_dictionary_1 = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

        rn_ordered_list = deque()
        queue = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]



roman_numeral_test = RomanNumerals()
roman_numeral_test.romanNumeralsInt("III")  # 3
roman_numeral_test.romanNumeralsInt("LVII")  # 58
roman_numeral_test.romanNumeralsInt("MCMXCIV")  # 1994
roman_numeral_test.romanNumeralsInt("LXXXIX")  # 89
roman_numeral_test.romanNumeralsInt("MMD")  # 2500
roman_numeral_test.romanNumeralsInt("CMLII")  # 952

# roman_numeral_test_1 = RomanNumerals()
# roman_numeral_test_1.romanNumeralsStr(3)
