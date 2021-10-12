# #opcode_table={instruction_name:(Opcode, Type, Number of registers, mem_addr, $Imm)}
opcode_table = {"add" : ("00000", "A", 3, False, False),
"sub" : ("00001", "A", 3, False, False),
"mov" : ("00010", "B", 1, False, True),
"mov" : ("00011", "C", 2, False, False),
"ld" : ("00100", "D", 1, True, False),
"st" : ("00101", "D", 1, True, False),
"mul" : ("00110", "A", 3, False, False),
"div" : ("00111", "C", 2, False, False),
"rs" : ("01000", "B", 1, False, True),
"ls" : ("01001", "B", 1, False, True),
"xor" : ("01010", "A", 3, False, False),
"or" : ("01011", "A", 3, False, False),
"and" : ("01100", "A", 3, False, False),
"not" : ("01101", "C", 2, False, False),
"cmp" : ("01110", "C", 2, False, False),
"jmp" : ("01111", "E", 0, True, False),
"jlt" : ("10000", "E", 0, True, False),
"jgt" : ("10001", "E", 0, True, False),
"je" : ("10010", "E", 0, True, False),
"hlt" : ("10011", "F", 0, False, False)}



def error_check_op(instruction):

    def reg_check(reg):

        if reg[0] != "R":
            print("error as register name is incorrect")
            return True
        elif reg[1:].isnumeric() == False:
            print("error as not between R0 and R6")
            return True
        elif int(reg[1:])>6 or int(reg[1:])<0:
            print("error as not between R0 and R6")
            return True
        else:
            return False

    def check_a(ins):
         error_found = 0
         l = len(ins)
         if l != 4:
             print("error due to length of syntax in type A")
             return True
             exit()

         reg1=reg_check(ins[1])
         if reg1 == True:
             error_found = 1
         reg2 = reg_check(ins[2])
         if reg2 == True:
             error_found = 1
         reg3 = reg_check(ins[3])
         if reg3 == True:
             error_found = 1


         if error_found == 1:
             return True
         else:
             return False

    def check_b(ins):
         error_found = 0
         l = len(ins)
         if l != 3:
             print("error due to length of syntax in type B")
             return True
             exit()

         reg1 = reg_check(ins[1])
         if reg1 == True:
             error_found = 1

         imm=ins[2]
         if imm[0] != "$":
             error_found = 1
             print("error as sign $ is not present in $Imm")
         elif imm[1:].isnumeric() == False:
             print("error as Imm is illegal")
             error_found=1
         elif int(imm[1:])>255 or int(imm[1:])<0:
             error_found = 1
             print("error as Imm is illegal")

         if error_found == 1:
             return True
         else:
             return False


    def check_c(ins):
         error_found = 0
         l = len(ins)
         if l != 3:
             print("error due to length of syntax in type C")
             return True
             exit()

         reg1=reg_check(ins[1])
         if reg1 == True:
             error_found = 1
         reg2 = reg_check(ins[2])
         if reg2 == True:
             error_found = 1

         if error_found == 1:
             return True
         else:
             return False

    def check_d(ins):
         error_found = 0
         l = len(ins)
         if l != 3:
             print("error due to length of syntax in type D")
             return True
             exit()

         reg1=reg_check(ins[1])
         if reg1 == True:
             error_found = 1

         if error_found == 1:
             return True
         else:
             return False

    def check_e(ins):

         l = len(ins)
         if l != 2:
             print("error due to length of syntax in type E")
             return True
         else:
             return False


    instruction_new=instruction.split()

    if instruction_new[0] == "add" :
         return check_a(instruction_new)

    elif instruction_new[0] == "sub" :
         return check_a(instruction_new)

    elif instruction_new[0] == "mov" :
        l = len(instruction_new)
        if l != 3:
            print("error due to length of syntax in type B")
            return True
            exit()
        elif instruction_new[2] == "FLAGS":
             return reg_check(instruction_new[1])
        elif instruction_new[2][0] == "$":
             return check_b(instruction_new)
        else:
             return check_c(instruction_new)


    elif instruction_new[0] == "ld" :
         return check_d(instruction_new)

    elif instruction_new[0] == "st" :
         return check_d(instruction_new)

    elif instruction_new[0] == "mul" :
         return check_a(instruction_new)

    elif instruction_new[0] == "div" :
         return check_c(instruction_new)

    elif instruction_new[0] == "rs" :
         return check_b(instruction_new)

    elif instruction_new[0] == "ls" :
         return check_b(instruction_new)

    elif instruction_new[0] == "xor" :
         return check_a(instruction_new)

    elif instruction_new[0] == "or" :
         return check_a(instruction_new)

    elif instruction_new[0] == "and" :
         return check_a(instruction_new)

    elif instruction_new[0] == "not" :
         return check_c(instruction_new)

    elif instruction_new[0] == "cmp" :
         return check_c(instruction_new)

    elif instruction_new[0] == "jmp" :
         return check_e(instruction_new)

    elif instruction_new[0] == "jlt" :
         return check_e(instruction_new)

    elif instruction_new[0] == "jgt" :
         return check_e(instruction_new)

    elif instruction_new[0] == "je" :
         return check_e(instruction_new)

    elif instruction_new[0] == "var" :
         l = len(instruction_new)
         if l != 2:
             print("syntax error due to length in variable instruction")
             return True
         else:
             return False


    elif instruction_new[0] == "hlt":
        return False

    elif ":" in instruction_new[0]:
        i = instruction.index(":")
        l = len(instruction_new)
        if l <2:
            print("syntax error due to length in label instruction")
            return True

        else:
            ins_after_label = instruction[i+1:]
            lst = ["add", "sub", "mov", "ld", "st", "mul", "div", "rs", "ls", "xor", "or", "and", "not", "cmp", "jmp",
                   "jlt", "jgt", "je", "hlt"]
            ins_after_label_split=ins_after_label.split()
            if ins_after_label_split[0] in lst:
                return error_check_op(ins_after_label)
            else:
                print("typo error in label instruction")
                return True

    else:
        print("Typo error due to wrong instruction name in syntax")
        return True




