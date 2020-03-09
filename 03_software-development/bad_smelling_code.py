import numpy as np;import matplotlib.pyplot as plt
x=np.arange(10,0.2);y=np.sin(x)+3.0
plt.figure();plt.plot(x,y,'r')
plt.figure();plt.plot(x,y+np.random.randn(len(x)),'b')
z=np.sin(x)+3.0
plt.figure();plt.plot(x,y,'r')
plt.figure();plt.plot(x,z+np.random.randn(len(x)),'b')