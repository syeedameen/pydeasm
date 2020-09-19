
#   Author:     SYEED MOHD AMEEN                                    Date:   19-09-2020
#   Email:      ameensyeed2@gmail.com
#   License:    GPLv3



#------------------------------------------------------------#
#                       Opcode Table                         #
#------------------------------------------------------------#


accumulator         = 0
reg                 = 1
i_reg               = 2 
page_address        = 3 
address_16_bit      = 4 
data_16_bit         = 5 
accumulator         = 6 
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



opcode = {
        0:('nop'        0,                     0,0,0),
        1:('ajmp',      page_address                ),
        2:('ljmp',      address_16_bit              ),
        3:('rr',        accumulator                 ),
        4:('inc',       accumulator                 ),
        5:('inc',       iram_address                ),
        6:('inc',       i_reg,                      0),
        7:('inc',       i_reg,                      1),
        8:('inc',       reg,                        0),
        9:('inc',       reg,                        1),
        10:('inc',      reg,                        2),

        11:('inc',      reg,                        3),
        12:('inc',      reg,                        4),
        13:('inc',      reg,                        5),
        14:('inc',      reg,                        6),
        15:('inc',      reg,                        7),
        16:('jbc',      bit_address,                relative_address),
        17:('acall',    page_address                ),
        18:('lcall',    address_16_bit              ),
        19:('rrc',      accumulator                 ),
        20:('dec',      accumulator                 ),

        21:('dec',      iram_address                ),
        22:('dec',      i_reg,                      0),
        23:('dec',      i_reg,                      1),
        24:('dec',      reg,                        0),
        25:('dec',      reg,                        1),
        26:('dec',      reg,                        2),
        27:('dec',      reg,                        3),
        28:('dec',      reg,                        4),
        29:('dec',      reg,                        5),
        30:('dec',      reg,                        6),

        31:('dec',      reg,                        7),
        32:('jb',       bit_address,                relative_address),
        33:('ajmp',     page_address                ),
        34:('ret'                                   ),
        35:('rl',       accumulator                 ),
        36:('add',      accumulator,                immediate_data),
        37:('add',      accumulator,                iram_address),
        38:('add',      accumulator,                i_reg,0),
        39:('add',      accumulator,                i_reg,1),
        40:('add',      accumulator,                reg,0),

        41:('add',      accumulator,                reg,1),
        42:('add',      accumulator,                reg,2),
        43:('add',      accumulator,                reg,3),
        44:('add',      accumulator,                reg,4),
        45:('add',      accumulator,                reg,5),
        46:('add',      accumulator,                reg,6),
        47:('add',      accumulator,                reg,7),
        48:('jnb',      bit_address,                relative_address),
        49:('acall',    page_address                ),
        50:('reti'                                  ),

        51:('rcl',      accumulator                 ),
        52:('addc',     accumulator,                immediate_data),
        53:('addc',     accumulator,                iram_address),
        54:('adcc',     accumulator,                i_reg,0),
        55:('adcc',     accumulator,                i_reg,1),
        56:('adcc',     accumulator,                reg,0),
        57:('adcc',     accumulator,                reg,1),
        58:('adcc',     accumulator,                reg,2),
        59:('adcc',     accumulator,                reg,3),
        60:('adcc',     accumulator,                reg,4),

        61:('adcc',     accumulator,                reg,5),
        62:('adcc',     accumulator,                reg,6),
        63:('adcc',     accumulator,                reg,7),
        64:('jc',       relative_address            ),
        65:('ajmp',     page_address                ),
        66:('orl',      iram_address,               accumulator),
        67:('orl',      iram_address,               immediate_data),
        68:('orl',      accumulator,                immediate_data),
        69:('orl',      accumulator,                iram_address),
        70:('orl',      accumulator,                i_reg,0),

        71:('orl',      accumulator,                i_reg,1),
        72:('orl',      accumulator,                reg,0),
        73:('orl',      accumulator,                reg,1),
        74:('orl',      accumulator,                reg,2),
        75:('orl',      accumulator,                reg,3),
        76:('orl',      accumulator,                reg,4),
        77:('orl',      accumulator,                reg,5),
        78:('orl',      accumulator,                reg,6),
        79:('orl',      accumulator,                reg,7),
        80:('jnc',      relative_address            ),

        81:('acall',    page_address                ),
        82:('anl',      iram_address,               accumulator),
        83:('anl',      iram_address,               immediate_data),
        84:('anl',      accumulator,                immediate_data),
        85:('anl',      accumulator,                iram_address),
        86:('anl',      accumulator,                i_reg,0),
        87:('anl',      accumulator,                i_reg,1),
        88:('anl',      accumulator,                reg,0),
        89:('anl',      accumulator,                reg,1),
        90:('anl',      accumulator,                reg,2),

        91:('anl',      accumulator,                reg,3),
        92:('anl',      accumulator,                reg,4),
        93:('anl',      accumulator,                reg,5),
        94:('anl',      accumulator,                reg,6),
        95:('anl',      accumulator,                reg,7),
        96:('jz',       relative_address            ),
        97:('ajmp',     page_address                ),
        98:('xrl',      iram_address,               accumulator),
        99:('xrl',      iram_address,               immediate_data),
        100:('xrl',     accumulator,                immediate_data),

        101:('xrl',     accumulator,                iram_address),
        102:('xrl',     accumulator,                i_reg,0),
        103:('xrl',     accumulator,                i_reg,1),
        104:('xrl',     accumulator,                reg,0), 
        105:('xrl',     accumulator,                reg,1),
        106:('xrl',     accumulator,                reg,2),
        107:('xrl',     accumulator,                reg,3),
        108:('xrl',     accumulator,                reg,4),
        109:('xrl',     accumulator,                reg,5),
        110:('xrl',     accumulator,                reg,6),

        111:('xrl',     accumulator,                reg,7),
        112:('jnz',     relative_address            ),
        113:('acall',   page_address                ),
        114:('orl',     carry,                      bit_address),
        115:('jmp',     i_acc_pl_dptr               ),
        116:('mov',     accumulator,                immediate_data),
        117:('mov',     iram_address,               immediate_data),
        118:('mov',     i_reg,                      immediate_data,0),
        119:('mov',     i_reg,                      immediate_data,1),
        120:('mov',     reg,                        immediate_data,0),

        121:('mov',     reg,                        immediate_data,1),
        122:('mov',     reg,                        immediate_data,2),
        123:('mov',     reg,                        immediate_data,3),
        124:('mov',     reg,                        immediate_data,4),
        125:('mov',     reg,                        immediate_data,5),
        126:('mov',     reg,                        immediate_data,6),
        127:('mov',     reg,                        immediate_data,7),
        128:('sjmp',    relative_address            ),
        129:('ajmp',    page_address                ),
        130:('anl',     carry,                      bit_address),

        131:('movc',    accumulator,                i_acc_pl_pc),
        132:('div',     accumulator,                Breg),
        133:('mov',     iram_address,               iram_address),
        134:('mov',     iram_address,               i_reg,0),
        135:('mov',     iram_address,               i_reg,1),
        136:('mov',     iram_address,               reg,0),
        137:('mov',     iram_address,               reg,1),
        138:('mov',     iram_address,               reg,2),
        139:('mov',     iram_address,               reg,3),

        140:('mov',     iram_address,               reg,4),
        141:('mov',     iram_address,               reg,5),
        142:('mov',     iram_address,               reg,6),
        143:('mov',     iram_address,               reg,7),
        144:('mov',     dptr,                       data_16_bit),
        145:('acall',   page_address                ),
        146:('mov',     bit_address,                carry),
        147:('movc',    accumulator,                i_acc_pl_dptr),
        148:('subb',    accumulator,                immediate_data),
        149:('subb',    accumulator,                iram_address),
        150:('subb',    accumulator,                i_reg,0),
        151:('subb',    accumulator,                i_reg,1),
        152:('subb',    accumulator,                reg,0),
        153:('subb',    accumulator,                reg,1),
        154:('subb',    accumulator,                reg,2),
        155:('subb',    accumulator,                reg,3),
        156:('subb',    accumulator,                reg,4),
        157:('subb',    accumulator,                reg,5),
        158:('subb',    accumulator,                reg,6),
        159:('subb',    accumulator,                reg,7),
        160:('orl',     carry,                      bit_address),

        161:('ajmp',    page_address                ),
        162:('mov',     carry,                      bit_address),
        163:('inc',     dptr                        ),
        164:('mul',     accumulator,                Breg),
        165:('reserved',0,0,0),         
        166:('mov',     i_reg,                      iram_address,0),
        167:('mov',     i_reg,                      iram_address,1),
        168:('mov',     reg,                        iram_address),
        169:('mov',     reg,                        iram_address,1),
        170:('mov',     reg,                        iram_address,2),

        171:('mov',     reg,                        iram_address,3),
        172:('mov',     reg,                        iram_address,4),
        173:('mov',     reg,                        iram_address,5),
        174:('mov',     reg,                        iram_address,6),
        175:('mov',     reg,                        iram_address,7),
        176:('anl',     carry,                      bit_address),
        177:('acall',   page_address                ),
        178:('cpl',     bit_address                 ),
        179:('cpl',     carry                       ),
        180:('cjne',    accumulator,                immediate_data,relative_address),

        181:('cjne',    accumulator,                iram_address,relative_address),
        182:('cjne',    i_reg,                      immediate_data,relative_address,0),
        183:('cjne',    i_reg,                      immediate_data,relative_address,1),
        184:('cjne',    reg,                        immediate_data,relative_address,0),
        185:('cjne',    reg,                        immediate_data,relative_address,1),
        186:('cjne',    reg,                        immediate_data,relative_address,2),
        187:('cjne',    reg,                        immediate_data,relative_address,3),
        188:('cjne',    reg,                        immediate_data,relative_address,4),
        189:('cjne',    reg,                        immediate_data,relative_address,5),
        190:('cjne',    reg,                        immediate_data,relative_address,6),
        191:('cjne',    reg,                        immediate_data,relative_address,7),
        192:('push',    iram_address                ),
        193:('ajmp',    page_address                ),
        194:('clr',     bit_address                 ),
        195:('clr',     carry                       ),
        196:('swap',    accumulator                 ),
        197:('xch',     accumulator,                iram_address),
        198:('xch',     accumulator,                i_reg,0),
        199:('xch',     accumulator,                i_reg,1),
        200:('xch',     accumulator,                reg,0),

        201:('xch',     accumulator,                reg,1),
        202:('xch',     accumulator,                reg,2),
        203:('xch',     accumulator,                reg,3),
        204:('xch',     accumulator,                reg,4),
        205:('xch',     accumulator,                reg,5),
        206:('xch',     accumulator,                reg,6),
        207:('xch',     accumulator,                reg,7),
        208:('pop',     iram_address                ),
        209:('acall',   page_address                ),
        210:('setb',    bit_address                 ),

        211:('setb',    carry                       ),
        212:('da a'                                 ),
        213:('djnz',    iram_address,               relative_address),
        214:('xchd',    accumulator,                i_reg,0),
        215:('xchd',    accumulator,                i_reg,1),
        216:('djnz',    reg,                        relative_address,0),
        217:('djnz',    reg,                        relative_address,1),
        218:('djnz',    reg,                        relative_address,2),
        219:('djnz',    reg,                        relative_address,3),
        220:('djnz',    reg,                        relative_address),
        221:('djnz',    reg,                        relative_address,5),
        222:('djnz',    reg,                        relative_address,6),
        223:('djnz',    reg,                        relative_address,7),
        224:('movx',    accumulator,                i_dptr),
        225:('ajmp',    page_address                ),
        226:('movx',    accumulator,                i_reg,0),
        227:('movx',    accumulator,                i_reg,1),
        228:('clr',     accumulator                 ),
        229:('mov',     accumulator,                iram_address),
        230:('mov',     accumulator,                i_reg,0),

        231:('mov',     accumulator,                i_reg,1),
        232:('mov',     accumulator,                reg,0),
        233:('mov',     accumulator,                reg,1),
        234:('mov',     accumulator,                reg,2),
        235:('mov',     accumulator,                reg,3),
        236:('mov',     accumulator,                reg,4),
        237:('mov',     accumulator,                reg,5),
        238:('mov',     accumulator,                reg,6),
        239:('mov',     accumulator,                reg,7),
        240:('movx',    i_dptr,                     accumulator),

        241:('acall',   page_address                ),
        242:('movx',    i_reg,                      accumulator,0),
        243:('movx',    i_reg,                      accumulator,1),
        244:('cpl',     accumulator                 ),
        245:('mov',     iram_address,               accumulator),
        246:('mov',     i_reg,                      accumulator,0),
        247:('mov',     i_reg,                      accumulator,1),
        248:('mov',     reg,                        accumulator,0),
        249:('mov',     reg,                        accumulator,1),
        250:('mov',     reg,                        accumulator,2),

        251:('mov',     reg,                        accumulator,3),
        252:('mov',     reg,                        accumulator,4),
        253:('mov',     reg,                        accumulator,5),
        254:('mov',     reg,                        accumulator,6),
        255:('mov',     reg,                        accumulator,7),
        
}


def main():
    pass 

if __name__ == "__main__":
    main()