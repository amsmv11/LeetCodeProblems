class Solution:
    def romanToInt(self, s: str) -> int:
        #i == index
        #e == letra
        res = 0
        stepUp = 0
        for i, e in reversed(list(enumerate(s))):
            if e == "I":
                if stepUp == 0:
                    res += 1
                else:
                    res -= 1
            elif e == "V":
                stepUp = 1
                res += 5

            elif e == "X":
                if stepUp < 2:
                    stepUp = 1
                    res += 10
                else:
                    res -= 10
            elif e == "L":
                stepUp = 2
                res += 50
            elif e == "C":
                if stepUp < 3:
                    stepUp = 2
                    res += 100
                else:
                    res -= 100
            elif e == "D":
                stepUp = 3
                res += 500
            elif e == "M":
                stepUp = 3
                res += 1000
        return res