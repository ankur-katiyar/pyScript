import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

rv = np.random.standard_normal(1000)

fig, ax = plt.subplots()
ax.hist(rv, bins=30)
fig
