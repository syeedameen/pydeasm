#                   file 2 convert hex digit to memonics and symbol table definition 


from function import *


#-------------------------------------------------------------------------------------#
#                       Gloabal Variable Define Here                                  #
#-------------------------------------------------------------------------------------#

line_buffer     = []            #hex line
address         = 0             #base address of hex line 
byte_count      = 0             #number of byte digit in hex line 
record_type     = 0             #intel hex file return type 
l               = []            #list contain line memonics or lable 
data            = []            #list contain only data byte in line 
count           = 0             #current pointing digit in hex line (starting from 0)


#------------------------------------------------------------------------#
#                   function:   (READ NEXT BYTE)                         #
#   1.  Return String type byte                                          #
#------------------------------------------------------------------------#
def read_next_byte():
    global count                        # no. of byte data in hex line  
    global data                         # line of hex digit 

    count += 1                          # increment byte count to point next hex digit 
    x = line_buffer[count]          
    return str(x)                       # return value at byte_count string type 


#------------------------------------------------------------------------#
#            function:   (give different field in hex line)              #
#------------------------------------------------------------------------#

def convert_info(buffer):                                 
    global line_buffer                   
    global address                      
    global byte_count
    global record_type
    global data
    global count


    # slicing of different intel hex file feilds (return into gloable varible)
    line_buffer = buffer
    address     = dec(buffer[3:7])          #  address of line          
    byte_count  = dec(buffer[1:3])          #  no. of bytes in line 
    record_type = dec(buffer[7:9])          #  record type (intel specific)
    data        = buffer[9:2*byte_count]    #  data except chesksum 




#------------------------------------------------------------------------#
#               Convert hex digit to decimal equivalent                  #
#------------------------------------------------------------------------#
def convert():
    pass 

















if __name__ == "__main__":
    print(" This is python module ")
    print(" Run pydeasm.py file ")