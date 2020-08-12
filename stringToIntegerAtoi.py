def myAtoi(string):
    res = ""
    sign = 1
    for i in range(len(string)):
        if not string[i].isdigit():
            if string[i] == '-':
                sign = -1
            elif string != '+':
                return 0
        elif string[i].isdigit():
            res += string[i]
        
    return int(res)*sign

s = input()
print(myAtoi(s))        