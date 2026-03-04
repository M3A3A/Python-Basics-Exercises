ask = str(input("Enter yout statement : "))
print ("=========================================")
asclis = []
ascien = []

for i in range (len(ask)) :
    asclis.append(ord(ask[i]))
print (asclis)

for j in range (len(asclis)) :
    if 97 <= asclis[j] <= 122 :
        zero = asclis[j] - 97
        shift = (zero + 3) % 26 
        ascien.append(chr(shift+97))
    elif 65 <= asclis[j] <= 90 :
        zero = asclis[j] - 65
        shift = (zero + 3) % 26 
        ascien.append(chr(shift+65))
print(ascien)
final = "".join(ascien)
print(final)



