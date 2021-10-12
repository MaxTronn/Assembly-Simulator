import opcode_table_3
import sampleprinting
from sys import stdin

#var_dict keeps track of all the variable and the order in which they were declared
#var_ctr keeps track of the order in which the variables were declared
#The value of variable in initialised to -1 in the beginning
#var_dict = { variable name : [var_ctr, value of variable]}
var_dict = {};
var_ctr = 0

#label_dict keeps track of all the labels
#label_dict = {label name(string) : label value(int)}
label_dict = {}

get_error = False

#jump_dict stores the input_lineno of jump instructions, so that we can print error at lineno statement in case
#a label is used but not defined
#jump_dict = { input_line : input_lst}
jump_dict={}



def passone():
    global get_error
    lineno = 0
    input_dict = {}

    # Input lineno keeps track of actual lineno in the input
    input_lineno = 0

    for line in stdin:
        input_lineno+=1
        if line == " ":
            break

        input_lst = line.split();

        if len(input_lst) == 0:
            continue

        # if error_found==true do not print binary
        get_error= opcode_table_3.error_check_op(line)


        if (get_error==True):
            print("Error found in Line Number :", input_lineno)
            break
        

        if input_lst[0] == "ld" or input_lst[0] == "st" :
            global var_dict
            if input_lst[2] not in var_dict.keys():
                print(" Error : Variable used before Declaration")
                print("Error found in Line Number :", input_lineno)
                get_error = True
                break

        if input_lst[0] == "var":

            if input_lst[1] in var_dict.keys():
                print("Error : Variable cannot be declared more than once")
                print("Error found in Line Number :", input_lineno)
                get_error = True
                break

            if input_lst[1] in label_dict.keys():
                print("Error : Variable Name and Label Name can't be same")
                print("Error found in Line Number :", input_lineno)
                get_error = True
                break

            global var_ctr
            var_ctr += 1
            var_dict.update({input_lst[1]: [var_ctr, -1]})

        if lineno>0 and ("hlt" in input_dict[lineno-1]):
            print("Error : hlt not being used as the last instruction")
            print("Error found in Line Number :", input_lineno-1)
            get_error=True
            break

        if input_lst[0] != "var":
            if (input_lst[0][-1] == ":"):
                if input_lst[0][:-1] in var_dict.keys():
                    print("Error : Variable Name and Label Name can't be same" )
                    print("Error found in Line Number :", input_lineno)
                    get_error = True
                    break

                if input_lst[0][:-1] in label_dict.keys():
                    print("Error : Label cannot be defined more than once")
                    print("Error found in Line Number :", input_lineno)
                    get_error = True
                    break

                label_dict.update({input_lst[0][0:-1]: lineno})

            if input_lst[0] == "jmp" or input_lst[0] == "jlt" or input_lst[0] == "jgt" or input_lst[0] == "je":
                if input_lst[1] in var_dict.keys():
                    print("Error : Variable Name and Label Name can't be same" )
                    print("Error found in Line Number :", input_lineno)
                    get_error = True
                    break

                jump_dict.update({input_lineno : input_lst})

            input_dict.update({lineno: input_lst})
            lineno += 1



    if get_error==False and lineno>0 and ("hlt" not in input_dict[lineno-1]):
        print("Error: Missing hlt instruction")
        print("Error found in Line Number :", input_lineno)
        get_error = True

    if get_error == False :
        for k in jump_dict.keys():
            if jump_dict[k][1] not in label_dict.keys():
                print("Error: Label used is not defined")
                print("Error found in Line Number :", k)
                get_error = True
                break


    if get_error == False :
        for i in range(1, var_ctr + 1):
            for k in var_dict.keys():
                if var_dict[k][0] == i:
                    var_dict[k][1] = lineno
                    input_dict.update({lineno: [k, ]})
                    lineno += 1
    '''
    print()

    for k, v in jump_dict.items():
        print(k, ":", v)

    print()
    
    for k,v in input_dict.items():
        print(k, ":", v)

    print()
    
    
    print()
    print()
    print("Initial var_dict : ")
    for k, v in var_dict.items():
        print(k, ":", v)

    print()
    print("input_dict : ")
    for k, v in input_dict.items():
        print(k, ":", v)

    
    print()
    print("Label_dict : ")
    for k,v in label_dict.items():
        print(k, ":", v)
    
    
#    print()
#    print("lineno =" , lineno)
    '''

    if (get_error == False):
        sampleprinting.printing(input_dict, label_dict)

passone()