import matplotlib.pyplot as plt
import numpy as np
x=np.array([35,25,25,15])
mylabels=["Apples", "Bananas", "Cherries", "Dates"]
myexplode=[0.4,0,0,0]

plt.pie(x, labels=mylabels, explode=myexplode, shadow=True)
plt.legend()
plt.show()