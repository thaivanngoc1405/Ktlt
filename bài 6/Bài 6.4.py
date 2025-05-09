print("Thai Van Ngoc ")
print("MSSV: 235752020710016")
print("#####################")
class RomanToIntConverter:
    def __init__(self):
        self.roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_int(self, roman):
        result = 0
        prev_value = 0
        for char in reversed(roman):
            value = self.roman_numerals[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result
converter = RomanToIntConverter()
roman_numeral = input("Nhập số La Mã: ")
integer_value = converter.roman_to_int(roman_numeral)
print("Số nguyên tương ứng là:", integer_value)
