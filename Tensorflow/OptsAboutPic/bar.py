import numpy as np
import matplotlib.pyplot as plt

y=np.random.rand(5);
x=np.arange(5);
colors=['#FF0000','#FFFF00','#00FF00','#00FFFF','#0000FF']
plt.bar(x,y,width=0.5,color=colors,edgecolor='#000000',linewidth=5)
plt.show()