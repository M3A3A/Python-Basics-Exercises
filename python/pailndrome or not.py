lis = "qwerty"
lis = list(lis)
print(lis)

for i in range (len(lis)-1):

    if (lis[len(lis)-1-i] == lis[i]) :
        print("is palindrome")
        break
    else:
        print("is not palindrome")
        break
