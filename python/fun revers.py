def revers() :
    str1 = input(("enter your string to revers : "))
    str2 = []
    for i in range (len(str1)) :
        v = str1 [len(str1)-i-1]
        str2.append(v)

    rever = "".join(str2)
    return rever

result = revers()
print (result)

