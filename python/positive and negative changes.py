bin = "0101011000001"
bin = list(bin)
print(bin)

pos = 0
neg = 0

for i in range (len(bin)-1):

    if (bin[i+1] == '1'):
        pos += 1

    if (bin[i+1] == '0'):
        neg += 1

    if (bin[i] == bin[i-1]):
        if (bin[i] == '1'):
            pos -= 1
        if (bin[i] == '0'):
            neg -= 1

print (f"has {pos} positive changes and {neg} negative changes")