#!/usr/bin/python

import sys
import boothmul

if len(sys.argv) != 3:
    print ("I deal with 2 integers")
    exit
else:
    w1 = int(input('Width of operand 1 : '))
    w2 = int(input('Width of operand 2 : '))
    
    boothmul.boothMul(i=int(sys.argv[1]),j=int(sys.argv[2]), x=w1, y=w2 )
