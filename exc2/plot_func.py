import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np

class Plotter:
        """Takes x min and x max as argument, also the increment in the x-axis
        for when calculating y values. """
    def __init__(self, x_min, x_max, dx = 0.01):
        self.x_array = np.arange(x_min, x_max, dx) #Creating the x axis array
        self.x_lim = (x_min, x_max)
        self.fig = plt.figure()

    def function(self):
        """Calculates the y_array from x_array through
        the function in question"""
        lambd = 5*np.sin(2*np.pi*self.x_array) #The function in question
        return 3*np.pi*np.exp(-lambd)

    def plot_func(self, x_label = None, y_label = None):
        """Plotting the function"""
        plt.plot(self.x_array, self.function())
        plt.grid()          #Grid on
        plt.show()

def main():
    """Test function for the class"""
    plot = Plotter(0.5, 1.2)
    plot.plot_func()

if __name__ == '__main__':
    main()
