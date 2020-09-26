#---------------------------------------------------------------------#                            Date:   26-09-2020
#       Define diffrent function used in disassembler    FILE 1       #
#---------------------------------------------------------------------#

from opcode import *


 
#------------------------------------------------------------------------#
#             function: (hexadecimal to decimal convertor)               #
#   1. INPUT  (list of hex digit)                                        #
#   2. OUTPUT (int type decimal equivalent)                              #
#------------------------------------------------------------------------#
def dec(number):
    length = len(number)    # no. of hex digit in list 

    x = 0                   # temp number[i] sotre
    index = 0               # store decimal equvilent 
    result = 0
    power = 0               # power of hex significent digit 
    for i in range((length-1),-1,-1):
        x = number[i]

        # Match all hex possible digits 
        if x == '0':
            index = 0
        elif x == '1':
            index = 1 
        elif x == '2':
            index = 2
        elif x == '3':
            index = 3
        elif x == '4':
            index = 4
        elif x == '5':
            index = 5
        elif x == '6':
            index = 6
        elif x == '7':
            index = 7
        elif x == '8':
            index = 8 
        elif x == '9':
            index = 9 
        
        
        elif x == 'A':
            index = 10
        elif x == 'a':
            index = 10 
        
        elif x == 'B':
            index = 11
        elif x == 'b':
            index = 11 

        elif x == 'C':
            index = 12 
        elif x == 'c':
            index = 12 

        elif x == 'D':
            index = 13 
        elif x == 'd':
            index = 13 
        
        elif x == 'E':
            index = 14 
        elif x == 'e':
            index = 14 
        
        else:
            index = 15 
       

        if power == 0:              # because x^0 = 1 
            result = index
        else:
            result = result + (index) * (16**power)     
        power += 1                  # increment power counter variable 
    
    return result                   # return decimal equvilant 


#------------------------------------------------------------------------#
#               function:   (return register number)                     #
#   1.  input (string type opcode digit)                                 #
#   2.  return (int type reg. number)                                    #
#------------------------------------------------------------------------#
def reg_number(opcode,index):          # index value provide where location of reg. 
    x = dec(opcode)                    # convert hex digit to decimal 
    return (opcodes[x][index])







