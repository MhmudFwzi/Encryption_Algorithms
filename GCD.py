X,Y = input().split()
X = int(X)
Y = int(Y)
 
if Y > X:
    temp = X
    X = Y
    Y = temp
while X%Y != 0:
    while X>Y:
        X = X - Y
    temp = X
    X = Y
    Y = temp
print(Y)
