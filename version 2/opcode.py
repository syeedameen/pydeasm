# #---------------------------------------------------#
# #            opcodes Management file       FILE 0   #
# #---------------------------------------------------#

# # addressing mode define here 
# none            = 0
# immediate_addr  = 1 
# direct_addr     = 2
# reg_addr        = 3 
# i_reg_addr      = 4
# relative_addr   = 5 
# absolute_addr   = 6
# long_addr       = 7
# index_addr      = 8 
# implied_addr    = 9
# flag_addr       = 10 
# # destination define here 
# accumulator_dest    = 11 
# direct_dest         = 12
# i_reg_dest          = 13
# dptr_dest           = 14

# _reg_number = []
# _opcode_len = []


# # opcode addressing mode definition 
# op_addr_mode = {
#     'add':[immediate_addr,reg_addr,direct_addr,i_reg_addr,],
#     'addc':[reg_addr,direct_addr,i_reg_addr,immediate_addr],
#     'subb':[reg_addr,direct_addr,i_reg_addr,immediate_addr],
#     'inc':[reg_addr,direct_addr,implied_addr,i_reg_addr],
#     'dec':[reg_addr,direct_addr,implied_addr,i_reg_addr],
#     'mul':[none],
#     'div':[none],
#     'da':[implied_addr],
#     'anl':{
#         accumulator_dest:[reg_addr,direct_addr,i_reg_addr,immediate_addr],
#         direct_dest:[implied_addr,immediate_addr]
#     },
#     'orl':{
#         accumulator_dest:[reg_addr,direct_addr,immediate_addr,i_reg_addr],
#         direct_dest:[implied_addr,immediate_addr]    
#     },
#     'xrl':{
#         accumulator_dest:[reg_addr,direct_addr,immediate_addr,i_reg_addr],
#         direct_dest:[implied_addr,immediate_addr]
#     },
#     'clr':[implied_addr,direct_addr,flag_addr],
#     'cpl':[implied_addr,direct_addr,flag_addr],
#     'mov':[],
#     'movx':[],
#     'movc':[],
#     'pop':[],
#     'push':[],
#     'xch':[],
#     'xchd':[],
#     'cjne':[],
#     'djnz':[],
#     'nop':[],
#     'ret':[],
#     'reti':[],
#     'setb':[],
#     'lcall':[],
#     'acall':[],
#     'ljmp':[],
#     'ajmp':[],
#     'sjmp':[],
#     'jmp':[],
# # conditional jump instructions
#     'jz':[],
#     'jnz':[],
#     'jc':[],
#     'jnc':[],
#     'jb':[],
#     'jnb':[],
#     'jnc':[],
# }


# # register number definition 
# _reg_number = [
# ]


# # opcode length definition 
# _opcode_len = []











#   Author:     SYEED MOHD AMEEN                                    Date:   19-09-2020
#   Email:      ameensyeed2@gmail.com
#   License:    GPLv3



#---------------------------------------------------------------------------------------------------------#
#                                         8051 Opcode Table                                               #
#---------------------------------------------------------------------------------------------------------#


accumulator         = 0
reg                 = 1
i_reg               = 2 
page_address        = 3 
address_16_bit      = 4 
data_16_bit         = 5 
bit_address         = 7 
relative_address    = 8 
iram_address        = 9 
carry               = 10 
immediate_data      = 11 
i_acc_pl_dptr       = 12 
i_acc_pl_pc         = 13
i_dptr              = 14
Breg                = 15 
dptr                = 16 
comp_bit_address    = 17 



opcodes = {
        0:('nop',       0,                               0,                             0,                              0),
        1:('ajmp',      page_address,                    0,                             0,                              0),
        2:('ljmp',      address_16_bit,                  0,                             0,                              0),
        3:('rr',        accumulator,                     0,                             0,                              0),
        4:('inc',       accumulator,                     0,                             0,                              0),
        5:('inc',       iram_address,                    0,                             0,                              0),
        6:('inc',       i_reg,                           0,                             0,                              0),
        7:('inc',       i_reg,                           1,                             0,                              0),
        8:('inc',       reg,                             0,                             0,                              0),
        9:('inc',       reg,                             1,                             0,                              0),
        10:('inc',      reg,                             2,                             0,                              0),

        11:('inc',      reg,                             3,                             0,                              0),
        12:('inc',      reg,                             4,                             0,                              0),
        13:('inc',      reg,                             5,                             0,                              0),
        14:('inc',      reg,                             6,                             0,                              0),
        15:('inc',      reg,                             7,                             0,                              0),
        16:('jbc',      bit_address,                     relative_address,              0,                              0),
        17:('acall',    page_address,                    0,                             0,                              0),
        18:('lcall',    address_16_bit,                  0,                             0,                              0),
        19:('rrc',      accumulator,                     0,                             0,                              0),
        20:('dec',      accumulator,                     0,                             0,                              0),

        21:('dec',      iram_address,                    0,                             0,                              0),
        22:('dec',      i_reg,                           0,                             0,                              0),
        23:('dec',      i_reg,                           1,                             0,                              0),
        24:('dec',      reg,                             0,                             0,                              0),
        25:('dec',      reg,                             1,                             0,                              0),
        26:('dec',      reg,                             2,                             0,                              0),
        27:('dec',      reg,                             3,                             0,                              0),
        28:('dec',      reg,                             4,                             0,                              0),
        29:('dec',      reg,                             5,                             0,                              0),
        30:('dec',      reg,                             6,                             0,                              0),

        31:('dec',      reg,                             7,                             0,                              0),
        32:('jb',       bit_address,                     relative_address,              0,                              0),
        33:('ajmp',     page_address,                    0,                             0,                              0),
        34:('ret',                                       0,                             0,                              0),
        35:('rl',       accumulator,                     0,                             0,                              0),
        36:('add',      accumulator,                     immediate_data,                0,                              0),
        37:('add',      accumulator,                     iram_address,                  0,                              0),
        38:('add',      accumulator,                     i_reg,                         0,                              0),
        39:('add',      accumulator,                     i_reg,                         1,                              0),
        40:('add',      accumulator,                     reg,                           0,                              0),

        41:('add',      accumulator,                     reg,                           1,                              0),
        42:('add',      accumulator,                     reg,                           2,                              0),
        43:('add',      accumulator,                     reg,                           3,                              0),
        44:('add',      accumulator,                     reg,                           4,                              0),
        45:('add',      accumulator,                     reg,                           5,                              0),
        46:('add',      accumulator,                     reg,                           6,                              0),
        47:('add',      accumulator,                     reg,                           7,                              0),
        48:('jnb',      bit_address,                     relative_address,              0,                              0),
        49:('acall',    page_address,                    0,                             0,                              0),
        50:('reti',     0,                               0,                             0,                              0),

        51:('rcl',      accumulator,                     0,                             0,                              0),
        52:('addc',     accumulator,                     immediate_data,                0,                              0),
        53:('addc',     accumulator,                     iram_address,                  0,                              0),
        54:('adcc',     accumulator,                     i_reg,                         0,                              0),
        55:('adcc',     accumulator,                     i_reg,                         1,                              0),
        56:('adcc',     accumulator,                     reg,                           0,                              0),
        57:('adcc',     accumulator,                     reg,                           1,                              0),
        58:('adcc',     accumulator,                     reg,                           2,                              0),
        59:('adcc',     accumulator,                     reg,                           3,                              0),
        60:('adcc',     accumulator,                     reg,                           4,                              0),

        61:('adcc',     accumulator,                     reg,                           5,                              0),
        62:('adcc',     accumulator,                     reg,                           6,                              0),
        63:('adcc',     accumulator,                     reg,                           7,                              0),
        64:('jc',       relative_address,                0,                             0,                              0),
        65:('ajmp',     page_address,                    0,                             0,                              0),
        66:('orl',      iram_address,                    accumulator,                   0,                              0),
        67:('orl',      iram_address,                    immediate_data,                0,                              0),
        68:('orl',      accumulator,                     immediate_data,                0,                              0),
        69:('orl',      accumulator,                     iram_address,                  0,                              0),
        70:('orl',      accumulator,                     i_reg,                         0,                              0),

        71:('orl',      accumulator,                     i_reg,                         1,                              0),
        72:('orl',      accumulator,                     reg,                           0,                              0),
        73:('orl',      accumulator,                     reg,                           1,                              0),
        74:('orl',      accumulator,                     reg,                           2,                              0),
        75:('orl',      accumulator,                     reg,                           3,                              0),
        76:('orl',      accumulator,                     reg,                           4,                              0),
        77:('orl',      accumulator,                     reg,                           5,                              0),
        78:('orl',      accumulator,                     reg,                           6,                              0),
        79:('orl',      accumulator,                     reg,                           7,                              0),
        80:('jnc',      relative_address,                0,                             0,                              0),

        81:('acall',    page_address,                    0,                             0,                              0),
        82:('anl',      iram_address,                    accumulator,                   0,                              0),
        83:('anl',      iram_address,                    immediate_data,                0,                              0),
        84:('anl',      accumulator,                     immediate_data,                0,                              0),
        85:('anl',      accumulator,                     iram_address,                  0,                              0),
        86:('anl',      accumulator,                     i_reg,                         0,                              0),
        87:('anl',      accumulator,                     i_reg,                         1,                              0),
        88:('anl',      accumulator,                     reg,                           0,                              0),
        89:('anl',      accumulator,                     reg,                           1,                              0),
        90:('anl',      accumulator,                     reg,                           2,                              0),

        91:('anl',      accumulator,                     reg,                           3,                              0),
        92:('anl',      accumulator,                     reg,                           4,                              0),
        93:('anl',      accumulator,                     reg,                           5,                              0),
        94:('anl',      accumulator,                     reg,                           6,                              0),
        95:('anl',      accumulator,                     reg,                           7,                              0),
        96:('jz',       relative_address,                0,                             0,                              0),
        97:('ajmp',     page_address,                    0,                             0,                              0),
        98:('xrl',      iram_address,                    accumulator,                   0,                              0),
        99:('xrl',      iram_address,                    immediate_data,                0,                              0),
        100:('xrl',     accumulator,                     immediate_data,                0,                              0),

        101:('xrl',     accumulator,                     iram_address,                  0,                              0),
        102:('xrl',     accumulator,                     i_reg,                         0,                              0),
        103:('xrl',     accumulator,                     i_reg,                         1,                              0),
        104:('xrl',     accumulator,                     reg,                           0,                              0), 
        105:('xrl',     accumulator,                     reg,                           1,                              0),
        106:('xrl',     accumulator,                     reg,                           2,                              0),
        107:('xrl',     accumulator,                     reg,                           3,                              0),
        108:('xrl',     accumulator,                     reg,                           4,                              0),
        109:('xrl',     accumulator,                     reg,                           5,                              0),
        110:('xrl',     accumulator,                     reg,                           6,                              0),

        111:('xrl',     accumulator,                     reg,                           7,                              0),
        112:('jnz',     relative_address,                0,                             0,                              0),
        113:('acall',   page_address,                    0,                             0,                              0),
        114:('orl',     carry,                           bit_address,                   0,                              0),
        115:('jmp',     i_acc_pl_dptr,                   0,                             0,                              0),
        116:('mov',     accumulator,                     immediate_data,                0,                              0),
        117:('mov',     iram_address,                    immediate_data,                0,                              0),
        118:('mov',     i_reg,                           immediate_data,                0,                              0),
        119:('mov',     i_reg,                           immediate_data,                1,                              0),
        120:('mov',     reg,                             immediate_data,                0,                              0),

        121:('mov',     reg,                             immediate_data,                1,                              0),
        122:('mov',     reg,                             immediate_data,                2,                              0),
        123:('mov',     reg,                             immediate_data,                3,                              0),
        124:('mov',     reg,                             immediate_data,                4,                              0),
        125:('mov',     reg,                             immediate_data,                5,                              0),
        126:('mov',     reg,                             immediate_data,                6,                              0),
        127:('mov',     reg,                             immediate_data,                7,                              0),
        128:('sjmp',    relative_address,                0,                             0,                              0),
        129:('ajmp',    page_address,                    0,                             0,                              0),
        130:('anl',     carry,                           bit_address,                   0,                              0),

        131:('movc',    accumulator,                     i_acc_pl_pc,                   0,                              0),
        132:('div',     accumulator,                     Breg,                          0,                              0),
        133:('mov',     iram_address,                    iram_address,                  0,                              0),
        134:('mov',     iram_address,                    i_reg,                         0,                              0),
        135:('mov',     iram_address,                    i_reg,                         1,                              0),
        136:('mov',     iram_address,                    reg,                           0,                              0),
        137:('mov',     iram_address,                    reg,                           1,                              0),
        138:('mov',     iram_address,                    reg,                           2,                              0),
        139:('mov',     iram_address,                    reg,                           3,                              0),

        140:('mov',     iram_address,                    reg,                           4,                              0),
        141:('mov',     iram_address,                    reg,                           5,                              0),
        142:('mov',     iram_address,                    reg,                           6,                              0),
        143:('mov',     iram_address,                    reg,                           7,                              0),
        144:('mov',     dptr,                            data_16_bit,                   0,                              0),
        145:('acall',   page_address,                    0,                             0,                              0),
        146:('mov',     bit_address,                     carry,                         0,                              0),
        147:('movc',    accumulator,                     i_acc_pl_dptr,                 0,                              0),
        148:('subb',    accumulator,                     immediate_data,                0,                              0),
        149:('subb',    accumulator,                     iram_address,                  0,                              0),
        150:('subb',    accumulator,                     i_reg,                         0,                              0),
        151:('subb',    accumulator,                     i_reg,                         1,                              0),
        152:('subb',    accumulator,                     reg,                           0,                              0),
        153:('subb',    accumulator,                     reg,                           1,                              0),
        154:('subb',    accumulator,                     reg,                           2,                              0),
        155:('subb',    accumulator,                     reg,                           3,                              0),
        156:('subb',    accumulator,                     reg,                           4,                              0),
        157:('subb',    accumulator,                     reg,                           5,                              0),
        158:('subb',    accumulator,                     reg,                           6,                              0),
        159:('subb',    accumulator,                     reg,                           7,                              0),
        160:('orl',     carry,                           bit_address,                   0,                              0),

        161:('ajmp',    page_address,                    0,                             0,                              0),
        162:('mov',     carry,                           bit_address,                   0,                              0),
        163:('inc',     dptr,                            0,                             0,                              0),
        164:('mul',     accumulator,                     Breg,                          0,                              0),
        165:('reserved',0,0,0),                                                 
        166:('mov',     i_reg,                           iram_address,                  0,                              0),
        167:('mov',     i_reg,                           iram_address,                  1,                              0),
        168:('mov',     reg,                             iram_address,                  0,                              0),
        169:('mov',     reg,                             iram_address,                  1,                              0),
        170:('mov',     reg,                             iram_address,                  2,                              0),

        171:('mov',     reg,                             iram_address,                  3,                              0),
        172:('mov',     reg,                             iram_address,                  4,                              0),
        173:('mov',     reg,                             iram_address,                  5,                              0),
        174:('mov',     reg,                             iram_address,                  6,                              0),
        175:('mov',     reg,                             iram_address,                  7,                              0),
        176:('anl',     carry,                           comp_bit_address,                   0,                              0),
        177:('acall',   page_address,                    0,                             0,                              0),
        178:('cpl',     bit_address,                     0,                             0,                              0),
        179:('cpl',     carry,                           0,                             0,                              0),
        180:('cjne',    accumulator,                     immediate_data,                relative_address,               0),

        181:('cjne',    accumulator,                     iram_address,                  relative_address,               0),
        182:('cjne',    i_reg,                           immediate_data,                relative_address,               0),
        183:('cjne',    i_reg,                           immediate_data,                relative_address,               1),
        184:('cjne',    reg,                             immediate_data,                relative_address,               0),
        185:('cjne',    reg,                             immediate_data,                relative_address,               1),
        186:('cjne',    reg,                             immediate_data,                relative_address,               2),
        187:('cjne',    reg,                             immediate_data,                relative_address,               3),
        188:('cjne',    reg,                             immediate_data,                relative_address,               4),
        189:('cjne',    reg,                             immediate_data,                relative_address,               5),
        190:('cjne',    reg,                             immediate_data,                relative_address,               6),
        191:('cjne',    reg,                             immediate_data,                relative_address,               7),
        192:('push',    iram_address,                    0,                             0,                              0),
        193:('ajmp',    page_address,                    0,                             0,                              0),
        194:('clr',     bit_address,                     0,                             0,                              0),
        195:('clr',     carry,                           0,                             0,                              0),
        196:('swap',    accumulator,                     0,                             0,                              0),
        197:('xch',     accumulator,                     iram_address,                  0,                              0),
        198:('xch',     accumulator,                     i_reg,                         0,                              0),
        199:('xch',     accumulator,                     i_reg,                         1,                              0),
        200:('xch',     accumulator,                     reg,                           0,                              0),

        201:('xch',     accumulator,                     reg,                           1,                              0),
        202:('xch',     accumulator,                     reg,                           2,                              0),
        203:('xch',     accumulator,                     reg,                           3,                              0),
        204:('xch',     accumulator,                     reg,                           4,                              0),
        205:('xch',     accumulator,                     reg,                           5,                              0),
        206:('xch',     accumulator,                     reg,                           6,                              0),
        207:('xch',     accumulator,                     reg,                           7,                              0),
        208:('pop',     iram_address,                    0,                             0,                              0),
        209:('acall',   page_address,                    0,                             0,                              0),
        210:('setb',    bit_address,                     0,                             0,                              0),

        211:('setb',    carry,                           0,                             0,                              0),
        212:('da a',                                     0,                             0,                              0),
        213:('djnz',    iram_address,                    relative_address,              0,                              0),
        214:('xchd',    accumulator,                     i_reg,                         0,                              0),
        215:('xchd',    accumulator,                     i_reg,                         1,                              0),
        216:('djnz',    reg,                             relative_address,              0,                              0),
        217:('djnz',    reg,                             relative_address,              1,                              0),
        218:('djnz',    reg,                             relative_address,              2,                              0),
        219:('djnz',    reg,                             relative_address,              3,                              0),
        220:('djnz',    reg,                             relative_address,              0,                              0),
        221:('djnz',    reg,                             relative_address,              5,                              0),
        222:('djnz',    reg,                             relative_address,              6,                              0),
        223:('djnz',    reg,                             relative_address,              7,                              0),
        224:('movx',    accumulator,                     i_dptr,                        0,                              0),
        225:('ajmp',    page_address,                    0,                             0,                              0),
        226:('movx',    accumulator,                     i_reg,                         0,                              0),
        227:('movx',    accumulator,                     i_reg,                         1,                              0),
        228:('clr',     accumulator,                     0,                             0,                              0),
        229:('mov',     accumulator,                     iram_address,                  0,                              0),
        230:('mov',     accumulator,                     i_reg,                         0,                              0),

        231:('mov',     accumulator,                     i_reg,                         1,                              0),
        232:('mov',     accumulator,                     reg,                           0,                              0),
        233:('mov',     accumulator,                     reg,                           1,                              0),
        234:('mov',     accumulator,                     reg,                           2,                              0),
        235:('mov',     accumulator,                     reg,                           3,                              0),
        236:('mov',     accumulator,                     reg,                           4,                              0),
        237:('mov',     accumulator,                     reg,                           5,                              0),
        238:('mov',     accumulator,                     reg,                           6,                              0),
        239:('mov',     accumulator,                     reg,                           7,                              0),
        240:('movx',    i_dptr,                          accumulator,                   0,                              0),

        241:('acall',   page_address,                    0,                             0,                              0),
        242:('movx',    i_reg,                           accumulator,                   0,                              0),
        243:('movx',    i_reg,                           accumulator,                   1,                              0),
        244:('cpl',     accumulator,                     0,                             0,                              0),
        245:('mov',     iram_address,                    accumulator,                   0,                              0),
        246:('mov',     i_reg,                           accumulator,                   0,                              0),
        247:('mov',     i_reg,                           accumulator,                   1,                              0),
        248:('mov',     reg,                             accumulator,                   0,                              0),
        249:('mov',     reg,                             accumulator,                   1,                              0),
        250:('mov',     reg,                             accumulator,                   2,                              0),

        251:('mov',     reg,                             accumulator,                   3,                              0),
        252:('mov',     reg,                             accumulator,                   4,                              0),
        253:('mov',     reg,                             accumulator,                   5,                              0),
        254:('mov',     reg,                             accumulator,                   6,                              0),
        255:('mov',     reg,                             accumulator,                   7,                              0),
        
}

if __name__ == "__main__":
    print(" This is python module ")
    print(" Run pydeasm.py file ")