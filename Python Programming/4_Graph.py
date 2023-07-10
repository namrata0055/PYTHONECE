import numpy as np
import matplotlib.pyplot as plt
import random
class Plot:
    def GraphicalPlot():
        x_axis=np.random.randint(20,40,10) #generate 10 nos b/w 20 to 40
        y_axis=np.random.randint(20,50,10)
        print("X axis values: ",x_axis)
        print("Y axis values: ",y_axis)
        plt.plot(x_axis,marker="o",mfc="yellow",mec="black",color="blue")
        plt.plot(y_axis,marker="o",mfc="lime",mec="red",color="maroon")
        plt.grid(color="coral")
        plt.show()
Plot.GraphicalPlot()