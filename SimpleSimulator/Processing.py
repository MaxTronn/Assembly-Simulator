import simprint
import Plotter
from sys import stdin

#load pc from main (pc = Program Counter)


#print(plist)


pc = 0
plist=[0,]
global mem_list
mem_list = [0]*256

#st_ld_dict keeps track of memory addresses used in store and load instruction and the pc value when these instructions are invoked
st_ld_dict = {}

#get reg values from main
global reg_list
reg_list = [0,0,0,0,0,0,0,0]


def typeA(opcode, a, b, c):


    global reg_list

    global pc
    global plist

    #Add

    if opcode == "00000" :
        reg_list[7]=0
        reg_list[a] = reg_list[b] + reg_list[c]
        pc += 1
        plist.append(pc)



        if reg_list[a] > 65535: #exceed; a=
            flagV=1
            reg_list[a]=reg_list[a]%65536
            reg_list[7] = 8


    #Subtract
    elif opcode == "00001" :
        reg_list[7] = 0
        pc += 1
        plist.append(pc)

        if (reg_list[c] > reg_list[b]):
            
            reg_list[a] = 0
            reg_list[7] = 8

        else:
            reg_list[a] = reg_list[b] - reg_list[c]


    #Multiply
    elif opcode == "00110" :
        reg_list[7] = 0
        reg_list[a] = reg_list[b] * reg_list[c]
        pc+=1
        plist.append(pc)

        if reg_list[a] > 65535:
            reg_list[7] = 8
            reg_list[a] = reg_list[a] % 65536
            

    #Xor
    elif opcode == "01010":
        reg_list[7]=0
        reg_list[a] = reg_list[b] ^ reg_list[c]
        pc += 1
        plist.append(pc)

    #Or
    elif opcode == "01011":
        reg_list[7] = 0
        reg_list[a] = reg_list[b] | reg_list[c]
        pc += 1
        plist.append(pc)

    #And
    elif opcode == "01100":
        reg_list[7] = 0
        reg_list[a] = reg_list[b] & reg_list[c]
        pc += 1
        plist.append(pc)
   # print(plist)
    simprint.simprint(reg_list, plist[-2])
    #reg_list[7]=0

def typeB(opcode, a, imm):

    global reg_list
    global pc
    global plist

    #Move Immediate
    if opcode == "00010":
        reg_list[7]=0
        reg_list[a] = imm

        pc+=1
        plist.append(pc)

    #Right Shift
    elif opcode == "01000":
        reg_list[7] = 0
        reg_list[a] = reg_list[a] >> imm
        pc += 1
        plist.append(pc)

    #Left Shift
    elif opcode == "01001":
        reg_list[7] = 0
        reg_list[a] = reg_list[a] << imm
        pc += 1
        plist.append(pc)

        if reg_list[a] > 65535:
            reg_list[7] = 0
            
            reg_list[a] = reg_list[a] % 65536
            reg_list[7]=8

    simprint.simprint(reg_list, plist[-2])
   # reg_list[7]=0

def typeC(opcode, a, b):
    global reg_list
    global plist

    global pc

    #Move Register Register / FLAGS
    if opcode == "00011":

        reg_list[a] = reg_list[b]
        pc+=1
        plist.append(pc)
        reg_list[7]=0

    #Divide
    elif opcode == "00111":
        reg_list[7] = 0
        reg_list[0] = reg_list[a] // reg_list[b]
        reg_list[1] = reg_list[a] % reg_list[b]
        pc += 1
        plist.append(pc)

    #Invert (Not Function)
    elif opcode == "01101":
        reg_list[7] = 0
        reg_list[a] = ~reg_list[b]
        pc += 1
        plist.append(pc)


    #Compare
    elif opcode == "01110":
        reg_list[7] = 0
        pc += 1
        plist.append(pc)
        if (reg_list[a] == reg_list[b]):

            reg_list[7]=1

        elif (reg_list[a] > reg_list[b]):

            reg_list[7] = 2



        elif (reg_list[a] < reg_list[b]):

            reg_list[7] = 4




    simprint.simprint(reg_list, plist[-2])
    #reg_list[7]=0

def typeD(opcode, a, addr):

    global reg_list
    global mem_list
    global mem_addr
    global pc
    global plist
    global st_ld_dict

    #Load  reg1  <-- data in addr
    if opcode == "00100":
        reg_list[7] = 0
        reg_list[a] = mem_list[addr]
        st_ld_dict.update({len(plist)-1:addr})
        pc+=1

        plist.append(pc)

    #Store  reg1 --> addr
    elif opcode == "00101":
        reg_list[7] = 0
        mem_list[addr] = reg_list[a]
        st_ld_dict.update({len(plist)-1:addr})
        pc+=1

        plist.append(pc)

    simprint.simprint(reg_list, plist[-2])


def typeE(opcode, addr):
    global mem_list
    global flagL
    global flagG
    global flagE
    global pc
    global plist

    #Unconditional Jump (jmp)
    if opcode == "01111":
#        plist.append(pc+1)
        pc = addr
        plist.append(pc)



    #Jump if Less than (jlt)
    elif opcode == "10000":
        if reg_list[7]==4:
            pc = addr
            plist.append(pc)
            reg_list[7]=0

        else:
            pc+=1
            plist.append(pc)
            reg_list[7]=0


    #Jump if Greater than (jgt)
    elif opcode == "10001":
        if reg_list[7] == 2:
            pc = addr
            plist.append(pc)
            reg_list[7]=0

        else:
            pc+=1
            plist.append(pc)
            reg_list[7] = 0


    # Jump if Equal (je)
    elif opcode == "10010":
        if reg_list[7] == 1:
            pc = addr
            plist.append(pc)
            reg_list[7]=0

        else:
            pc+=1
            plist.append(pc)
            reg_list[7]=0

    simprint.simprint(reg_list, plist[-2])

    #reg_list[7] = 0


def typeF():

    global reg_list
    global pc

    reg_list[7]=0
    pc+=1
    plist.append(pc)
  #  print('end')
    simprint.simprint(reg_list, plist[-2])



#flags value of g in other

input_dict={}
input_list=[]

def pa():
    pc=0
    for line in stdin:
        #$input_lineno+=1
        if line == " ":
            break

        input_dict.update({pc: line})
        input_list.append(line)
        pc += 1



def input_reader(s):

    def type_A(ins):
        reg_1 = int(ins[7:10], 2)
        reg_2 = int(ins[10:13], 2)
        reg_3 = int(ins[13:], 2)
        return typeA(ins[0:5], reg_1, reg_2, reg_3)
        # (opcode, reg1, reg2, reg3)
        #reg1 is an integer. If reg1 is 2 it indicates the particualar register is R2.

    def type_B(ins):
        reg_1 = int(ins[5:8], 2)
        imm = int(ins[8:], 2)
        return typeB(ins[0:5], reg_1, imm)
        # (opcode, reg1, immediate value)

    def type_C(ins):
        reg_1 = int(ins[10:13], 2)
        reg_2 = int(ins[13:], 2)

        return typeC(ins[0:5], reg_1, reg_2)
        #(opcode, reg1, reg2)

    def type_D(ins):
        reg_1 = int(ins[5:8], 2)
        mem = int(ins[8:], 2)
        return typeD(ins[0:5], reg_1, mem)
        #(opcode, reg1, memory address)

    def type_E(ins):
        mem = int(ins[8:], 2)
        return typeE(ins[0:5], mem)
        #(opcode, memory address)

    #processing function of type F not handled yet
    def type_F(ins):
        return typeF()
        #(opcode)


    op = s[0:5]

    if op == "00000" or op == "00001" or op == "00110" or op == "01010" or op == "01011" or op == "01100":
        type_A(s)

    elif op == "00010" or op == "01000" or op == "01001":
        type_B(s)

    elif op == "00011" or op == "00111" or op == "01101" or op == "01110":
        type_C(s)

    elif op == "00100" or op == "00101":
        type_D(s)

    elif op == "01111" or op == "10000" or op == "10001" or op == "10010":
        type_E(s)

    elif op == "10011":
        type_F(s)


pa()
'''
for k,v in input_dict.items():
    print(k, " : ", v)
'''

while True:
    if plist[-1] < len(input_dict):

        input_reader(input_dict[plist[-1]])

    else:
        break

mem_list = simprint.memdmp(mem_list)

for i in range(len(input_list)):
    input_list[i] = input_list[i].replace("\n", "")
    mem_list[i] = input_list[i]

for i in mem_list:
    print(i)

plist = plist[:-1:]
'''
print("\n", "plist = ", plist, "\n")
print("\n" , " Store Load Dictionary {key = Cycle Number : Value = Mem_Address")
for k,v in st_ld_dict.items():
    print(k, " : ", v)
'''
Plotter.generate_plot(plist, st_ld_dict)