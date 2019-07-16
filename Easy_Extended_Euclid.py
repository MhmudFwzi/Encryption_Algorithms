def GCD(X,Y):
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
    return Y
 
M,N = input().split()
M = int(M)
N = int(N)
 
if GCD(M,N) != 1:
    print("IMPOSSIBLE")
else: #a = (int(N/M)+1)*M - N
      N = N%M
      a = M - N
      mM = [1,0,M]
      mN = [0,1,N]
      while N != 1:
          mT = mM.copy()
          mM = mN.copy()
          Mtemp = mT[2]
          for i in range(3):
              mN[i] = (mT[i] - int(Mtemp/N)*mM[i])%M
          N = mN[2]
      m = mN[1]%M
      print(str(a) + " " + str(m))
