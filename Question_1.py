import numpy as np
import matplotlib.pyplot as plt

from programming_task_1 import generate_points, find_closest

r_list = np.linspace(0, 2, 100)
r_modulus_list = []
for r in r_list:
    z_in, w_out = generate_points(r)
    smallest_modulus = find_closest(z_in, w_out)[0]
    r_modulus_list.append(smallest_modulus)
    np.array(r_modulus_list)

plt.plot(r_list, r_modulus_list)
plt.show()