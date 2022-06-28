# Source: https://www.w3schools.com/python/trypython.asp?filename=demo_matplotlib_scatter

# Three lines to make our compiler able to draw:
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('Agg')


x = np.array([25, 17, 25, 29, 20, 15, 11, 17, 16, 16])
y = np.array([11, 11, 13, 9, 10, 7, 3, 8, 9, 4])

plt.scatter(x, y)
plt.show()

# Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
