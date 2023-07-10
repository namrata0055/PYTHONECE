import matplotlib.pyplot as plt
import pandas as pd
class Dataframe():
    def dict_input():
        Sampdata = {}
        n = int(input("Enter number of entries: "))
        for i in range(n):
            k = input("Enter key: ")
            v = eval(input("Enter values: "))
            Sampdata[k] = v

        df = pd.DataFrame(Sampdata)
        df.to_csv("User_input_plot.csv")
        print("File created successfully")
        df.plot(marker = ".")
        plt.grid()
        plt.show()
        print(Sampdata)

Dataframe.dict_input()