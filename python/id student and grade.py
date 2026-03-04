a = [[1,90],[2,80],[3,70],[4,60],[5,50]]

x = int(input("Enter the ID of student: "))
for i in range (len(a)):
    if (a[i][0] == x):
        print(f"The grade of student with ID {x} is {a[i][1]}")