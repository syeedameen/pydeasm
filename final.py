#----------------------------------------------------------#
#           PYTHON DISASSEMBLER IN ONE FILE                #
#----------------------------------------------------------#



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







opcode = {
        '00':('nop'),
        '01':('ajmp',page_address),
        '02':('ljmp',address_16_bit),
        '03':('rr a'),
        '04':('inc a'),
        '05':('inc',iram_address),
        '06':('inc @r0'),
        '07':('inc @r1'),
        '08':('inc r0'),
        '09':('inc r1'),
        '0A':('inc r2'),
        '0B':('inc r3'),
        '0C':('inc r4'),
        '0D':('inc r5'),
        '0E':('inc r6'),
        '0F':('inc r7'),
        '10':('jbc 0x',      bit_address,                relative_address),
        '11':('acall',    page_address                ),
        '12':('lcall',    address_16_bit              ),
        '13':('rrc a'),
        '14':('dec a'),

        '15':('dec 0x',iram_address),
        '16':('dec @r0'),
        '17':('dec @r1'),
        '18':('dec r0'),
        '19':('dec r1'),
        '1A':('dec r2'),
        '1B':('dec r3'),
        '1C':('dec r4'),
        '1D':('dec r5'),
        '1E':('dec r6'),

        '1F':('dec r7'),
        '20':('jb',       bit_address,                relative_address),
        '21':('ajmp',     page_address                ),
        '22':('ret'),
        '23':('rl a'),
        '24':('add a',immediate_data),
        '25':('add a',iram_address),
        '26':('add a,@r0'),
        '27':('add a,@r1'),
        '28':('add a,r0'),

        '29':('add a,r1'),
        '2A':('add a,r2'),
        '2B':('add a,r3'),
        '2C':('add a,r4'),
        '2D':('add a,r5'),
        '2E':('add a,r6'),
        '2F':('add a,r7'),
        '30':('jnb',      bit_address,                relative_address),
        '31':('acall',    page_address                ),
        '32':('reti'                                  ),

        '33':('rcl a'),
        '34':('addc a,',immediate_data),
        '35':('addc a,',iram_address),
        '36':('adcc a,@r0'),
        '37':('adcc a,@r1'),
        '38':('adcc a,r0'),
        '39':('adcc a,r1'),
        '3A':('adcc a,r2'),
        '3B':('adcc a,r3'),
        '3C':('adcc a,r4'),

        '3D':('adcc a,r5'),
        '3E':('adcc a,r6'),
        '3F':('adcc a,r7'),
        '40':('jc',relative_address           ),
        '41':('ajmp',page_address               ),
        '42':('orl 0x',iram_address,accumulator),
        '43':('orl 0x', iram_address,immediate_data),
        '44':('orl a,',immediate_data),
        '45':('orl a,',iram_address),
        '46':('orl a,@r0'),

        '47':('orl a,@r1'),
        '48':('orl a,r0'),
        '49':('orl a,r1'),
        '4A':('orl a,r2'),
        '4B':('orl a,r3'),
        '4C':('orl a,r4'),
        '4D':('orl a,r5'),
        '4E':('orl a,r6'),
        '4F':('orl a,r7'),
        '50':('jnc',relative_address),

        '51':('acall',page_address),
        '52':('anl 0x',iram_address,accumulator),
        '53':('anl 0x',iram_address,immediate_data),
        '54':('anl a,#0x',immediate_data),
        '55':('anl a,',iram_address),
        '56':('anl a,@r0'),
        '57':('anl a,@r1'),
        '58':('anl a,r0'),
        '59':('anl a,r1'),
        '5A':('anl a,r2'),

        '5B':('anl a,r3'),
        '5C':('anl a,r4'),
        '5D':('anl a,r5'),
        '5E':('anl a,r6'),
        '5F':('anl a,r7'),
        '60':('jz',relative_address),
        '61':('ajmp',page_address),
        '62':('xrl 0x',iram_address,accumulator),
        '63':('xrl 0x',iram_address,immediate_data),
        '64':('xrl a,#',immediate_data),

        '65':('xrl a,0x',iram_address),
        '66':('xrl a,@r0'),
        '67':('xrl a,@r1'),
        '68':('xrl a,r0'), 
        '69':('xrl a,r1'),
        '6A':('xrl a,r2'),
        '6B':('xrl a,r3'),
        '6C':('xrl a,r4'),
        '6D':('xrl a,r5'),
        '6E':('xrl a,r6'),

        '6F':('xrl a,r7'),
        '70':('jnz',relative_address),
        '71':('acall',page_address),
        '72':('orl c,0x',bit_address),
        '73':('jmp @a+dptr'),
        '74':('mov a,#0x',immediate_data),
        '75':('mov 0x',iram_address,immediate_data),
        '76':('mov a,@r0'),
        '77':('mov a,@r1'),
        '78':('mov r0,#0x',immediate_data),

        '79':('mov r1,#0x',immediate_data),
        '7A':('mov r2,#0x',immediate_data),
        '7B':('mov r3,#0x',immediate_data),
        '7C':('mov r4,#0x',immediate_data),
        '7D':('mov r5,#0x',immediate_data),
        '7E':('mov r6,#0x',immediate_data),
        '7F':('mov r7,#0x',immediate_data),
        '80':('sjmp',relative_address),
        '81':('ajmp',page_address),
        '82':('anl c,0x',bit_address),

        '83':('movc a,@a+pc'),
        '84':('div ab'),
        '85':('mov 0x',     iram_address,               iram_address),
        '86':('mov 0x',     iram_address,               i_reg,0),
        '87':('mov 0x',     iram_address,               i_reg,1),
        '88':('mov 0x',     iram_address,               reg,0),
        '89':('mov 0x',     iram_address,               reg,1),
        '8A':('mov 0x',     iram_address,               reg,2),
        '8B':('mov 0x',     iram_address,               reg,3),

        '8C':('mov 0x',     iram_address,               reg,4),
        '8D':('mov 0x',     iram_address,               reg,5),
        '8E':('mov 0x',     iram_address,               reg,6),
        '8F':('mov 0x',     iram_address,               reg,7),
        '90':('mov dptr,#0x',data_16_bit),
        '91':('acall',page_address),
        '92':('mov 0x',bit_address,carry),
        '93':('movc a,@a+dptr'),
        '94':('subb a,#0x',immediate_data),
        '95':('subb a,0x',iram_address),
        '96':('subb a,@r0'),
        '97':('subb a,@r1'),
        '98':('subb a,r0'),
        '99':('subb a,r1'),
        '9A':('subb a,r2'),
        '9B':('subb a,r3'),
        '9C':('subb a,r4'),
        '9D':('subb a,r5'),
        '9E':('subb a,r6'),
        '9F':('subb a,r07'),
        'A0':('orl c,0x',bit_address),

        'A1':('ajmp',page_address),
        'A2':('mov c,0x',bit_address),
        'A3':('inc dptr'),
        'A4':('mul ab'),
        'A5':('reserved'),         
        'A6':('mov @r0,0x',iram_address),
        'A7':('mov @r1,0x',iram_address),
        'A8':('mov r0,0x',iram_address),
        'A9':('mov r1,0x',iram_address),
        'AA':('mov r2,0x',iram_address),

        'AB':('mov r3,0x',iram_address),
        'AC':('mov r4,0x',iram_address),
        'AD':('mov r5,0x',iram_address),
        'AE':('mov r6,0x',iram_address),
        'AF':('mov r7,0x',iram_address),
        'B0':('anl c,0x',bit_address),
        'B1':('acall',page_address),
        'B2':('cpl 0x',bit_address),
        'B3':('cpl c'),
        'B4':('cjne a,#0x',immediate_data,relative_address),

        'B5':('cjne a,0x',iram_address,relative_address),
        'B6':('cjne @r0,#0x',immediate_data,relative_address),
        'B7':('cjne @r1,#0x',immediate_data,relative_address),
        'B8':('cjne r0,#0x',immediate_data,relative_address),
        'B9':('cjne r1,#0x',immediate_data,relative_address),
        'BA':('cjne r2,#0x',immediate_data,relative_address),
        'BB':('cjne r3,#0x',immediate_data,relative_address),
        'BC':('cjne r4,#0x',immediate_data,relative_address),
        'BD':('cjne r5,#0x',immediate_data,relative_address),
        'BE':('cjne r6,#0x',immediate_data,relative_address),
        'BF':('cjne r7,#0x',immediate_data,relative_address),
        'C0':('push 0x',iram_address),
        'C1':('ajmp',page_address),
        'C2':('clr 0x',bit_address),
        'C3':('clr c'),
        'C4':('swap a'),
        'C5':('xch a,0x',iram_address),
        'C6':('xch a,@r0'),
        'C7':('xch a,@r1'),
        'C8':('xch a,r0'),

        'C9':('xch a,r1'),
        'CA':('xch a,r2'),
        'CB':('xch a,r3'),
        'CC':('xch a,r4'),
        'CD':('xch a,r5'),
        'CE':('xch a,r6'),
        'CF':('xch a,r7'),
        'D0':('pop 0x',iram_address),
        'D1':('acall 0x',page_address),
        'D2':('setb 0x',bit_address),

        'D3':('setb c'),
        'D4':('da a'),
        'D5':('djnz 0x',iram_address,relative_address),
        'D6':('xchd a,@r0'),
        'D7':('xchd a,@r1'),
        'D8':('djnz r0,0x',relative_address),
        'D9':('djnz r1,0x',relative_address),
        'DA':('djnz r2,0x',relative_address),
        'DB':('djnz r3,0x',relative_address),
        'DC':('djnz r4,0x',relative_address),
        'DD':('djnz r5,0x',relative_address),
        'DE':('djnz r6,0x',relative_address),
        'DF':('djnz r7,0x',relative_address),
        'E0':('movx a,@dptr'),
        'E1':('ajmp',page_address),
        'E2':('movx a,@r0'),
        'E3':('movx a,@r1'),
        'E4':('clr a'),
        'E5':('mov a,0x',iram_address),
        'E6':('mov a,@r0'),

        'E7':('mov a,@r1'),
        'E8':('mov a,r0'),
        'E9':('mov a,r1'),
        'EA':('mov a,r2'),
        'EB':('mov a,r3'),
        'EC':('mov a,r4'),
        'ED':('mov a,r5'),
        'EE':('mov a,r6'),
        'EF':('mov a,r7'),
        'F0':('movx @dptr,a'),

        'F1':('acall',page_address),
        'F2':('movx @r0,a'),
        'F3':('movx @r1,a'),
        'F4':('cpl a'),
        'F5':('mov 0x',iram_address,accumulator),
        'F6':('mov @r0,a'),
        'F7':('mov @r1,a'),
        'F8':('mov r0,a'),
        'F9':('mov r1,a'),
        'FA':('mov r2,a'),

        'FB':('mov r3,a'),
        'FC':('mov r4,a'),
        'FD':('mov r5,a'),
        'FE':('mov r6,a'),
        'FF':('mov r7,a'),
        
}


#---------------------------------------------------------------------------------#
#                           Length of Different opcodes                           #
#---------------------------------------------------------------------------------#

opcode_len = [
        1,2,3,1,1,2,1,1,1,1,1,1,1,1,1,1,        # 00 - 0F 
        3,2,3,1,1,2,1,1,1,1,1,1,1,1,1,1,        # 10 - 1F
        3,2,1,1,2,2,1,1,1,1,1,1,1,1,1,1,        # 20 - 2F 
        3,2,1,1,2,2,1,1,1,1,1,1,1,1,1,1,        # 30 - 3F 
        2,2,2,3,2,2,1,1,1,1,1,1,1,1,1,1,        # 40 - 4F
        2,2,2,3,2,2,1,1,1,1,1,1,1,1,1,1,        # 50 - 5F
        2,2,2,3,2,2,1,1,1,1,1,1,1,1,1,1,        # 60 - 6F 
        2,2,2,1,2,3,2,2,2,2,2,2,2,2,2,2,        # 70 - 7F
        2,2,2,1,1,3,2,2,2,2,2,2,2,2,2,2,        # 80 - 8F 
        3,2,2,1,2,2,1,1,1,1,1,1,1,1,1,1,        # 90 - 9F
        2,2,2,1,1,0,2,2,2,2,2,2,2,2,2,2,        # A0 - AF
        2,2,2,1,3,3,3,3,3,3,3,3,3,3,3,3,        # B0 - BF
        2,2,2,1,1,2,1,1,1,1,1,1,1,1,1,1,        # C0 - CF
        2,2,2,1,1,3,1,1,2,2,2,2,2,2,2,2,        # D0 - DF 
        1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,        # E0 - EF
        1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,        # F0 - FF    
]


one_byte    = 140       #number of one byte instructions
two_byte    = 91        #number of two byte instructions
three_byte  = 24        #number of three byte instructions
reserved    = 1         #number of reserved instruction 
