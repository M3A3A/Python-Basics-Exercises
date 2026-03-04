lis =  [1,1,2,3,5,8,13,21,34,55,89,144]
even = []

for i in range(len(lis)):
    if lis[i] % 2 == 0:
        even.append(lis[i])
print(even)