# Try running this program.
# Then change it to generate another subplot with the product of y1 and y2.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

plt.figure()

t = np.arange(0.0, 5.0, 0.1)  # try printing t

plt.subplot(311)
y1 = np.exp(-t)
plt.plot(t, y1, 'b')  # try 'g' or 'bo' or 'k+'

plt.subplot(312)
y2 = np.cos(2*np.pi*t)
plt.plot(t, y2, 'ro-')

plt.subplot(313)
y3 = y1*y2
plt.plot(t, y3, 'go-')

plt.show()

