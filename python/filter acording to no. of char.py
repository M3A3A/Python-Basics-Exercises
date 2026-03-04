lis = ["My Name", "Is", "Python", "Mousa"]
n = int(input("Enter a number n: "))

for i in range (len(lis)):
    if (len(lis[i]) == n):
        print(lis[i])
    else :
        print("No word with this length")