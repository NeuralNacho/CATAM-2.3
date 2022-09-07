import matplotlib.pyplot as plt
import math
import cmath
import numpy as np

from programming_task_1 import generate_points

r_list = [0.1, 0.5, 0.75, 1, 1.25, 5]
subplot_no = 1
for i in range(6):
    z_in, w_out = generate_points(r_list[i], 
                            lambda z: z**3 + z)
    plt.subplot(2, 3, i+1)
    plt.plot(w_out.real, w_out.imag, antialiased=True, 
                                        color = 'green')
    # plt.xlabel('$Re$')
    # plt.ylabel('$Im$')
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.title('$r = %.2f$' %r_list[i])
plt.show()


# first plot the circle arcs
plt.rc('font', size = 20)
r = 0.75
vf = np.vectorize(lambda z: z**3)
z_in = []
for counter in range(2001):
    # range is number of points in plot
    z_in.append(r*cmath.exp((0.5*math.pi*(1/2000)*counter)*1j))
z_in = np.array(z_in)
w_out = vf(z_in)
plt.subplot(1, 2, 1)
plt.plot(w_out.real, w_out.imag, color = 'green')
vf = np.vectorize(lambda z: z)
z_in = []
for counter in range(2001):
    # range is number of points in plot
    z_in.append(r*cmath.exp((0.5*math.pi*(1/2000)*counter)*1j))
z_in = np.array(z_in)
w_out = vf(z_in)
plt.plot(w_out.real, w_out.imag, color = 'orange')
# now plot some dashed lines
p1, q1, s1 = r**3, (r**3)*cmath.exp((3*math.pi/4)*1j), \
                    (r**3)*cmath.exp((3*math.pi/2)*1j)
p2, q2, s2 = r, r*cmath.exp((math.pi/4)*1j), \
                    r*cmath.exp((math.pi/2)*1j)
plt.plot([p1.real, p2.real], [p1.imag, p2.imag], 
            linestyle = 'dashed', color = 'black')
plt.plot([q1.real, q2.real], [q1.imag, q2.imag], 
            linestyle = 'dashed', color = 'black')
plt.plot([s1.real, s2.real], [s1.imag, s2.imag], 
            linestyle = 'dashed', color = 'black')
plt.xlabel('$Re$')
plt.ylabel('$Im$')
plt.grid(linestyle = '--', linewidth = 0.5)
#next plot image
vf = np.vectorize(lambda z: z**3+z)
z_in = []
for counter in range(2001):
    # range is number of points in plot
    z_in.append(r*cmath.exp((0.5*math.pi*(1/2000)*counter)*1j))
z_in = np.array(z_in)
w_out = vf(z_in)
plt.subplot(1, 2, 2)
plt.plot(w_out.real, w_out.imag)
plt.xlabel('$Re$')
plt.ylabel('$Im$')
plt.grid(linestyle = '--', linewidth = 0.5)
plt.show()
