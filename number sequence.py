import matplotlib.pyplot as plt
import numpy as np
res = 50
x = np.linspace(0,res,num=res+1)
y = x**2+3*x-4

plt.scatter(x,y)
plt.grid(True)

y_min = np.min(y)
y_max = np.max(y)
plt.axis([0-1,res+1,y_min-abs(y_min*0.1),y_max+y_max*0.1])


for i, j in zip(x,y):
    plt.text(i,j+0.7,'({},{})'.format(i,j))

#plt.plot(x,np.log(x))
plt.show()



