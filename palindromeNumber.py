def isPalindrome(x):
    str = str(x)
    i = 0
    for i in range(len(str)//2):
        if str[i] != str[-i-1]:
            return False
    return True