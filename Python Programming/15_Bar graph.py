import matplotlib.pyplot as plt
import numpy as np
class Bargraph:
    def Plot():
        x_ax_1=[2,4,6,8,10,12,14,16,18,20]
        y_ax_1=np.random.randint(10,50,10)
        plt.bar(x_ax_1,y_ax_1)
        plt.show()
Bargraph.Plot()