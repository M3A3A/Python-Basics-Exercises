def max_three_num (x,y,z) :

    if x > y and x > z :
        return x
    elif z > x and z > y :
        return z
    else :
        return y

result = max_three_num(2,200,100) 
print(result)
