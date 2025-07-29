import matplotlib.pyplot as plt
import numpy as np

maths=np.array([88,92,80,89,100,80,60,100,80,34])
science=np.array([35,79,79,48,100,88,32,45,50,30])


plt.scatter(maths,science)
plt.title('Scatter Plot')
plt.xlabel('Maths Marks')
plt.ylabel('Science Marks')
plt.grid(True)
plt.show()
