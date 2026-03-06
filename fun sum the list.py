def sum_all_list () :

    sum = 0
    lis = (1,2,3,4,5,6,7,8,9,10)
    for i in range (len(lis)) :
        sum += lis[i]

    return sum

result = sum_all_list()
print(result)
  