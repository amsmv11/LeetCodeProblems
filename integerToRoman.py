class Solution:
    def intToRoman(self, num: int) -> str:
        unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        dezenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        milhares = ["", "M", "MM", "MMM"]
        
        res = ""
        casa_decimal = 0
        while num > 0:
            digit = num % 10
            num = num//10
            if casa_decimal == 0:
                res = unidades[digit]
            elif casa_decimal == 1:
                res = dezenas[digit] + res
            elif casa_decimal == 2:
                res = centenas[digit] + res
            elif casa_decimal == 3:
                res = milhares[digit] + res
            casa_decimal += 1
        
        return res