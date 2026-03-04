n = int(input("Enter a number n: "))

A = [[(i + j)**2 for j in range(n)] for i in range(n)]

print("The 2D list A:")
for row in A:
    print(row)
    