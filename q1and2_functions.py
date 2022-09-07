import numpy as np
import matplotlib.pyplot as plt
import math

from programming_task_1 import generate_points, find_closest


def modulus_plot(r_start, r_end, func):  
    # plots graph showing shortest modulus for different r
    r_list = np.linspace(r_start, r_end, 100)  
    # 100 points used between start and end
    r_modulus_list = []
    for r in r_list:
        z_in, w_out = generate_points(r, func)  # change for Q2
        smallest_modulus = find_closest(z_in, w_out)[0]
        r_modulus_list.append(smallest_modulus)

    r_modulus_list = np.array(r_modulus_list)
    plt.plot(r_list, r_modulus_list, color = 'orange')
    plt.xticks(np.arange(r_start, r_end, 0.2))
    plt.xlabel('r', fontsize = 14)
    plt.ylabel('Modulus of closest point to $0+0i$', 
                                        fontsize = 14)
    # change step size for plots in q1 and q2
    plt.show()  


def find_decimal(start, decimal_place, func, begin = 0, 
                end = 2*math.pi, step = 2*math.pi/10000):
    # finds next decimal of r which minimising smallest modulus
    # begin, end, no_points used in generate_points function
    r_list = np.linspace(start - 0.1**(decimal_place), 
                        start + 0.1**(decimal_place), 21) 
    # 20 next decimal points between start and end tested
    smallest_modulus = math.inf
    optimal_r = start
    optimal_z = 0  # this will be the actual root
    for r in r_list:
        z_in, w_out = generate_points(r, func, begin, end, step)
        modulus, _, input_point = find_closest(z_in, w_out)
        if modulus < smallest_modulus:
            smallest_modulus = modulus
            optimal_r = r
            optimal_z = input_point
        # finds smallest modulus for all values of r in list
    return optimal_r, optimal_z

def find_r(start, func = lambda z: 
        z**3 - z**2 + (2-1j)*z - 1 - 1j):  
    # know start to 0 d.p
    for decimal in range(4):
        start, z = find_decimal(start, decimal + 1, func)
    return start, z
