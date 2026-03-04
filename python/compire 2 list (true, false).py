a = [10,18,20,17,10]
b = [1,2,3,4,5]

m = 0

for i in range (len(a)) :

    if (a[i] > b[i]) :
        m = m + 1

if (m == len(a)) :
    print("True")
else :
    print("False")