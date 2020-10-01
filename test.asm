pop 0x7F
pop 0x7E
pop 0x83
pop 0x82
pop 0xE0
push 0x7
nop
nop
nop
nop
nop
push 0x45
lcall None
movx @r0,a
add a,r4
djnz r2,0xD4
anl a,r4
xchd a,@r1
anl c,!0xFB
nop
nop
nop
nop
nop
nop
