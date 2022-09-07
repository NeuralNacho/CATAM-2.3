import math
import numpy as np
import matplotlib.pyplot as plt

from programming_task_1 import generate_points


def k_tot(r, f_prime, f_dprime):
    no_points = 1000 # increase for more accuracy
    z_array, f_prime_array = generate_points(r, 
            f_prime, step = 2*math.pi / no_points)
    f_dprime_array = generate_points(r, f_dprime, 
                step = 2*math.pi / no_points)[1]

    x_prime_array = 1j*f_prime_array*z_array
    x_dprime_array = -z_array*(f_prime_array + 
                        f_dprime_array*z_array)

    A = x_prime_array.real * x_dprime_array.imag 
    B =  x_prime_array.imag * x_dprime_array.real
    C = np.square(np.absolute(x_prime_array))
    integrand_array = np.divide(A - B, C, 
        out = np.zeros_like(A), where = C > 0.0001)
    # where condition eliminates (most) problems dividing by 0
    # where a small loops forst forms

    # trapezium rule:
    k_tot = ((2*math.pi / no_points)*(sum(integrand_array) -  \
            (integrand_array[0] + integrand_array[-1]) / 2))
    return k_tot, integrand_array

if __name__ == '__main__':
    k_t, integrand_array = k_tot(0.9, lambda z : 
        3*z**2 - 2*z + 2 - 1j, lambda z : 6*z - 2)
    plt.plot(integrand_array)
    plt.show()
    print(k_t)
