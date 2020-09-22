import matplotlib

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np

matplotlib.use("TkAgg")

class Plotter:
    def __init__(self, x_min, x_max, dx = 0.01):
        self.x_array = np.arange(x_min, x_max, dx) #Creating the x axis array
        self.x_lim = (x_min, x_max)
        self.fig = plt.figure()

    def function(self):
        """Calculates the y_array from x_array through
        the function in question"""
        lambd = 5*np.sin(2*np.pi*self.x_array)
        return 3*np.pi*np.exp(-lambd)

    def plot_func(self, x_label = None, y_label = None):
        """Plotting the function"""


        axcolor = 'lightgoldenrodyellow'
        #axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
        #axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

        #sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=5, valstep=0.01)
        #samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=3)

        plt.plot(self.x_array, self.function())
        plt.grid()
        plt.show()

def main():
    plot = Plotter(0.5, 1.2)
    plot.plot_func()

if __name__ == '__main__':
    main()
