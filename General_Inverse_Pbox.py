
 IN,OUT = input().split()
IN = int(IN)
OUT = int(OUT)
P = input().split(" ")
for i in range(0,len(P)):
    P[i] = int(P[i])
 
 
if OUT<IN : print("IMPOSSIBLE")
else:
    v = 1
    for i in range(IN):
        if i+1 not in P:
            v = 0
            print("IMPOSSIBLE")
    if v == 1:
        O = []
        for i in range(IN):
            O.append(P.index(i+1) + 1)
        print(*O, sep=' ')
