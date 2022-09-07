import matplotlib.pyplot as plt

from programming_task_1 import generate_points

r_list = [0.1, 0.3, 0.75, 1, 1.05, 2.2, 4, 20]
subplot_no = 1
for i in range(8):
    z_in, w_out = generate_points(r_list[i], 
                lambda z: z**3 - z**2 - z + 1)
    plt.subplot(2, 4, i+1)
    plt.plot(w_out.real, w_out.imag, color = 'indigo')
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.title('$r = %.2f$' %r_list[i])
    # plt.annotate('origin', xy=(0, 0), xytext=(1, 0.5),
    #         arrowprops=dict(facecolor='black', shrink=0.01))
plt.show()