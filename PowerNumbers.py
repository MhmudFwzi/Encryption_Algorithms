a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
 
bbin = bin(b)[2:]
aBinaryPowers = []
for i in range(len(bbin)):
    if i == 0:
        aBinaryPowers.append(a%c)
    else: aBinaryPowers.append(aBinaryPowers[i-1]*aBinaryPowers[i-1]%c)
product = 1
for i in range (len(bbin)):
    if (bbin[i] == "1"):
        product = product*aBinaryPowers[bbin.__len__()-i - 1]
print(product%c)
