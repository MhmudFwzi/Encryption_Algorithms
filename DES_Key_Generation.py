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
 
Input = input()
Output= GenerateDESkeys(Input)
for i in range(0, len(Output)):
    print (Output[i])
