import difflib
def longestCommonPrefix(strs):
    if strs == []:
        return ""
    if len(strs) == 1:
        return strs[0]
    comparative = strs[0]
    aux = ""
    for i in range(1, len(strs)):
        if aux != "":
            comparative = aux
        elif comparative == "":
            break
        if strs[i] == "":
            return ""
        aux = ""
        for i,s in enumerate(strs[i]):
            if i<len(comparative) and comparative[i] == s:  #se os chars forem iguais
                aux += s
            else:
                comparative = aux
                break
    if aux != "":
        return aux
    else:
        return comparative

longestCommonPrefix(["abab","aba",""])
    