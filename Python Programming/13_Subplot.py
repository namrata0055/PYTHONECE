import matplotlib.pyplot as plt
import numpy as np
class Subplot:
    def Plot():
        x_ax_1=np.random.randint(10,50,10)
        y_ax_1=np.random.randint(10,50,10)
        plt.subplot(2,2,1)              #2 rows, 2 columns, 1st pos
        plt.plot(x_ax_1,y_ax_1, marker="o", mfc="red")

        x_ax_2=np.random.randint(10,50,10)
        y_ax_2=np.random.randint(10,50,10)
        plt.subplot(2,2,2)              
        plt.scatter(x_ax_2,y_ax_2)

        x_ax_3=np.random.randint(10,50,10)
        plt.subplot(2,2,3)              
        plt.pie(x_ax_3)

        x_ax_4=np.random.randint(10,50,10)
        y_ax_4=np.random.randint(10,50,10)
        plt.subplot(2,2,4)              
        plt.plot(x_ax_4,y_ax_4, marker="o", mfc="red")

        plt.show()
Subplot.Plot()