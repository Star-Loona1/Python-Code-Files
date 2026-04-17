class RomanConvertor:
    def __init__(self):
        self.numbers_mapped = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    def convert(self, num):
        roman_numeral = ""
        for value, symbol in self.numbers_mapped:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral

ob1 = RomanConvertor()
print(ob1.convert(16))
