import matplotlib.pyplot as plt

n = [6, 7, 8, 9, 10, 11, 12]
t = [0, 0.01, 0.1, 0.99, 11.13, 135.84, 1709.66]

n1 = [6, 7, 8, 9, 10, 11, 12]
t1 = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]

fig, ax = plt.subplots()
ax.plot(n, t, marker='o', mfc='w', mec='r', label='Brute Force')
ax.plot(n1, t1, marker='o', mfc='w', mec='r', label='Heuristic')
ax.set_xlabel('n')
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
#legend.get_frame().set_facecolor('C0')
#ax.set_yscale('log')
ax.set_ylabel('Time (s)')
plt.show()