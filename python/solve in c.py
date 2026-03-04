
a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))

up = -b + ((b**2-4*a*c)**0.5)
up1 = -b - ((b**2-4*a*c)**0.5)
down = 2*a

X1 = up/down
X2 = up1/down

print (f"The Value Of X1 = {X1} When X = {up}/{down}")
print (f"The Value Of X2 = {X2} When X = {up1}/{down}")


