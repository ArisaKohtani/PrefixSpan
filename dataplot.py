import matplotlib.pyplot as plt
import numpy as np


x1 = np.array([2,2,2])
y1 = np.array([0.25, 0.5, 0.75])
z1 = np.array([85.19, 2.759, 0.2906])

x2 = np.array([3,3,3])
y2 = np.array([0.25, 0.5, 0.75])
z2 = np.array([740.1, 31.64, 2.675])

x3 = np.array([4,4])
y3 = np.array([0.5, 0.75])
z3 = np.array([953.4, 36.96])

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection' : '3d'})

ax.set_xlabel("the number of data(10^n")
ax.set_ylabel("minsup")
ax.set_zlabel("execute time(s)")

ax.plot(x1, y1, z1, color = "red",label=f'num={100}')
ax.plot(x2, y2, z2, color = "blue",label=f'num={1000}')
ax.plot(x3, y3, z3, color = "green",label=f'num={10000}')
ax.set_zscale('log')
ax.view_init(elev= 5, azim=-10)
plt.legend()
plt.show()
