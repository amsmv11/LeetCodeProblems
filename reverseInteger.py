class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        res = 0
        if x < 0:
            flag = 1
        x = abs(x)
        pot_dez = len(str(x)) -1
        
        while pot_dez >= 0:
            res += x%10 * 10**pot_dez
            pot_dez -= 1
            x = x//10
            
        if res > (2**31 -1):
            res = 0
        
        if flag:
            res *= -1
        
        return res