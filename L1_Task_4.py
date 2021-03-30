import numpy as np
import matplotlib.pyplot as plt
x = np.linespace(0, 10, 400)
plt.plot(x, np.cos(1*x))
plt.plot(x, np.cos(17*x))
plt.show()
