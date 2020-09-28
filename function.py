from final import *



#------------------------------------------------------------------------#
#                     Declare Global Variable                            #
#------------------------------------------------------------------------#

l = []                      # list to store one line instruction 
line_buffer = []            # list store hex line 
address = 0                 # current address of hex digit in decimal 
byte_count = 0              # no. of byte in a line 
record_type = 0             # intel hex file record type 
data = []                   # contain data nyte only 
i = 0                       # counter for next byte read 

#------------------------------------------------------------------------#
#         function:   (return next byte and increment byte count)        #
#------------------------------------------------------------------------#
def read_next_byte():
    global byte_count                   # number of bytes in line 
    global data                         # line of hex digit 

    byte_count -= 1                     # increment byte count to point next hex digit 
    i += 1
    x = data[(i*2):(i*2)+2]          
    return str(x)                       # return value at byte_count string type 


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
    reg = opcodes[x][index_no]
    return str(reg)                     # return string type 


#----------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------#
#              1 byte Instructions                    #
#-----------------------------------------------------#

def one_byte_instruction(x):
    l = opcodes[x][0]       # load opcode memonics into memonincs list 

#-----------------------------------------------------#
#              2 byte Instructions                    #
#-----------------------------------------------------#

def two_byte_instruction(x):
    byte = 0                         #store next byte of opcode
    byte = read_next_byte(x)         #read next byte data from line buffer (data[])

    # for immediate addressing mode 
    # read second byte and feed into l list 
    if opcodes[x][1] == immediate_data:     
        l = opcodes[x][0]
        l.append(byte)
    # for direct addressing mode 
    # read second byte and feed into l list 
    elif opcodes[x][1] == iram_address:
        l = opcodes[x][0] 
        l.append(byte)
        if opcodes[x][2] == accumulator:
            l.append('a')
        elif opcodes[x][2] == reg:
            l.append('r')
            l.append(reg_number(x))
        elif opcodes[x][2] == i_reg:
            l.append('@r')
            l.append(reg_number(x))
    
    # if destination is Accumulator 




#-----------------------------------------------------#
#              3 byte Instructions                    #
#-----------------------------------------------------#

def three_byte_instruction(x):
    pass
#---------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------#
#          function:   (convert hex digit into it's instruction)         #
#------------------------------------------------------------------------#    
def convert(x):
    l.clear()               # clear memonics list 
    
    # instruction is one byte (one byte instruction function call)
    if opcode_len[dec(x)] == 1:
        one_byte_instruction(x)
    # instruction is two byte (two byte instruction function call)
    elif opcode_len[dec(x)] == 2:
        two_byte_instruction(x)
    # instruction is three byte (three byte instruction function call)
    elif opcode_len[dec(x)] == 3:
        three_byte_instruction(x)
         





#------------------------------------------------------------------------#
#            function:   (give different filed in hex line)              #
#------------------------------------------------------------------------#

def convert_info(buffer):       # main starting point 
    global line_buffer 
    global address
    global byte_count
    global record_type
    global data
    global i


    # slicing of different intel hex file feilds (return into gloable varible)
    line_buffer = buffer
    address     = dec(buffer[3:7])                 #  address of line          
    byte_count  = dec(buffer[1:3])                 #  no. of bytes in line 
    record_type = dec(buffer[7:9])                 #  record type (intel specific)
    data        = buffer[9:2*byte_count]           #  data except chesksum 
    print(data)

#-----------------------Error in while loop-------------------------------byte count is not inc
    x = 0
    # for i in range(byte_count):
    while byte_count != 0:
        x = data[(i*2):(i*2)+2]         # one byte of line 
        convert(x)                      # transfer one digit
        i += 1                          # increment digit counter to point next digit  
        fd.write(str(l))
        fd.write('\n')



# opening files 
fs = open('test.hex','r')
fd = open('test.asm','w')

for j in fs.readlines():
    convert_info(j)

    
