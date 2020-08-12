    res = ""
    sign = 1
    flag = 0
    for i in range(len(str)):
        if not str[i].isdigit():
            if flag == 0:    
                if str[i] == '-':
                    sign = -1
                    flag = 1
                elif str[i] == '+':
                    flag = 1
                elif str[i] != ' ':
                    return 0
            else:
                break
        elif str[i].isdigit():
            flag = 1
            res += str[i]
    if flag == 0 or res == "":
        return 0
    if int(res) >= 2**31:
        res = 2**31
        if sign == 1:
            res -= 1
        
    return int(res)*sign