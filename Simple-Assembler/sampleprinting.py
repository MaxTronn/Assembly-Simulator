opcode_table = {"add": ("00000", "A", 3, False, False),
                "sub": ("00001", "A", 3, False, False),
                "mov": ("00010", "B", 1, False, True),
                "mov": ("00011", "C", 2, False, False),
                "ld": ("00100", "D", 1, True, False),
                "st": ("00101", "D", 1, True, False),
                "mul": ("00110", "A", 3, False, False),
                "div": ("00111", "C", 2, False, False),
                "rs": ("01000", "B", 1, False, True),
                "ls": ("01001", "B", 1, False, True),
                "xor": ("01010", "A", 3, False, False),
                "or": ("01011", "A", 3, False, False),
                "and": ("01100", "A", 3, False, False),
                "not": ("01101", "C", 2, False, False),
                "cmp": ("01110", "C", 2, False, False),
                "jmp": ("01111", "E", 0, True, False),
                "jlt": ("10000", "E", 0, True, False),
                "jgt": ("10001", "E", 0, True, False),
                "je": ("10010", "E", 0, True, False),
                "hlt": ("10011", "F", 0, False, False)}

typeA = ['add', 'sub', 'mul', 'xor', 'or', 'and']
typeB = ['rs', 'ls']
typeC = ['div', 'not', 'cmp']
typeD = ['ld', 'st']
typeE = ['jmp', 'jlt', 'jgt', 'je']
typeF = ['hlt']


reg = {'R0': '000', 'R1': '001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101', 'R6': '110', 'FLAGS': '111'}

# PrintingPattern
# BinaryEncoding

def printing(input_dict,label_dict):
    for key, value in input_dict.items():
        if value[0] in typeA:
            for i in opcode_table:
                # print(value[0])
                if value[0] == i:
                    # print(value[0])
                    # print(i)
                    a = opcode_table[i][0]
            #           print(a)
            b = '00'
            #  print(b)
            for i in reg:
                if value[1] == i:
                    c = reg[i]
            #         print(c)

            for i in reg:
                if value[2] == i:
                    d = reg[i]
            #        print(d)

            for i in reg:
                if value[3] == i:
                    e = reg[i]
            #       print(e)

            print(a + b + c + d + e)


        elif value[0] in typeB:
            if value[0] == 'mov':
                if '$' in value[2]:
                    a = '00010'

                    for i in reg:
                        if value[1] == i:
                            b = reg[i]

                    c = value[2][1:]
                    # cc=bin(int(c))
                    binv = bin(int(c)).replace("0b", "")
                    l = len(str(binv))
                    dif = 8 - l
                    q = str(0) * dif + str(binv)
                    # print(q)

                    print(a + b + q)

            else:
                if value[0] != 'mov':
                    for i in opcode_table:
                        if value[0] == i:
                            a = opcode_table[i][0]

                    for i in reg:
                        if value[1] == i:
                            b = reg[i]

                    c = value[2][1:]
                    # cc=bin(int(c))
                    binv = bin(int(c)).replace("0b", "")
                    l = len(str(binv))
                    dif = 8 - l
                    q = str(0) * dif + str(binv)
                    # print(q)

                    print(a + b + q)

        elif value[0] in typeC:
            if value[0] == 'mov':
                if '$' not in value[2]:
                    a = "00011"

                    b = '00000'

                    for i in reg:
                        if value[1] == i:
                            c = reg[i]

                    for i in reg:
                        if value[2] == i:
                            d = reg[i]

                    print(a + b + c + d)

            else:
                for i in opcode_table:
                    if value[0] == i:
                        a = opcode_table[i][0]

                b = '00000'

                for i in reg:
                    if value[1] == i:
                        c = reg[i]

                for i in reg:
                    if value[2] == i:
                        d = reg[i]

                print(a + b + c + d)

        elif value[0] in typeD:
            for i in opcode_table:
                if value[0] == i:
                    a = opcode_table[i][0]

            for i in reg:
                if value[1] == i:
                    b = reg[i]

            for i in input_dict:
                if value[2] == input_dict[i][0]:
                    c = bin(i)
                    binv = bin(int(i)).replace("0b", "")
                    l = len(str(binv))
                    dif = 8 - l
                    q = str(0) * dif + str(binv)

            print(a + b + q)
        elif value[0] in typeE:
            for i in opcode_table:
                if value[0] == i:
                    a = opcode_table[i][0]

            b = '000'

            for i in input_dict:
                if value[1] == input_dict[i][0]:
                    c = bin(i)
                    binv = bin(int(i)).replace("0b", "")
                    l = len(str(binv))
                    dif = 8 - l
                    q = str(0) * dif + str(binv)

                else:
                    for r in label_dict:
                        if value[1] == r:
                            c = label_dict[r]
                            binv = bin(int(c)).replace("0b", "")
                    l = len(str(binv))
                    dif = 8 - l
                    q = str(0) * dif + str(binv)

            print(a + b + q)

        elif value[0] == 'hlt':
            a = '10011'
            b = '00000000000'
            print(a + b)

        elif value[0] == 'mov':
            if '$' in value[2]:
                a = '00010'

                for i in reg:
                    if value[1] == i:
                        b = reg[i]

                c = value[2][1:]
                # cc=bin(int(c))
                binv = bin(int(c)).replace("0b", "")
                l = len(str(binv))
                dif = 8 - l
                q = str(0) * dif + str(binv)

                print(a + b + q)
            else:
                a = "00011"
                b = '00000'

                for i in reg:
                    if value[1] == i:
                        c = reg[i]

                for i in reg:
                    if value[2] == i:
                        d = reg[i]

                print(a + b + c + d)


        elif ':' in value[0]:

            a = key
            del input_dict[a][0]
            #  print(input_dict)
            w = {a: input_dict[a]}
            printing(w, label_dict)




