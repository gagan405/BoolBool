import sys
from bitstring import BitArray, BitStream

def boothMul(i,j,x=4,y=4):

    print ("Numbers entered are :",i, j)
    print ("Operand width : x =", x, "\t", "y =",y)    
    print()

    try:
        A=BitArray(int=i,length=x) + BitArray(int=0,length=y+1)  
        S=BitArray(int=-i,length=x) + BitArray(int=0,length=y+1)
        P=BitArray(int=0,length=x) + BitArray(int=j,length=y) + BitArray('0b0')
    except Exception as err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        return -1

    print("A =", A.bin, "\tS =", S.bin, "\tP =", P.bin)

    count=y

    while(count > 0):
        count -= 1
        
        if P[-2:] == '0b00':
            P.int >>= 1 
            print("count = ", count, "00 : ")
            print("A =", A.bin, "\tS =", S.bin, "\tP =", P.bin)
            
        elif P[-2:] == '0b01':
            Sum = P.int + A.int
            P = BitArray(int=Sum,length=x+y+2)[-(x+y+1):]
            P.int >>= 1
            print("count = ", count, "01 : ")
            print("A =", A.bin, "\tS =", S.bin, "\tP =", P.bin)
            
        elif P[-2:] == '0b10':
            Sum = P.int + S.int
            P = BitArray(int=Sum,length=x+y+2)[-(x+y+1):]
            P.int >>= 1
            print("count = ", count, "10 : ")
            print("A =", A.bin, "\tS =", S.bin, "\tP =", P.bin)
            
        else:
            P.int >>= 1 
            print("count = ", count, "11 : \n")
            print("A =", A.bin, "\tS =", S.bin, "\tP =", P.bin)
            
    P.int >>= 1 
    print(P.int)
