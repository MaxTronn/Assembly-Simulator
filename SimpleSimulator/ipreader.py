import Processing
def input_reader(s):

    def type_A(ins):
        reg_1 = int(ins[7:10], 2)
        reg_2 = int(ins[10:13], 2)
        reg_3 = int(ins[13:], 2)
        return Processing.typeA(ins[0:5], reg_1, reg_2, reg_3)
        # (opcode, reg1, reg2, reg3)
        #reg1 is an integer. If reg1 is 2 it indicates the particualar register is R2.

    def type_B(ins):
        reg_1 = int(ins[5:8], 2)
        imm = int(ins[8:], 2)
        return Processing.typeB(ins[0:5], reg_1, imm)
        # (opcode, reg1, immediate value)

    def type_C(ins):
        reg_1 = int(ins[10:13], 2)
        reg_2 = int(ins[13:], 2)

        return Processing.typeC(ins[0:5], reg_1, reg_2)
        #(opcode, reg1, reg2)

    def type_D(ins):
        reg_1 = int(ins[5:8], 2)
        mem = int(ins[8:], 2)
        return Processing.typeD(ins[0:5], reg_1, mem)
        #(opcode, reg1, memory address)

    def type_E(ins):
        mem = int(ins[8:], 2)
        return Processing.typeE(ins[0:5], mem)
        #(opcode, memory address)

    #processing function of type F not handled yet
    def type_F(ins):
        return Processing.typeF()
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

#input_reader("0001000100000100")#move R1 $4
#input_reader("0001001000000100")#move R2 $4
#input_reader("0000000000001010")#Add R0 R1 R2
#input_reader("0001101000100000")#move R3 R0 type C and D
#input_reader("0010100000000010")# store R0 mem_addr{2} type D
#input_reader("0111100000000010")#jump memaddr(2)


"""
type E
Flags V
Printing CHECK'
PC= list-->jump
memory dump
"""