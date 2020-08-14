def isMatchAux(s, p, lsc, asterisc):
    if p == ".*":       #aplica se a tudo
        return True
    if s == "" and p == "":  #se se acabar a string e o pattern, entao e valido
        return True
    if s == "" and len(p) == 2 and p[-1] == "*":   #se se acabar a string, pattern for qq* e valido
        return True
    if s != "" and p == "":
        return False
    if s == "" and p != "":
        if asterisc == 1:
            if len(p) == 1:
                if p[0] == lsc:
                    return isMatchAux(s, p[1:], "", 0)
                if p[0] != lsc:
                    return False  
            if p[0] == lsc and 1 < len(p) and p[1] != "*":  #falta verificar se o proximo nao e um asterisco
                return isMatchAux(s, p[1:], "", 0)
            if p[1] == "*":
                return isMatchAux(s, p[2:], lsc, 1) 
    

    else:
        i = 0
        j = 0
        current_char_pattern = p[i]
        if i+1 < len(p):        #verificar se o char a testar tem * a seguir
            if p[i+1] == "*":
                i += 2
                while j < len(s):
                    current_char_string = s[j]
                    if current_char_pattern == current_char_string:
                        j += 1
                    else:
                        break
                return isMatchAux(s[j:], p[i:], current_char_string, 1)

        current_char_string = s[j]   #foi verificado que nao tinha *
        if current_char_pattern == current_char_string or current_char_pattern == ".":
            i += 1
            j += 1
            return isMatchAux(s[j:], p[i:], current_char_string, 0)




def isMatch(s, p):
    return isMatchAux(s, p, "", 0)
    
    

print(isMatch("aaa", "a*a"))
    
    
                

        