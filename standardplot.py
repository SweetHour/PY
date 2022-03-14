import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,3000)
#plt.plot(x, np.cosh(x)+np.sin(x)*1000)  !AQQQ`1`     # Plot the sine of each x point
plt.plot(x,np.square(x))
plt.plot(x,np.log(x))
plt.show()



