class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        res_aux = ""
        res = ""
        cons = s[0:2]
        if cons[0] == cons[1]:
            res = cons
        else:
            res = cons[0]
        for e in range(2, len(s)):
            #print(e)
            #caso seja Impar "bbbbabbbb"
            res_aux = ""
            j = 2
            j_aux = 0
            while e-j >= 0 and e+j_aux < len(s):
                if s[e + j_aux] == cons[e-j]:
                    #print("arranjei palindromo impar")
                    res_aux = cons[e-j:] + s[e: e+j_aux+1]
                    #print(res_aux)
                else: 
                    break
                j_aux += 1
                j += 1
            if len(res_aux) > len(res):
                res = res_aux

            #caso seja par "aaaa"
            res_aux = ""
            j = 1
            j_aux = 0
            while e-j >= 0 and e+j_aux < len(s):
                #print("iteration")
                if s[e + j_aux] == cons[e-j]:
                    #print("arranjei palindromo par")
                    res_aux = cons[e-j:] + s[e: e+j_aux+1]
                    #print(res_aux)
                else:
                    break
                j_aux += 1
                j += 1
            if len(res_aux) > len(res):
                res = res_aux

            #no fim adicionar letra ao palindromo
            cons += s[e]

        return res

