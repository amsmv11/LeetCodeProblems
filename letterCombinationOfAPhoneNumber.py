def combination(strList):
    if len(strList) == 1:
        return [z for z in strList[0]]
    a = strList[0]
    b = strList[1]
    res = [x+y for x in a for y in b]
    if len(strList) == 3:
        c = strList[2]
        return [x+y for x in res for y in c]
        
    elif len(strList) == 4:
        c = strList[2]
        res1 = [x+y for x in res for y in c]
        d = strList[3]
        return [x+y for x in res1 for y in d]
    
    else:
        return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dict = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        
        myList = [dict[int(x)] for x in digits]
        return combination(myList)
        
        
        
        
        

        