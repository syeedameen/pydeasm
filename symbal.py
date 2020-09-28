import function as fn 

fs = open('test.hex','r')
fd = open('test.asm','w')

for i in fs.readlines():
    fn.convert_info(i)
    fs.write('\n')

# print assembly language number of lines 
for i in fd.readlines():
    print(i)
