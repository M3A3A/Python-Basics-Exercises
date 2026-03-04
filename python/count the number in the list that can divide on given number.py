a = [[5,7,10],[4,9,15],[11,20,17]]

x = int(input("Enter Your Number :"))
count = 0
for i in range (len(a)):
    for j in range (len(a[i])):
        if (a[i][j] / x == int(a[i][j] / x)):
            count = count +1

print(f"the number in the list that can divided by {x} is {count}")