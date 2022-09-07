import matplotlib.pyplot as plt

from programming_task_1 import generate_points

r_list = [0.7, 0.9, 1.25, 2, 10]
loc_list = [(0, 0), (0, 4), (0, 8), (1,2), (1, 6)]
subplot_no = 1
for i in range(5):
    z_in, w_out = generate_points(r_list[i], 
        lambda z: z**3 - z**2 + (2-1j)*z - 1 - 1j)
    plt.subplot2grid(shape = (2, 12), loc = loc_list[i], 
                                            colspan = 3)
    plt.plot(w_out.real, w_out.imag, color = 'black')
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.title('$r = %.2f$' %r_list[i])
plt.show()