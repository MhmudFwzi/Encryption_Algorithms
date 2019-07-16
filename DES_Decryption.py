def GenerateDESkeys(input):
    "This function returns the 16 DES keys corresponding to some input"
    ###Convert input to binary
    bin1 = bin(int(input, 16))[2:]
    while bin1.__len__() != 64:
        bin1 = "0" + bin1
    ###Apply PC1
    PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    bin2 = ""
    for i in range(0,len(PC1)):
        bin2 = bin2 + bin1[PC1[i] - 1]
    ###shift first 28 and second 28 according to table
    lbin2 = bin2[0:28]
    rbin2 = bin2[28:]
    bin3 = []
    Rotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    for i in range(0,len(Rotations)):
        for j in range(0,Rotations[i]):
            lbin2 = lbin2[1:28]+ lbin2[0]
            rbin2 = rbin2[1:28] + rbin2[0]
        bin3.append(lbin2 + rbin2)
    ###Apply PC2
    PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30,40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    finalbin = []
    for i in range (0, len(bin3)):
        bin4 = ""
        for j in range(0, len(PC2)):
            bin4 = bin4 + bin3[i][PC2[j] - 1]
        finalbin.append(bin4)
    ##Convert to Hex
    Keys = []
    for k in range(0, len(finalbin)):
        Keys.append(hex(int(finalbin[k], 2)).upper()[2:])
        while Keys[k].__len__() != 12:
            Keys[k] = "0" + Keys[k]
    return Keys
def DESstage(inp,key):
    ###Convert input and key to binary
    bin1 = bin(int(inp, 16))[2:]
    while bin1.__len__() != 64:
        bin1 = "0" + bin1
    kbin1 = bin(int(key,16))[2:]
    while kbin1.__len__() != 48:
        kbin1 = "0" + kbin1
    ###Expansion permutation
    EP =[32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    lbin = bin1[0:32]
    rbin = bin1[32:]
    rbin2 = ""
    for i in range(0, len(EP)):
        rbin2 = rbin2 + rbin[EP[i] - 1]
    ###XOR with key
    rbin3 = int(rbin2,2) ^ int(kbin1,2)
    rbin3 = bin(rbin3)[2:]
    while rbin3.__len__() != 48:
        rbin3 = "0" + rbin3
    ###SBoxes
    rbin32 = ""
    Sbox1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
             0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
             4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
             15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    rbin31 = rbin3[0:6]
    row = int(rbin31[0]+rbin31[5],2)
    column = int(rbin31[1:5],2)
    rbin31 = bin(Sbox1[row*16 + column])[2:]
    while rbin31.__len__() != 4:
        rbin31 = "0" + rbin31
    rbin32 = rbin32 + rbin31
 
    Sbox2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
             3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
             0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
             13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    rbin31 = rbin3[6:12]
    row = int(rbin31[0]+rbin31[5],2)
    column = int(rbin31[1:5],2)
    rbin31 = bin(Sbox2[row*16 + column])[2:]
    while rbin31.__len__() != 4:
        rbin31 = "0" + rbin31
    rbin32 = rbin32 + rbin31
    Sbox3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
             13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
             13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
             1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    rbin31 = rbin3[12:18]
    row = int(rbin31[0]+rbin31[5],2)
    column = int(rbin31[1:5],2)
    rbin31 = bin(Sbox3[row*16 + column])[2:]
    while rbin31.__len__() != 4:
        rbin31 = "0" + rbin31
    rbin32 = rbin32 + rbin31
    Sbox4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
             13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
             10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
             3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    rbin31 = rbin3[18:24]
    row = int(rbin31[0]+rbin31[5],2)
    column = int(rbin31[1:5],2)
    rbin31 = bin(Sbox4[row*16 + column])[2:]
    while rbin31.__len__() != 4:
        rbin31 = "0" + rbin31
    rbin32 = rbin32 + rbin31
    Sbox5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
             14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
             4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
             11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    rbin31 = rbin3[24:30]
    row = int(rbin31[0]+rbin31[5],2)
    column = int(rbin31[1:5],2)
    rbin31 = bin(Sbox5[row*16 + column])[2:]
    while rbin31.__len__() != 4:
        rbin31 = "0" + rbin31
    rbin32 = rbin32 + rbin31
    Sbox6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
             10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
             9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
             4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    rbin31 = rbin3[30:36]
    row = int(rbin31[0]+rbin31[5],2)
    column = int(rbin31[1:5],2)
    rbin31 = bin(Sbox6[row*16 + column])[2:]
    while rbin31.__len__() != 4:
        rbin31 = "0" + rbin31
    rbin32 = rbin32 + rbin31
    Sbox7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
             13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
             1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
             6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    rbin31 = rbin3[36:42]
    row = int(rbin31[0]+rbin31[5],2)
    column = int(rbin31[1:5],2)
    rbin31 = bin(Sbox7[row*16 + column])[2:]
    while rbin31.__len__() != 4:
        rbin31 = "0" + rbin31
    rbin32 = rbin32 + rbin31
    Sbox8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
             1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
             7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
             2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    rbin31 = rbin3[42:]
    row = int(rbin31[0]+rbin31[5],2)
    column = int(rbin31[1:5],2)
    rbin31 = bin(Sbox8[row*16 + column])[2:]
    while rbin31.__len__() != 4:
        rbin31 = "0" + rbin31
    rbin32 = rbin32 + rbin31
    ###Permutation
    P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    rbin4 = ""
    for i in range(0, len(P)):
        rbin4 = rbin4 + rbin32[P[i] - 1]
 
    ###############TEST = PLEASE ERASE = ###########
    #test = hex(int(rbin4,2)).upper()[2:]
    #while test.__len__() != 8:
    #    test = "0" + test
    #print(test)
    ################################################
    ###XOR left with right
    rbin5 = int(rbin4,2) ^ int(lbin,2)
    rbin5 = bin(rbin5)[2:]
    while rbin5.__len__() != 32:
        rbin5 = "0" + rbin5
    rbin5 = rbin + rbin5
    fhex = hex(int(rbin5,2)).upper()[2:]
    while fhex.__len__() != 16:
        fhex = "0" + fhex
    return fhex
 
def DEStotal(initialKey, message):
    ###GENERATE KEYS
    Keys = GenerateDESkeys(initialKey)
    ###CONVERT MESSAGE TO BINARY
    message = bin(int(message, 16))[2:]
    while message.__len__() != 64:
        message = "0" + message
    ###INITIAL PERMUTATION
    IP = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9,  1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]
    message2 = ""
    for i in range(0,len(IP)):
        message2 = message2 + message[IP[i] - 1]
    ###RECONVERT TO HEX
    mhex = hex(int(message2,2)).upper()[2:]
    while mhex.__len__() != 16:
        mhex = "0" + mhex
    ###16 rounds
    for i in range(16):
        mhex = DESstage(mhex,Keys[15 - i])
    ##CONVERT TO BINARY
    temp = bin(int(mhex, 16))[2:]
    while temp.__len__() != 64:
        temp = "0" + temp
    ###32-BIT SWAP
    temp = temp[32:] + temp[0:32]
    ###INVERSE INITIAL PERMUTATION
    IIP = [40, 8, 48, 16, 56, 24, 64, 32,
           39, 7, 47, 15, 55, 23, 63, 31,
           38, 6, 46, 14, 54, 22, 62, 30,
           37, 5, 45, 13, 53, 21, 61, 29,
           36, 4, 44, 12, 52, 20, 60, 28,
           35, 3, 43, 11, 51, 19, 59, 27,
           34, 2, 42, 10, 50, 18, 58, 26,
           33, 1, 41, 9, 49, 17, 57, 25]
    message3 = ""
    for i in range(0, len(IIP)):
        message3 = message3 + temp[IIP[i] - 1]
    ###RECONVERT TO HEX
    mhex = hex(int(message3,2)).upper()[2:]
    while mhex.__len__() != 16:
        mhex = "0" + mhex
    return mhex
 
 
#DEStotal("0000000000000000","355550B2150E2451")
 
 
 
 
#INPUT
initialKey = input()
message = input()
iterations = int(input())
 
for i in range(iterations):
    message = DEStotal(initialKey, message)
print(message)
