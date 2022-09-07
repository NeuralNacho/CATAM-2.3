from q1and2_functions import modulus_plot, find_r, find_decimal
import math
import cmath

modulus_plot(0, 2, lambda z: z**3 - z**2 + (2-1j)*z - 1 - 1j)

# Use different start, end pairs in programming task 1
r1, z = find_r(0.6)
print(r1, z, cmath.phase(z))  # phase is arg
r2, z = find_r(1.4)
print(r2, z, cmath.phase(z))
r3, z = find_r(1.6)
print(r3, z, cmath.phase(z), '\n')

r, z = find_decimal(0.61803, 5, lambda z: z**3 - z**2 
            + (2-1j)*z - 1 - 1j, (0.5 - 0.1)*math.pi, 
            (0.5 + 0.1)*math.pi, 2*math.pi/350000)
arg = cmath.phase(z)
print(r, z, arg)
print(r1*math.cos(arg), r1*math.sin(arg))
r, z = find_decimal(1.41421, 5, lambda z: z**3 - z**2 
                + (2-1j)*z - 1 - 1j, (0.25 - 0.1)*math.pi, 
                (0.25 + 0.1)*math.pi, 2*math.pi/350000)
arg = cmath.phase(z)
print(r, z, arg)
print(r2*math.cos(arg), r2*math.sin(arg))
r, z = find_decimal(1.61803, 5, lambda z: z**3 - z**2 
                + (2-1j)*z - 1 - 1j, (1.5 - 0.1)*math.pi, 
                (1.5 + 0.1)*math.pi, 2*math.pi/350000)
arg = cmath.phase(z) + 2*math.pi
print(r, z, arg)
print(r3*math.cos(arg), r3*math.sin(arg))
# Smaller step size giving more accuracy
# Smaller arc used for fast calculation