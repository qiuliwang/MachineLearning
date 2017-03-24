"""
WangQL
"""
import numpy as np
import matplotlib.pyplot as plt

y=np.random.randn(100)
plt.plot(y, label='line label', color='r', linestyle='-', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title(u'title')
plt.show()