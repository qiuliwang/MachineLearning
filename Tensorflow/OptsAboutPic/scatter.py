import numpy as np
import matplotlib.pyplot as plt

z=np.random.randn(100,2)
print z
z[:,1]=0.5*z[:,0]+np.sqrt(0.5)*z[:,1]
x=z[:,0];
y=z[:,1];
#plt.scatter(x,y);
plt.scatter(x,y,marker='s',c='r');
plt.show()