import matplotlib.pyplot as plt
import numpy as np
import cmath


def generate_points(r, func, begin = 0, end = 2*cmath.pi, 
                                step = 2*cmath.pi/10000):
    # change begin and end for different sections of C_r
    # 0, 2 for full circle
    vf = np.vectorize(func)
    z_in = []
    no_points = round((end - begin)/step)
    for counter in range(no_points + 1):
        # range is number of points in plot
        z_in.append(r*cmath.exp((begin + step*counter)*1j))
    z_in = np.array(z_in)
    w_out = vf(z_in)
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


if __name__ == '__main__':  
    # ^ will not run when imported into other files
    r = input('Enter radius r: ')
    r = float(r)

    z_in, w_out = generate_points(r, lambda z: 
                    z**3 - z**2 + (2-1j)*z - 1 - 1j)
    smallest_modulus, closest_point, \
            closest_point_input = find_closest(z_in, w_out)
    print('Closest point to 0+0i is: ', closest_point)
    print('Modulus of closest point is:', smallest_modulus)

    plt.rc('font', size = 16)
    plt.plot(w_out.real, w_out.imag, color = 'black')
    plt.xlabel('$Re$')
    plt.ylabel('$Im$')
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.show()