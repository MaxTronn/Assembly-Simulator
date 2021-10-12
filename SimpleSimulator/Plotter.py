#Print 2 points in case of ld and st instructions

import matplotlib.pyplot as plt
import numpy as np

def generate_plot(pc_list, st_ld_dict):

    st_ld_arr = []
    st_ld_cycle_arr = []
    for k in st_ld_dict.keys():
        st_ld_arr.append(st_ld_dict[k])
        st_ld_cycle_arr.append(k)

    cycle_arr = list(range(0, len(pc_list)))
    pc_list.extend(st_ld_arr)

    cycle_arr.extend(st_ld_cycle_arr)

#    print((pc_list))
#    print((cycle_arr))

    y = np.array(pc_list)
    x = np.array(cycle_arr)

    axes = plt.axes()
    axes.set_ylim([-0.5, max(pc_list)+0.5])
    axes.set_xlim([-0.5, len(pc_list)+0.5])
    
    plt.scatter(x,y)

    plt.title("Memory Accesses v/s Cycles")
    plt.xlabel("Cycle")
    plt.ylabel("Address")
    plt.savefig("Graph1.png")
    plt.show()
    
#generate_plot([1,2,3,2,1,3,2,3,2,5,6,8,2,4,5])
