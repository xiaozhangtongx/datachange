# （行值，列值，密度值）三维可视化
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

pd = pd.read_csv("res/D.csv", names=["x", "y", "count", "lable"])

x = np.array(pd['x'])
y = np.array(pd['y'])
z = np.array(pd['count'])

# fig = plt.figure()
# ax3d = Axes3D(fig)
# surf = ax3d.plot_surface(x, y, z, cmap="rainbow", linewidth=0, antialiased=False)
# fig.colorbar(surf, shrink=0.5, aspect=5)
fig = plt.figure()
ax3d = Axes3D(fig)
ax3d.set_zlim(0, 10)
ax3d.scatter(x, y, z, marker=".")

plt.show()
