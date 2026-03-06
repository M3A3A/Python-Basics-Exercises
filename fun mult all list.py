def mul_all_list () :

    mult = 1
    lis = (1,2,3,4,5,6,7,8,9,10)
    for i in range (len(lis)) :
        mult *= lis[i]
    return mult

result = mul_all_list()
print (result)