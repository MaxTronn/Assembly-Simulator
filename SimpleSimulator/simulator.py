import ipreader
import Processing
import simprint
from sys import stdin

input_dict={}
input_list=[]
#pc_list = [0,]
def pa():
    pc=0
    for line in stdin:
        #$input_lineno+=1
        if line == "\n":
            break

        input_dict.update({pc: line})
        input_list.append(line)
        pc += 1

pa()
#print(input_dict)
#print(input_list)

#for x in range(len(input_list)):
#    ipreader.input_reader(input_list[x])

#ctr = 0
#while True:
#    if ctr>len(input_dict):
#        break
#
#    ipreader.input_reader(input_list[pc_list[ctr]])


'''
m=Processing.mem_list

n=simprint.memdmp(m)

for c in range(len(input_list)):
    n[c]=input_list[c]

for v in n:
    print(v)
#simprint.memdmp(m)
'''

