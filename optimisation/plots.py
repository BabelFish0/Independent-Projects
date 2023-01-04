import matplotlib.pyplot as plt

n = [6, 7, 8, 9, 10, 11, 12]
t = [0, 0.01, 0.1, 0.99, 11.13, 135.84, 1709.66]

fig, ax = plt.subplots()
ax.plot(n, t, marker='o', mfc='w', mec='r')
ax.set_xlabel('n')
ax.set_ylabel('Time (s)')
plt.show()