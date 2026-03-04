import random 

a = [random.randint(1, 100) for _ in range(10)]
print("List a:", a)

gusses = 0
for i in range (10):
    x = int(input("Enter a number to search in the list: "))
    for j in range (10):
        if (a[j] == x):
                gusses += 1
        else:
                continue

print(f"The number of true guesses {gusses} times in the list.")  