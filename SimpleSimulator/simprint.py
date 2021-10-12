# <PC (8 bits)><space><R0 (16 bits)><space>...<R6 (16 bits)><space><FLAGS (16 bits)>

#rg = [0, 1, 2, 3, -4, 5, 6, 7]  # for reference to be deleted #negative binary
#p = 2 # for reference to be deleted



def simprint(reg, pc):
    w = [0] * 8
    ii = pc
    biv = bin(int(ii)).replace("0b", "")
    l = len(str(biv))
    diff = 8 - l
    prg = str(0) * diff + str(biv)

    for x in range(len(reg)):
        if reg[x] < 0:
            i = ~reg[x]
            binv = bin(int(i)).replace("0b", "")
            l = len(str(binv))
            dif = 16 - l
            q = str(0) * dif + str(binv)
            

            inv = q

            inr = inv.replace('1', '2')

            inr = inr.replace('0', '1')

            inr = inr.replace('2', '0')



            w[x] = inr

        else:

            i = reg[x]
            binv = bin(int(i)).replace("0b", "")
            l = len(str(binv))
            dif = 16 - l
            q = str(0) * dif + str(binv)

            w[x] = q

    print(prg + ' ' + w[0] + ' ' + w[1] + ' ' + w[2] + ' ' + w[3] + ' ' + w[4] + ' ' + w[5] + ' ' + w[6] + ' ' + w[7])
    #print(Processing.plist)
    #print(Processing.mem_list)

#simprint(rg, p)  # for reference to be deleted

mem_list = [0] * 256  # for reference to be deleted


def memdmp(mem):

    lst=[]
    for x in range(len(mem)):
        i = mem[x]
        binv = bin(int(i)).replace("0b", "")
        l = len(str(binv))
        dif = 16 - l
        q = str(0) * dif + str(binv)
        lst.append(q)
    return lst


#memdmp(Processing.mem_list)  # for reference to be deleted
