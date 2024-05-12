import numpy as np
import matplotlib.pyplot as plt

pp = np.random.uniform(0.0, 5.0, 100000)

plt.hist(pp, 100)
plt.show()