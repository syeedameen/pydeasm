import table as tab
from string import *


#------------------------------------------------------------------------#
#                     Declare Global Variable                            #
#------------------------------------------------------------------------#

l           = []            # list to store one line instruction 
line_buffer = []            # list store hex line 
address     = 0             # current address of hex digit in decimal 
byte_count  = 0             # no. of byte in a line 
record_type = 0             # intel hex file record type 
data        = []            # data bytes in line (except add,byte_count,checksum,etc)
t           = 0             

#------------------------------------------------------------------------#
#         function:   (return next byte and increment byte count)        #
#------------------------------------------------------------------------#
def read_next_byte():
    global data                         # line of hex digit 
    global t

    x = data[(t*2):(t*2)+2]             # get next two hex digit(one byte) into x 
    t += 1                              # increment index counter to point next digit
    return str(x)                       # return string type 

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
#          function:   (return spacific value at opcode[i][j])           #
#------------------------------------------------------------------------#
def reg_number(opcode,index_no):
    x = dec(opcode)                     # convert decimal equivalent of hex 
    reg = tab.opcode[x][index_no]
    return str(reg)                     # return string type 


#------------------------------------------------------------------------#
#            function:   (give different filed in hex line)              #
#------------------------------------------------------------------------#

def convert_info(buffer):       # main starting point 
    global l
    global line_buffer 
    global address
    global byte_count
    global record_type
    global data
    global t


    # slicing of different intel hex file feilds (return into gloable varible)
    line_buffer = buffer
    address     = dec(buffer[3:7])       #  address of line          
    byte_count  = dec(buffer[1:3])       #  no. of bytes in line 
    record_type = dec(buffer[7:9])       #  record type (intel specific)
    data        = buffer[9:41]           #  data except chesksum 
    t           = 0                      # loop counter 

#-----------------------Error in while loop-------------------------------byte count is not inc
    x = 0 # local temp varible 

    while t <= byte_count:              # repeat until counter <= byte_count (no. of digit each line)
        x = data[(t*2):(t*2)+2]         # one byte of line 
        t += 1                          # increment digit counter to point next digit 
        convert(x)                      # transfer one digit     




#------------------------------------------------------------------------#
#          function:   (convert hex digit into it's instruction)         #
#------------------------------------------------------------------------#    
def convert(opcode):
    x = dec(opcode)         # opcode decimal equivalent in x variable 
    global l                # list that store instruction of it's instruction                

    l.clear()               # clear list before used 
    relative   = 0          # store relative address 
    byte       = 0          # fetch rext byte of data


#--------------------------------------------------------------#
#                Handling ADD Instruction                      # 
#--------------------------------------------------------------#
    if tab.opcode[x][0] == 'add':
        l.append('add ')
        # fetch First operand 
        if tab.opcode[x][1] == tab.accumulator:             # first operand or destination register is accumulator 
            l.append('a,')
            # fetch Second operand 
            if tab.opcode[x][2] == tab.reg:                 # for register addressing mode  (ADD A,Rn)
                l.append('r')
                l.append(reg_number(opcode,3))         
            elif tab.opcode[x][2] == tab.i_reg:             # for register indirect addressing mode  (ADD A,@Ri)
                l.append('@r')
                l.append(reg_number(opcode,3))
            elif tab.opcode[x][2] == tab.iram_address:      # for direct addressing mode    (ADD A,direct_address)
                byte = read_next_byte()
                l.append('0x')    # because hex digit 
                l.append(byte)    # append byte data 
            elif tab.opcode[x][2] == tab.immediate_data:    # for immediate addressing mode (ADD A,#data)
                byte = read_next_byte()
                l.append('#0x')     # immediate sign                          
                l.append(byte)    # append byte data


#---------------------------------------------------------------#
#                Handling ADDC Instruction                      #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'addc':
        l.append('addc ')
        # fetch First operand 
        if tab.opcode[x][1] == tab.accumulator:             # first operand or destination registe is accumulator 
            l.append('a')
            # fetch Second operand 
            if tab.opcode[x][2] == tab.reg:                 # for register addressing mode      (ADDC A,Rn)
                l.append('r')
                l.append(reg_number(opcode,3))
            elif tab.opcode[x][2] == tab.i_reg:             # for register indirect addressing mode  (ADDC A,@Ri)
                l.append('@r')
                l.append(reg_number(opcode,3))
            elif tab.opcode[x][2] == tab.immediate_data:    # for immediate addressing mode         (ADDC A,#data)
                byte = read_next_byte()
                l.append('#0x')
                l.append(byte)
            elif tab.opcode[x][2] == tab.iram_address:      # for direct addressing mode        (ADDC A,direct_address)
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)

#---------------------------------------------------------------#
#                Handling SUBB Instruction                      #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'subb':
        l.append('subb ')
        # fetch first operand 
        if tab.opcode[x][1] == tab.accumulator:             # first operand or destination register is accumulator 
            l.append('a,')
            # fetch second operand 
            if tab.opcode[x][2] == tab.reg:                 # for register addressing mode      (SUBB A,Rn) 
                l.append('r')
                l.append(reg_number(opcode,3))
            elif tab.opcode[x][2] == tab.i_reg:             # for register indirect addressing mode     (SUBB A,@Ri)
                l.append('@r')
                l.append(reg_number(opcode,3))
            elif tab.opcode[x][2] == tab.immediate_data:    # for immediate addressing mode             (SUBB A,#data)
                byte = read_next_byte()
                l.append('#0x')
                l.append(byte)
            elif tab.opcode[x][2] == tab.iram_address:      # for direct addressing mode            (SUBB A,direct_address)
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)
        
#---------------------------------------------------------------#
#                 Handling INC Instruction                      #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'inc':                             
        l.append('inc ')
        # fetch first operand 
        if tab.opcode[x][1] == tab.accumulator:             # for implied addressing mode       (INC A)
            l.append('a')
        elif tab.opcode[x][1] == tab.reg:                   # for register addressing mode      (INC Rn)
            l.append('r')
            l.append(reg_number(opcode,2))
        elif tab.opcode[x][1] == tab.i_reg:                 # for register indirect addressing mode     (INC @Ri)
            l.append('@r')
            l.append(reg_number(opcode,2))             
        elif tab.opcode[x][1] == tab.iram_address:          # for direct addressing mode        (INC direct_address)
            byte = read_next_byte()
            l.append('0x')
            l.append(byte)
        elif tab.opcode[x][1] == tab.dptr:                  # for increment data pointer        (INC DPTR)
            l.append('dptr')


#---------------------------------------------------------------#
#                Handling DEC Instruction                       #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'dec':
        l.append('dec ')
        # fetch first operand 
        if tab.opcode[x][1] == tab.accumulator:             # for implied addressing mode       (DEC A)
            l.append('a')
        elif tab.opcode[x][1] == tab.reg:                   # for register addressing mode      (DEC Rn)
            l.append('r')
            l.append(reg_number(opcode,2))
        elif tab.opcode[x][1] == tab.i_reg:                 # for indirect addressing mode      (DEC @Ri)
            l.append('@r')
            l.append(reg_number(opcode,2))
        elif tab.opcode[x][1] == tab.iram_address:          # for direct addressing mode        (DEC direct_address)
            byte = read_next_byte()
            l.append('0x')
            l.append(byte)
                

#---------------------------------------------------------------#
#                Handling MUL Instruction                       #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'mul':
        l.append('mul ')
        l.append('ab')

#---------------------------------------------------------------#
#                Handling DIV Instruction                       #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'div':
        l.append('div ')
        l.append('ab')
    
#---------------------------------------------------------------#
#                Handling DA A Instruction                      #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'da':
        l.append('da ')
        l.append('a')


#---------------------------------------------------------------#
#                Handling ANL Instruction                       #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'anl':
        l.append('anl ')
        # fetch first operand 
        if tab.opcode[x][1] == tab.accumulator:                 # if first operand is Accumulator  
            l.append('a,')
            # fetch second operand 
            if tab.opcode[x][2] == tab.reg:                     # for register addressing mode  (ANL A,Rn)
                l.append('r')
                l.append(reg_number(opcode,3))
            elif tab.opcode[x][2] == tab.i_reg:                 # for register indirect addressing mode (ANL A,@Ri)
                l.append('@r')
                l.append(reg_number(opcode,3))
            elif tab.opcode[x][2] == tab.immediate_data:        # for immediate addressing mode (ANL A,#data)
                byte = read_next_byte()
                l.append('#0x')
                l.append(byte)
            else:                                               # for direct addressing mode is all condition fail (ANL A,direct_address)
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)
        # if first operand is Direct Address
        elif tab.opcode[x][1] == tab.iram_address:
            if tab.opcode[x][2] == tab.accumulator:             # for (ANL direct,a)
               byte = read_next_byte()
               l.append('0x')
               l.append(byte)
               l.append(',a')   
            else:                                               # for (ANL direct,#data)
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)
                l.append(',#0x')
                byte = read_next_byte() # read immediate data 
                l.append(byte)
        # if first operand is carry bit 
        else:
            l.append('c,')
            if tab.opcode[x][2] == tab.bit_address:             # for (ANL C,bit_address)
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)
            else:                                               # for (ANL C,~bit_address)          {after operation complement bit}
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)
        
#---------------------------------------------------------------#
#                 Handling OR Instruction                       #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'orl':
        l.append('orl ')
        # fetch first operand 
        if tab.opcode[x][1] == tab.accumulator:                 # if first operand is accumulator 
            l.append('a,')
            # fetch Second operand 
            if tab.opcode[x][2] == tab.reg:                     # for register addressing mode (ORL A,Rn)
                l.append('r')
                l.append(reg_number(opcode,3))
            elif tab.opcode[x][2] == tab.i_reg:                 # for register indirect addressing mode (ORL A,@Ri)
                l.append('@r')
                l.append(reg_number(opcode,3))
            elif tab.opcode[x][2] == tab.immediate_data:        # for immediate addressing mode (ORL A,#data)
                byte = read_next_byte()
                l.append('#0x')
                l.append(byte)
            else:                                               # for direct addressing mode (ORL A,direct_address)
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)
        # if first operand is Direct Address
        elif tab.opcode[x][1] == tab.iram_address:
            if tab.opcode[x][2] == tab.accumulator:             # for (ORL direct,A)
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)
                l.append(',a')
            else:                                               # for (ORL direct,data)
                byte = read_next_byte()
                l.append('0x')          # append direct address 
                l.append(byte)
                byte = read_next_byte() # read immediate data 
                l.append(',#0x')
                l.append(byte)
        # if first operand is Carray 
        else:
            if tab.opcode[x][2] == tab.bit_address:             # for (ORL C,bit_address)
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)
            else:                                               # for (ORL C,!bit_address)          {after operation complement bit}
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)

#---------------------------------------------------------------#
#                Handling XRL Instruction                       #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'xrl':
        l.append('xrl ')
        # fetch first operand 
        if  tab.opcode[x][1] == tab.accumulator:                     # if first operand is accumulator 
            l.append('a,')
            # fetch second operand  
            if  tab.opcode[x][2] == tab.reg:                         # for register addressing mode (XRL A,Rn)
                l.append('r')
                l.append(reg_number(opcode,3))
            elif  tab.opcode[x][2] == tab.i_reg:                     # for register indirect addressing mode (XRL A,@Ri)
                l.append('@r')
                l.append(reg_number(opcode,3))
            elif  tab.opcode[x][2] == tab.immediate_data:            # for immediate addressing mode (XRL A,#data)
                byte = read_next_byte()
                l.append('#0x')
                l.append(byte)
            else:                                                    # for direct addressing mode (XRL A,direct_address)
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)    
        else:                                                        # if first operand is not accumulator 
            if tab.opcode[x][2] == tab.accumulator:
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)
                l.append(',a')
            else:
                byte = read_next_byte() # read direct address 
                l.append('0x')
                l.append(byte)
                byte = read_next_byte() # read immediate data
                l.append(',#0x')
                l.append(byte)

#---------------------------------------------------------------#
#                Handling CLR Instruction                       #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'clr':
        l.append('cpl ')
        # fetch operand (accumulator, carry, bit_address)
        if tab.opcode[x][1] == tab.accumulator:                     # clear accumulator instruction (CLR A) 
            l.append('a')
        elif tab.opcode[x][1] == tab.carry:                         # clear carry flag instruction (CLR C)
            l.append('c')
        else:                                                       # clear bit                    (CLR bit_address)
            byte = read_next_byte()  # read bit_address
            l.append('0x')
            l.append(byte)
            
#---------------------------------------------------------------#
#                Handling CPL Instruction                       #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'cpl':
        l.append('cpl ')
        # fetch operand (accumulator, carry, bit_address)
        if tab.opcode[x][1] == tab.accumulator:                     # complement accumulator instruction (CPL A)
            l.append('a')                                       
        elif tab.opcode[x][1] == tab.carry:                         # complement carry flag (CPL C)
            l.append('c')                                       
        else:                                                       # complement bit        (CPL bit_address)
            byte = read_next_byte() # read bit_address
            l.append('0x')
            l.append(byte)
    
#---------------------------------------------------------------#
#                 Handling ROTATE Instruction                   #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'rl':                                  # for (RL A)
        l.append('rl a')
    elif tab.opcode[x][0] == 'rlc':                                 # for (RLC A)
        l.append('rlc a')
    elif tab.opcode[x][0] == 'rr':                                  # for (RR A)
        l.append('rr a')
    elif tab.opcode[x][0] == 'rrc':
        l.append('rrc a')                                           # for (RRC A)
    
#---------------------------------------------------------------#
#                 Handling SWPA Instruction                     #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'swap':
        l.append('swap a')

#---------------------------------------------------------------#
#                   Handling MOV Instruction                    #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'mov':
        l.append('mov ')
        # fetch First operand (accumulator)
        if tab.opcode[x][1] == tab.accumulator:                     # if first operand is accumulator             
            l.append('a,')
            if tab.opcode[x][2] == tab.reg:                         # register addressing mode (MOV A,Rn)  
                l.append('r')
                l.append(reg_number(opcode,3))
            elif tab.opcode[x][2] == tab.i_reg:                     # register indirect addressing mode (MOV A,@Ri)
                l.append('@r')
                l.append(reg_number(opcode,3))
            elif tab.opcode[x][2] == tab.immediate_data:            # for immediate addressing mode (MOV A,#data)
                byte = read_next_byte() # read immediate data 
                l.append('#0x')
                l.append(byte)
            else:                                                   # for direct addressing mode (MOV A,direct_address)                                                                                 
                byte = read_next_byte() # read direct_address
                l.append('0x')
                l.append(byte)
                
        # fetch first operand (Rn)
        elif tab.opcode[x][1] == tab.reg:
            l.append('r')
            l.append(reg_number(opcode,3))
            l.append(',')           # create space b/w operands
            if tab.opcode[x][2] == tab.accumulator:                 # second operand accumulator (MOV Rn,A)
                l.append('a')
            elif tab.opcode[x][2] == tab.immediate_data:            # second operand immediate data (MOV Rn,#data)
                byte = read_next_byte()
                l.append('#0x')
                l.append(byte)
            else:                                                   # second operand direct_address (MOV Rn,direct_address)
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)
        # fetch first operand (Direct_address)
        elif tab.opcode[x][1] == tab.iram_address:                  
            byte = read_next_byte()
            l.append('0x')
            l.append(byte)
            l.append(',')
            if tab.opcode[x][2] == tab.accumulator:                 # second operand accumulator (MOV direct,A)
                l.append('a')
            elif tab.opcode[x][2] == tab.reg:                       # second operand reg    (MOV direct,Rn)
                l.append('r')
                l.append(reg_number(opcode,3))  
            elif tab.opcode[x][2] == tab.iram_address:              # second operand direct_address  (MOV direct,direct)
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)
            elif tab.opcode[x][2] == tab.i_reg:                     # second operand @reg   (MOV direct,Ri)
                l.append('@r')
                l.append(reg_number(opcode,3))
            else:                                                   # second operand immediate data (MOV direct,#data)
                byte = read_next_byte()
                l.append('#0x')
                l.append(byte)
        # fetch first operand (@Ri)
        elif tab.opcode[x][1] == tab.i_reg:
            l.append('@r')
            l.append(reg_number(opcode,3))
            l.append(',')
            if tab.opcode[x][2] == tab.accumulator:                 # second operand accumulator (MOV @Ri,A)
                l.append('a')
            elif tab.opcode[x][2] == tab.iram_address:              # second operand direct_address (MOV @Ri,direct_address)
                byte = read_next_byte()
                l.append('0x')
                l.append(byte)
            elif tab.opcode[x][2] == tab.immediate_data:            # second operand immediate data (MOV @Ri,#data)
                byte = read_next_byte()
                l.append('#0x')
                l.append(byte)
        # fetch first operand (carry)
        elif tab.opcode[x][1] == tab.carry:                         # for (MOV C,bit_address)
            l.append('c,')
            byte = read_next_byte()
            l.append('0x')
            l.append(byte)
        
        # fetch first operand (bit_address)
        else:                                                       # for (MOV bit_address,C)
            byte = read_next_byte()
            l.append('0x')
            l.append(byte)
            l.append(',c')
        

#---------------------------------------------------------------#
#                  Handling MOVC Instruction                    #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'movc':
        l.append('movc a,')
        if tab.opcode[x][2] == tab.i_acc_pl_dptr:                   # for MOVC A,@A+DPTR
            l.append('@a+dptr')
        else:                                                       # for MOVC A,@A+PC
            l.append('@a+pc')           



#---------------------------------------------------------------#
#                  Handling MOVX Instruction                    #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'movx':
        l.append('movx ')
        # fetch first operand   (Accumulator)
        if tab.opcode[x][1] == tab.accumulator:                     # if first operand is accumulator 
            l.append('a,')
            # fetch second operand  (@Ri, @DPTR)
            if tab.opcode[x][2] == tab.i_reg:                       # for indirect register (MOV A,@Ri)
                l.append('@r')
                l.append(reg_number(opcode,3))
            else:                                                   # for data pointer (MOV A,@DPTR)
                l.append('@dptr')
        elif tab.opcode[x][1] == tab.i_reg:                         # if first operand is @Ri
            l.append('@r')      
            l.append(reg_number(opcode,3))                          # for (MOV @Ri,A)
            l.append(',a')
        else:                                                       # for (MOV @DPTR,A)
            l.append('@dptr,a')


#---------------------------------------------------------------#
#                Handling PUSH/POP Instruction                  #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'pop':                                 # pop direct_address
        byte = read_next_byte()
        l.append('0x')
        l.append(byte)
    elif tab.opcode[x][0] == 'push':                                # push direct_address
        byte = read_next_byte()
        l.append('0x')
        l.append(byte)

#---------------------------------------------------------------#
#                  Handling XCH Instruction                     #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'xch':
        l.append('xch a,')  # first operand is always accumulator  

        # fetch second operand 
        if tab.opcode[x][2] == tab.reg:                             # second operand reg.   (XCH A,Rn)
            l.append('r')
            l.append(reg_number(opcode,3))
        elif tab.opcode[x][2] == tab.i_reg:                         # second operand reg. pointer (XCH A,@Ri)
            l.append('@r')
            l.append(reg_number(opcode,3))
        else:                                                       # second operand direct_address (XCH A,direct_address)
            byte = read_next_byte()
            l.append('0x')
            l.append(byte) 

#---------------------------------------------------------------#
#                 Handling XCHG Instruction                     #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'xchd':
        l.append('xchd a,@r')
        l.append(reg_number(opcode,3))

#---------------------------------------------------------------#
#                  Handling SETB Instruction                    #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'setb':
        l.append('setb ')
        # fetch first operand 
        if tab.opcode[x][1] == tab.carry:                           # if first operand is carry 
            l.append('c')
        else:                                                       # if first operand is bit_address
            byte = read_next_byte()
            l.append('0x')
            l.append(byte)

#---------------------------------------------------------------#
#              Handling NOP,RET,RETI Instruction                #
#---------------------------------------------------------------#
    elif tab.opcode[x][0] == 'nop':
        l.append('nop ') 
    
    elif tab.opcode[x][0] == 'ret':
        l.append('ret ')

    elif tab.opcode[x][0] == 'reti':
        l.append('reti ')

#---------------------------------------------------------------#
#                  Handling SETB Instruction                    #
#---------------------------------------------------------------#



fs = open('test.hex','r')
fd = open('test.asm','w')


for i in fs.readlines(): 
    convert_info(i)

    for j in l:
        fd.write(j)
    fd.write('\n')

