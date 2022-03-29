import matplotlib.pyplot as plt
import numpy as np
import cmath


def generate_points(r):
    f_z = lambda z : z**3 - z**2 + (2-1j)*z - 1 - 1j
    vf_z = np.vectorize(f_z)

    z_in = []
    for counter in range(1001):  # number is number of points in plot
        z_in.append(r*cmath.exp((2*cmath.pi*counter)*1j / 1000))
    z_in = np.array(z_in)
    w_out = vf_z(z_in)
    return z_in, w_out


def find_closest(z_in, w_out):
    smallest_modulus = float('inf')
    closest_point = 0
    index = 0  # for finding inputted value of z
    for point in w_out:
        modulus = abs(point)
        if modulus < smallest_modulus:
            smallest_modulus = modulus
            closest_point = point
            closest_point_input = z_in[index]
        index += 1
    return smallest_modulus, closest_point, closest_point_input


r = input('Enter radius r: ')
r = float(r)

z_in, w_out = generate_points(r)
smallest_modulus, closest_point, closest_point_input = find_closest(z_in, w_out)
print('Closest point to 0+0i is : ', closest_point)
print('Modulus of closest point is:', smallest_modulus)


plt.plot(w_out.real, w_out.imag)
plt.xlabel('$Re$')
plt.ylabel('$Im$')
plt.grid(linestyle = '--', linewidth = 0.5)
plt.show()
