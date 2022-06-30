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


roman_numeral_test = RomanNumerals()
roman_numeral_test.romanNumeralsInt("III")  # 3
roman_numeral_test.romanNumeralsInt("LVII")  # 58
roman_numeral_test.romanNumeralsInt("MCMXCIV")  # 1994
roman_numeral_test.romanNumeralsInt("LXXXIX")  # 89
roman_numeral_test.romanNumeralsInt("MMD")  # 2500
