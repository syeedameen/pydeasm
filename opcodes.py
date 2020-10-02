
#------------------------------------------------------------------------#
#                     Declare Global Variables                           #
#------------------------------------------------------------------------#

l           = []            # list to store one line instruction 
line_buffer = []            # list store hex line 
address     = 0             # current address of hex digit in decimal 
byte_count  = 0             # no. of byte in a line 
record_type = 0             # intel hex file record type 
data        = []            # contain byte data of hex line  
i           = 0             # data byte slicing index variable  






#------------------------------------------------------------------------#
#             function: (hexadecimal to decimal convertor)               #
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
#         function:   (return next byte and increment byte count)        #
#------------------------------------------------------------------------#
def read_next_byte():
    global byte_count                   # number of bytes in line 
    global data                         # line of hex digit
    global i                            # byte slicing index varible 

    i += 1                              # increment data slicing index 
    x = data[(i*2):(i*2)+2]             # get next byte into x 

    byte_count -= 1                     # increment byte count to point next hex digit           
    return str(x)                       # return value at byte_count string type 



# #------------------------------------------------------------------------#
# #          function:   (return spacific value at opcode[i][j])           #
# #------------------------------------------------------------------------#
# def reg_number(opcode,index_no):
#     x = dec(opcode)                     # convert decimal equivalent of hex 
#     reg = tab.opcode[x][index_no]
#     return str(reg)                     # return string type 





#------------------------------------------------------------------------#
#            function:   (give different filed in hex line)              #
#------------------------------------------------------------------------#
def convert_info(buffer):               # feed hex line into this function 
    global l
    global line_buffer 
    global address
    global byte_count
    global record_type
    global data 
    global i                    

    i = 0                               # for slicing hex digit 

    # slicing of different intel hex file feilds (return into gloable varible)
    line_buffer = buffer
    address     = dec(buffer[3:7])       #  address of line          
    byte_count  = dec(buffer[1:3])       #  no. of bytes in line 
    record_type = dec(buffer[7:9])       #  record type (intel specific)
    data        = buffer[9:2*byte_count] #  data except chesksum 

#-----------------------Error in while loop-------------------------------byte count is not inc
    x = 0                               # local variable to store one byte 
    # for i in range(byte_count):
    while byte_count != -1:
        l.clear()
        x = data[(i*2):(i*2)+2]         # one byte of line 
        memonics(x)                     # transfer one digit to memonics
        for k in l:
            fd.write(str(k))
        # fd.write('      RECORD TYPE:  ')
        # fd.write(str(record_type))
        # fd.write('      BYTE COUNT:    ')
        # fd.write(str(byte_count))
        # fd.write(str('  '))
        fd.write('\n')                  # feed new line character 

        i += 1                          # increment digit counter to point next digit  
        byte_count -= 1                 # decrement byte_count by 1
        


#------------------------------------------------------------------------#
#          function:   (convert hex digit into it's instruction)         #
#------------------------------------------------------------------------#    






#------------------------------------------------------------------------#
#               opcode field related different funciton                  #
#------------------------------------------------------------------------#
def append_rel_address():
    pass
def append_16_bit_address():
    pass 
def append_page_address():
    pass 
def page_address():
    pass 





#-----------------------------------------------------------------------#
#                Convert opcode to it's instruction                     #
#-----------------------------------------------------------------------#
def memonics(num):
    x = dec(num)                                # convert hexadecimal to decimal 


    if x == 0:                                  # nop 
        l.append('nop')             
    elif x == 1:                                # ajmp page_address 
        l.append('ajmp ')           
        l.append(append_page_address())
    elif x == 2:                                # ljmp 16_bit_address 
        l.append('ljmp ')
        l.append(append_16_bit_address())
    elif x == 3:                                # rr a 
        l.append('rr a')
    elif x == 4:                                # inc a 
        l.append('inc a')
    elif x == 5:                                # inc direct_address
        l.append('inc 0x')
        l.append(read_next_byte())
    elif x == 6:                                # inc @r0
        l.append('inc @r0')
    elif x == 7:                                # inc @r1
        l.append('inc @r1')
    elif x == 8:                                # inc r0 
        l.append('inc r0')                  
    elif x == 9:                                # inc r1 
        l.append('inc r1')                  
    elif x == 10:                               # inc r2 
        l.append('inc r2')                  
    elif x == 11:                               # inc r3 
        l.append('inc r3')                  
    elif x == 12:                               # inc r4 
        l.append('inc r4')                  
    elif x == 13:                               # inc r5 
        l.append('inc r5')                  
    elif x == 14:                               # inc r6 
        l.append('inc r6')                  
    elif x == 15:                               # inc r7
        l.append('inc r7')
    elif x == 16:                               # jbc rel_address
        l.append('jbc ')
        l.append(append_rel_address())
    elif x == 17:                               # acall page_address
        l.append('acall ')
        l.append(append_page_address())
    elif x == 18:                               # lcall 16_bit_addr
        l.append('lcall ')
        l.append(append_16_bit_address())
    elif x == 19:                               # rrc a 
        l.append('rrc a')
    elif x == 20:                               # dec a 
        l.append('dec a')
    elif x == 21:                               # dec direct_addr
        l.append('dec 0x')
        l.append(read_next_byte())
    elif x == 22:                               # dec @r0
        l.append('dec @r0')         
    elif x == 23:                               # dec @r1
        l.append('dec @r1')
    elif x == 24:                               # dec r0 
        l.append('dec r0')                  
    elif x == 25:                               # dec r1
        l.append('dec r1')                  
    elif x == 26:                               # dec r2
        l.append('dec r2')                  
    elif x == 27:                               # dec r3
        l.append('dec r3')                  
    elif x == 28:                               # dec r4 
        l.append('dec r4')
    elif x == 29:                               # dec r5 
        l.append('dec r5')
    elif x == 30:                               # dec r6 
        l.append('dec r6')                  
    elif x == 31:                               # dec r7 
        l.append('dec r7')                  
    elif x == 32:                               # jb rel_address
        l.append('jb ')
        l.append(append_rel_address())
    elif x == 33:                               # ajmp page_addr
        l.append('ajmp')
        l.append(append_page_address())
    elif x == 34:                               # ret 
        l.append('ret')             
    elif x == 35:                               # rl a 
        l.append('rl a')                
    elif x == 36:                               # add a,#data
        l.append('add a,#0x')
        l.append(read_next_byte())
    elif x == 37:                               # add a,direct_addr
        l.append('add a,0x')
        l.append(read_next_byte())
    elif x == 38:                               # add a,@r0
        l.append('add a,@r0')           
    elif x == 39:                               # add a,@r1
        l.append('add a,@r1')           
    elif x == 40:                               # add a,r0
        l.append('add a,r0')
    elif x == 41:                               # add a,r1
        l.append('add a,r1')                
    elif x == 42:                               # add a,r2 
        l.append('add a,r2')                
    elif x == 43:                               # add a,r3 
        l.append('add a,r3')                
    elif x == 44:                               # add a,r4 
        l.append('add a,r4')                
    elif x == 45:                               # add a,r5 
        l.append('add a,r5')                
    elif x == 46:                               # add a,r6 
        l.append('add a,r6')                
    elif x == 47:                               # add a,r7 
        l.append('add a,r7')                
    elif x == 48:                               # jnb bit_addr,rel_addr
        l.append('jnb 0x')
        l.append(read_next_byte())
        l.append(',')
        l.append(append_rel_address())
    elif x == 49:                               # acall page_addr
        l.append('acall ')
        l.append(page_address())
    elif x == 50:                               # reti 
        l.append('reti')            
    elif x == 51:                               # rcl a
        l.append('rcl a')           
    elif x == 52:                               # addc a,#data
        l.append('addc a,#0x')
        l.append(read_next_byte())
    elif x == 53:                               # addc a,direct_addr
        l.append('addc a,0x')           
        l.append(read_next_byte())          
    elif x == 54:                               # addc a,@r0
        l.append('addc a,@r0')          
    elif x == 55:                               # addc a,@r1
        l.append('addc a,@r1')          
    elif x == 56:                               # addc a,r0
        l.append('addc a,r0')           
    elif x == 57:                               # addc a,r1
        l.append('addc a,r1')
    elif x == 58:                               # addc a,r2
        l.append('addc a,r2')               
    elif x == 59:                               # addc a,r3
        l.append('addc a,r3')               
    elif x == 60:                               # addc a,r4 
        l.append('addc a,r4')               
    elif x == 61:                               # addc a,r5
        l.append('addc a,r5')               
    elif x == 62:                               # addc a,r6 
        l.append('addc a,r6')               
    elif x == 63:                               # addc a,r7 
        l.append('addc a,r7')               
    elif x == 64:                               # jc rel_addr
        l.append('jc ')
        l.append(append_rel_address())
    elif x == 65:                               # ajmp page_addr
        l.append('ajmp ')       
        l.append(append_page_address())     
    elif x == 66:                               # orl direct_addr,a 
        l.append('orl 0x')
        l.append(read_next_byte())
        l.append(',a')
    elif x == 67:                               # orl direct_addr,#data
        l.append('orl 0x')
        l.append(read_next_byte())
        l.append(',#0x')
        l.append(read_next_byte())
    elif x == 68:                               # orl a,#data
        l.append('orl a,#0x')           
        l.append(read_next_byte())          
    elif x == 69:                               # orl a,direct_addr
        l.append('orl a,0x')            
        l.append(read_next_byte())          
    elif x == 70:                               # orl a,@r0
        l.append('orl a,@r0')           
    elif x == 71:                               # orl a,@r1
        l.append('orl a,@r1')           
    elif x == 72:                               # orl a,r0
        l.append('orl a,r0')
    elif x == 73:                               # orl a,r1
        l.append('orl a,r1')                
    elif x == 74:                               # orl a,r2
        l.append('orl a,r2')                
    elif x == 75:                               # orl a,r3 
        l.append('orl a,r3')                
    elif x == 76:                               # orl a,r4 
        l.append('orl a,r4')                
    elif x == 77:                               # orl a,r5
        l.append('orl a,r5')                
    elif x == 78:                               # orl a,r6 
        l.append('orl a,r6')                
    elif x == 79:                               # orl a,r7 
        l.append('orl a,r7')                
    elif x == 80:                               # jnc rel_addr
        l.append('jnc ')
        l.append(append_rel_address())
    elif x == 81:                               # acall page_addr
        l.append('acall ')
        l.append(page_address())
    elif x == 82:                               # anl direct_addr,a
        l.append('anl 0x')          
        l.append(read_next_byte())          
        l.append(',a')          
    elif x == 83:                               # anl direct_addr,#data
        l.append('anl 0x')          
        l.append(read_next_byte())          
        l.append(',#0x')            
        l.append(read_next_byte())          
    elif x == 84:                               # anl a,#data
        l.append('anl a,#0x')           
        l.append(read_next_byte())          
    elif x == 85:                               # anl a,direct_addr
        l.append('anl a,0x')            
        l.append(read_next_byte())
    elif x == 86:                               # anl a,@r0
        l.append('anl a,@r0')                   
    elif x == 87:                               # anl a,@r1
        l.append('anl a,@r1')
    elif x == 88:                               # anl a,r0
        l.append('anl a,r0')                
    elif x == 89:                               # anl a,r1
        l.append('anl a,r1')                
    elif x == 90:                               # anl a,r2 
        l.append('anl a,r2')                
    elif x == 91:                               # anl a,r3 
        l.append('anl a,r3')                
    elif x == 92:                               # anl a,r4 
        l.append('anl a,r4')                
    elif x == 93:                               # anl a,r5 
        l.append('anl a,r5')                
    elif x == 94:                               # anl a,r6 
        l.append('anl a,r6')                
    elif x == 95:                               # anl a,r7 
        l.append('anl a,r7')
    elif x == 96:                               # jz rel_addr
        l.append('jz ')
        l.append(append_rel_address())
    elif x == 97:                               # ajmp page_addr
        l.append('ajmp ')       
        l.append(append_page_address())     
    elif x == 98:                               # xrl direct_addr,a
        l.append('xrl 0x')      
        l.append(read_next_byte())      
        l.append(',a')      
    elif x == 99:                               # xrl direct_addr,#data
        l.append('xrl 0x')      
        l.append(read_next_byte())      
        l.append(',#0x')        
        l.append(read_next_byte())      
    elif x == 100:                              # xrl a,#data
        l.append('xrl a,#0x')       
        l.append(read_next_byte())      
    elif x == 101:                              # xrl a,direct_addr
        l.append('xrl a,0x')        
        l.append(read_next_byte())      
    elif x == 102:                              # xrl a,@r0
        l.append('xrl a,@r0')       
    elif x == 103:                              # xrl a,@r1
        l.append('xrl a,@r1')
    elif x == 104:                              # xrl a,r0
        l.append('xrl a,r0')
    elif x == 105:                              # xrl a,r1
        l.append('xrl a,r1')                
    elif x == 106:                              # xrl a,r2
        l.append('xrl a,r2')                
    elif x == 107:                              # xrl a,r3 
        l.append('xrl a,r3')                
    elif x == 108:                              # xrl a,r4
        l.append('xrl a,r4')                
    elif x == 109:                              # xrl a,r5 
        l.append('xrl a,r5')                
    elif x == 110:                              # xrl a,r6 
        l.append('xrl a,r6')                
    elif x == 111:                              # xrl a,r7 
        l.append('xrl a,r7')                
    elif x == 112:                              # jnz rel_addr
        l.append('jnz ')
        l.append(append_rel_address())
    elif x == 113:                              # acall page_addr
        l.append('acall ')
        l.append(append_page_address())
    elif x == 114:                              # orl c,bit_addr
        l.append('orl c,')
        l.append(read_next_byte())
    elif x == 115:                              # jmp @a+dptr
        l.append('jmp @a+dptr')
    elif x == 116:                              # mov a,#data
        l.append('mov a,#0x')
        l.append(read_next_byte())
    elif x == 117:                              # mov direct_addr,#data
        l.append('mov 0x')      
        l.append(read_next_byte())      
        l.append(',#0x')        
        l.append(read_next_byte())      
    elif x == 118:                              # mov @r0,#data
        l.append('mov @r0,#0x')     
        l.append(read_next_byte())      
    elif x == 119:                              # mov @r1,#data
        l.append('mov @r1,#0x')     
        l.append(read_next_byte())      
    elif x == 120:                              # mov r0,#data
        l.append('mov r0,#0x')      
        l.append(read_next_byte())      
    elif x == 121:                              # mov r1,#data
        l.append('mov r1,#0x')      
        l.append(read_next_byte())      
    elif x == 122:                              # mov r2,#data
        l.append('mov r2,#0x')      
        l.append(read_next_byte())      
    elif x == 123:                              # mov r3,#data
        l.append('mov r3,#0x')      
        l.append(read_next_byte())      
    elif x == 124:                              # mov r4,#data
        l.append('mov r4,#0x')      
        l.append(read_next_byte())      
    elif x == 125:                              # mov r5,#data
        l.append('mov r5,#0x')      
        l.append(read_next_byte())      
    elif x == 126:                              # mov r6,#data
        l.append('mov r6,#0x')      
        l.append(read_next_byte())      
    elif x == 127:                              # mov r7,#data
        l.append('mov r7,#0x')      
        l.append(read_next_byte())      
    elif x == 128:                              # sjmp rel_addr
        l.append('sjmp ')       
        l.append(append_rel_address())      
    elif x == 129:                              # ajmp page_addr
        l.append('ajmp ')       
        l.append(append_page_address())     
    elif x == 130:                              # anl c,bit_addr
        l.append('anl c,0x')        
        l.append(read_next_byte())      
    elif x == 131:                              # movc a,@a+pc
        l.append('movc a,@a+pc')        
    elif x == 132:                              # div ab
        l.append('div ab')      
    elif x == 133:                              # mov direct_addr,direct_addr
        l.append('mov 0x')
        l.append(read_next_byte())
        l.append('0x')
        l.append(read_next_byte())
    elif x == 134:                              # mov direct_addr,@r0
        l.append('mov 0x')
        l.append(read_next_byte())
        l.append(',@r0')
    elif x == 135:                              # mov direct_addr,@r1
        l.append('mov 0x')          
        l.append(read_next_byte())          
        l.append(',@r1')            
    elif x == 136:                              # mov direct_addr,r0
        l.append('mov 0x')          
        l.append(read_next_byte())          
        l.append(',r0')         
    elif x == 137:                              # mov direct_addr,r1
        l.append('mov 0x')          
        l.append(read_next_byte())          
        l.append(',r1')         
    elif x == 138:                              # mov direct_add,r2
        l.append('mov 0x')          
        l.append(read_next_byte())          
        l.append(',r2')         
    elif x == 139:                              # mov direct_addr,r3 
        l.append('mov 0x')          
        l.append(read_next_byte())          
        l.append(',r3')         
    elif x == 140:                              # mov direct_addr,r4
        l.append('mov 0x')          
        l.append(read_next_byte())          
        l.append(',r4')         
    elif x == 141:                              # mov direct_addr,r5
        l.append('mov 0x')          
        l.append(read_next_byte())          
        l.append(',r5')         
    elif x == 142:                              # mov direct_addr,r6
        l.append('mov 0x')          
        l.append(read_next_byte())          
        l.append(',r6')         
    elif x == 143:                              # mov direct_addr,r7
        l.append('mov 0x')          
        l.append(read_next_byte())          
        l.append(',r7')             
    elif x == 144:                              # mov dptr,#16_bit_data
        l.append('mov dptr,#0x')            
        l.append(read_next_byte())          
        l.append(read_next_byte())          
    elif x == 145:                              # acall page_address
        l.append('acall ')          
        l.append(append_page_address())
    elif x == 146:                              # mov bit_addr,c
        l.append('mov 0x')          
        l.append(read_next_byte())          
        l.append(',c')          
    elif x == 147:                              # movc a,@a+dptr
        l.append('movc a,@a+dptr')          
    elif x == 148:                              # subb a,#data
        l.append('subb a,#0x')          
        l.append(read_next_byte())          
    elif x == 149:                              # subb a,direct_addr
        l.append('subb a,0x')
        l.append(read_next_byte)
    elif x == 150:                              # subb a,@r0
        l.append('subb a,@r0')          
    elif x == 151:                              # subb a,@r1
        l.append('subb a,@r1')          
    elif x == 152:                              # subb a,r0
        l.append('subb a,r0')
    elif x == 153:                              # subb a,r1
        l.append('subb a,r1')               
    elif x == 154:                              # subb a,r2
        l.append('subb a,r2')               
    elif x == 155:                              # subb a,r3
        l.append('subb a,r3')               
    elif x == 156:                              # subb a,r4
        l.append('subb a,r4')               
    elif x == 157:                              # subb a,r5 
        l.append('subb a,r5')               
    elif x == 158:                              # subb a,r6 
        l.append('subb a,r6')               
    elif x == 159:                              # subb a,r7 
        l.append('subb a,r7')               
    elif x == 160:                              # orl c,bit_addr
        l.append('orl c,0x')
        l.append(read_next_byte())
    elif x == 161:                              # ajmp page_addr
        l.append('ajmp ')
        l.append(append_page_address())
    elif x == 162:                              # mov c,bit_addr
        l.append('mov c,0x')
        l.append(read_next_byte())
    elif x == 163:                              # inc dptr
        l.append('inc dptr')            
    elif x == 164:                              # mul ab 
        l.append('mul ab')          
    elif x == 165:                              # intel Reserved byte 
        l.append('reserved byte')           
    elif x == 166:                              # mov @r0,direct_addr
        l.append('mov @r0,0x')          
        l.append(read_next_byte())          
    elif x == 167:                              # mov @r1,direct_addr
        l.append('mov @r1,0x')          
        l.append(read_next_byte())          
    elif x == 168:                              # mov r0,direct_addr
        l.append('mov r0,0x')           
        l.append(read_next_byte())                    
    elif x == 169:                              # mov r1,direct_addr
        l.append('mov r1,0x')
        l.append(read_next_byte())
    elif x == 170:                              # mov r2,direct_adddr
        l.append('mov r2,0x')           
        l.append(read_next_byte())          
    elif x == 171:                              # mov r3,direct_addr
        l.append('mov r3,0x')           
        l.append(read_next_byte())          
    elif x == 172:                              # mov r4,direct_addr
        l.append('mov r4,0x')           
        l.append(read_next_byte())          
    elif x == 173:                              # mov r5,direct_addr
        l.append('mov r5,0x')           
        l.append(read_next_byte())          
    elif x == 174:                              # mov r6,direct_addr
        l.append('mov r6,0x')           
        l.append(read_next_byte())          
    elif x == 175:                              # mov r7,direct_addr
        l.append('mov r7,0x')           
        l.append(read_next_byte())          
    elif x == 176:                              # anl c,!bit_address
        l.append('anl c,!0x')           
        l.append(read_next_byte())          
    elif x == 177:                              # acall page_addr
        l.append('acall ')
        l.append(append_page_address())
    elif x == 178:                              # cpl bit_addr
        l.append('cpl 0x')          
        l.append(read_next_byte())          
    elif x == 179:                              # cpl carry
        l.append('cpl c')           
    elif x == 180:                              # cjne a,#data,rel_addr
        l.append('cjne a,#0x')      
        l.append(read_next_byte())
        l.append(',0x')
        l.append(append_rel_address())
    elif x == 181:                              # cjne a,direct_addr,rel_addr
        l.append('cjne a,0x')
        l.append(read_next_byte())
        l.append(',0x')
        l.append(append_rel_address())
    elif x == 182:                              # cjne @r0,#data,rel_addr
        l.append('cjne @r0,#0x')
        l.append(read_next_byte())
        l.append(',0x')
        l.append(append_rel_address())
    elif x == 183:                              # cjne @r1,#data
        l.append('cjne @r1,#0x')        
        l.append(read_next_byte())      
        l.append(',0x')     
        l.append(append_rel_address())      
    elif x == 184:                              # cjne r0,#data
        l.append('cjne r0,#0x')     
        l.append(read_next_byte())      
        l.append(',0x')     
        l.append(append_rel_address())      
    elif x == 185:                              # cjne r1,#data
        l.append('cjne r1,#0x')     
        l.append(read_next_byte())      
        l.append(',0x')     
        l.append(append_rel_address())      
    elif x == 186:                              # cjne r2,#data
        l.append('cjne r2,#0x')     
        l.append(read_next_byte())      
        l.append(',0x')     
        l.append(append_rel_address())          
    elif x == 187:                              # cjne r3,#data
        l.append('cjne r3,#0x')     
        l.append(read_next_byte())      
        l.append(',0x')     
        l.append(append_rel_address())      
    elif x == 188:                              # cjne r4,#data,rel_addr
        l.append('cjne r4,#0x')     
        l.append(read_next_byte())      
        l.append(',0x')     
        l.append(append_rel_address())      
    elif x == 189:                              # cjne r5,#data,rel_addr
        l.append('cjne r5,#0x')     
        l.append(read_next_byte())      
        l.append(',0x')     
        l.append(append_rel_address())      
    elif x == 190:                              # cjne r6,#data,rel_addr
        l.append('cjne r6,#0x')     
        l.append(read_next_byte())      
        l.append(',0x')     
        l.append(append_rel_address())      
    elif x == 191:                              # cjne r7,#data,rel_addr
        l.append('cjne r7,#0x')     
        l.append(read_next_byte())      
        l.append(',0x')     
        l.append(append_rel_address())      
    elif x == 192:                              # push direct_addr
        l.append('push 0x')       
        l.append(read_next_byte())      
    elif x == 193:                              # ajmp page_addr
        l.append('ajmp ')       
        l.append(append_page_address())      
    elif x == 194:                              # clr bit_addr
        l.append('clr 0x')      
        l.append(read_next_byte())      
    elif x == 195:                              # clr carry 
        l.append('clr c')       
    elif x == 196:                              # swap a
        l.append('swap a')      
    elif x == 197:                              # xch a,direct_addr
        l.append('xch a,0x')        
        l.append(read_next_byte())      
    elif x == 198:                              # xch a,@r0
        l.append('xch a,@r0')       
    elif x == 199:                              # xch a,@r1
        l.append('xch a,@r1')       
    elif x == 200:                              # xch a,r0
        l.append('xch a,r0')        
    elif x == 201:                              # xch a,r1
        l.append('xch a,r1')        
    elif x == 202:                              # xch a,r2 
        l.append('xch a,r2')        
    elif x == 203:                              # xch a,r3 
        l.append('xch a,r3')        
    elif x == 204:                              # xch a,r4 
        l.append('xch a,r4')        
    elif x == 205:                              # xch a,r5 
        l.append('xch a,r5')            
    elif x == 206:                              # xch a,r6 
        l.append('xch a,r6')        
    elif x == 207:                              # xch a,r7 
        l.append('xch a,r7')        
    elif x == 208:                              # pop direct_addr
        l.append('pop 0x')     
        l.append(read_next_byte())      
    elif x == 209:                              # acall page_addr
        l.append('acall ')      
        l.append(append_page_address())     
    elif x == 210:                              # setb bit_addr
        l.append('setb 0x')     
        l.append(read_next_byte())      
    elif x == 211:                              # setb carry 
        l.append('setb c')      
    elif x == 212:                              # da a 
        l.append('da a')        
    elif x == 213:                              # djnz direct_addr,rel_addr
        l.append('djnz 0x')     
        l.append(read_next_byte())      
        l.append(',0x')     
        l.append(append_rel_address())      
    elif x == 214:                              # xchd a,@r0
        l.append('xchd a,@r0')      
    elif x == 215:                              # xchd a,@r1
        l.append('xchd a,@r1')      
    elif x == 216:                              # djnz r0,rel_addr
        l.append('djnz r0,0x')      
        l.append(read_next_byte())      
    elif x == 217:                              # djnz r1,rel_addr
        l.append('djnz r1,0x')      
        l.append(read_next_byte())      
    elif x == 218:                              # djnz r2,rel_addr
        l.append('djnz r2,0x')      
        l.append(read_next_byte())      
    elif x == 219:                              # djnz r3,rel_addr
        l.append('djnz r3,0x')      
        l.append(read_next_byte())      
    elif x == 220:                              # djnz r4,rel_addr
        l.append('djnz r4,0x')      
        l.append(read_next_byte())      
    elif x == 221:                              # djnz r5,rel_addr
        l.append('djnz r5,0x')      
        l.append(read_next_byte())      
    elif x == 222:                              # djnz r6,rel_addr
        l.append('djnz r6,0x')      
        l.append(read_next_byte())      
    elif x == 223:                              # djnz r7,rel_addr
        l.append('djnz r7,0x')      
        l.append(read_next_byte())      
    elif x == 224:                              # movx a,@dptr 
        l.append('movx a,@dptr')        
    elif x == 225:                              # ajmp page_addr
        l.append('ajmp ')
        l.append(append_page_address())
    elif x == 226:                              # movx a,@r0 
        l.append('movx a,@r0')
    elif x == 227:                              # movx a,@r1
        l.append('movx a,@r1')              
    elif x == 228:                              # clr a 
        l.append('clr a')           
    elif x == 229:                              # mov a,direct
        l.append('mov a,0x')            
        l.append(read_next_byte())          
    elif x == 230:                              # mov a,@r0
        l.append('mov a,@r0')           
    elif x == 231:                              # mov a,@r1
        l.append('mov a,@r1')           
    elif x == 232:                              # mov a,r0 
        l.append('mov a,r0')            
    elif x == 233:                              # mov a,r1 
        l.append('mov a,r1')            
    elif x == 234:                              # mov a,r2 
        l.append('mov a,r2')            
    elif x == 235:                              # mov a,r3 
        l.append('mov a,r3')            
    elif x == 236:                              # mov a,r4 
        l.append('mov a,r4')            
    elif x == 237:                              # mov a,r5 
        l.append('mov a,r5')            
    elif x == 238:                              # mov a,r6
        l.append('mov a,r6')            
    elif x == 239:                              # mov a,r7 
        l.append('mov a,r7')            
    elif x == 240:                              # movx @dptr,a 
        l.append('movx @dptr,a')            
    elif x == 241:                              # acall page_addr
        l.append('acall ')
        l.append(append_page_address())
    elif x == 242:                              # movx @r0,a 
        l.append('movx @r0,a')  
    elif x == 243:                              # movx @r1,a 
        l.append('movx @r1,a')  
    elif x == 244:                              # cpl a
        l.append('cpl a')   
    elif x == 245:                              # mov direct,a 
        l.append('mov 0x')  
        l.append(read_next_byte())  
        l.append(',a')  
    elif x == 246:                              # mov @r0,a 
        l.append('mov @r0,a')
    elif x == 247:                              # mov @r1,a 
        l.append('mov @r1,a')               
    elif x == 248:                              # mov r0,a 
        l.append('mov r0,a')                
    elif x == 249:                              # mov r1,a 
        l.append('mov r1,a')                
    elif x == 250:                              # mov r2,a 
        l.append('mov r2,a')                
    elif x == 251:                              # mov r3,a
        l.append('mov r3,a')                
    elif x == 252:                              # mov r4,a 
        l.append('mov r4,a')                
    elif x == 253:                              # mov r5,a
        l.append('mov r5,a')                
    elif x == 254:                              # mov r6,a 
        l.append('mov r6,a')                
    elif x == 255:                              # mov r7,a
        l.append('mov r7,a')



fs = open('test.hex','r')
fd = open('test.asm','w')


for i in fs.readlines():
    convert_info(i)

    # for j in l:
    #     fd.write(str(j))             # write memonics into file
    #     fd.write(' ')
    # fd.write('\n')              # feed new line character 
  














# if __name__ == "__main__":
#     print ("------------------------This is Python Module---------------------- ")
#     print ("    Run pydesm file                                                 ")
#     print ("    [d]    for disassembling file                                   ")
#     print ("    [l]    for creating listing file                                ")
#     print ("    [a]    for aborting file list                                   ")
    