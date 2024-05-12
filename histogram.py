import numpy as np
import matplotlib.pyplot as plt

pp = np.random.uniform(0.0, 5.0, 250)

plt.hist(pp,5)
plt.show()

#Histogram Explained
#We use the array from the example above to draw a histogram with 5 bars.

#The first bar represents how many values in the array are between 0 and 1.

#The second bar represents how many values are between 1 and 2.

#Etc.