import matplotlib.pyplot as plt
import numpy as np

def probability_plot_builder(data,filename = None):
    fig, ax = plt.subplots()
    time = list(data.keys())
    percentage = list(data.values())
    ax.barh(time,percentage)
    fig.savefig(filename)
    fig.show()
