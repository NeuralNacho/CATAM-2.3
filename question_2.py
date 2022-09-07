from q1and2_functions import modulus_plot, find_decimal, find_r
import math
import cmath

modulus_plot(0.6, 1.2, lambda z: 3*z**2 - 2*z + 2 - 1j)
# From this is is obvious the roots are roughly 0.8, 0.95

r, z = find_r(0.7, lambda z: 3*z**2 - 2*z + 2 - 1j)
print(r, z, cmath.phase(z))
r, z = find_r(0.9, lambda z: 3*z**2 - 2*z + 2 - 1j)
print(r, z, cmath.phase(z), '\n')

r1, z = find_decimal(0.78470, 5, lambda z: 3*z**2 - 2*z + 2 - 1j, 
                4.86 - 0.1*math.pi, 4.86 + 0.1*math.pi, 
                2*math.pi/350000)
arg = cmath.phase(z)+2*math.pi
print(r1, z, arg)
print(r1*math.cos(arg), r1*math.sin(arg))
r2, z = find_decimal(0.94986, 5, lambda z: 3*z**2 - 2*z + 2 - 1j, 
                0.96 - 0.1*math.pi, 0.96 + 0.1*math.pi, 
                2*math.pi/350000)
arg = cmath.phase(z)+2*math.pi
print(r2, z, arg)
print(r2*math.cos(arg), r2*math.sin(arg))