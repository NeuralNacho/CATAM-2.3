import math
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np
from programming_task_2 import k_tot

function_names = ['f_1(z)', 'g(z)', 'h(z)']
function_derivates = [lambda z : 3*z**2 - 2*z + 2 - 1j, 
    lambda z : 3*z**2 + 1, lambda z : 3*z**2 - 2*z - 1]
function_2nd_derivates = [lambda z : 6*z - 2, lambda z : 
                                6*z, lambda z : 6*z - 2]
colors = ['orangered', 'green', 'dodgerblue']


for i in range(3):
    r_max = 2
    r_array = []
    k_tot_array = []
    for c in range(400):
        r = r_max * (c+1) / 400  # c+1 so r = 0 not included
        r_array.append(r)
        k_tot_array.append(k_tot(r, function_derivates[i], 
                            function_2nd_derivates[i])[0])
    plt.subplot(1, 3, i+1)
    plt.plot(r_array, (1 / math.pi) * np.array(k_tot_array), 
                                        color = colors[i])
    ax = plt.gca()
    ax.yaxis.set_major_formatter \
        (tck.FormatStrFormatter('%g $\pi$'))
    ax.yaxis.set_major_locator \
        (tck.MultipleLocator(base=2))
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.xlabel('r')
    plt.ylabel('$\kappa_{tot}$')
    plt.title('$%s$' %function_names[i])
plt.show()