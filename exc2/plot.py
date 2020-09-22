import matplotlib
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np

class Plotter:
    def __init__(self, x_min, x_max, dx = 0.001):
        self.x_array = np.arange(x_min, x_max, dx) #Creating the x axis array
        self.x_lim = (x_min, x_max)
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)

    def function(self, offset = 0):
        """Calculates the y_array from x_array through
        the function in question"""
        lambd = 5*np.sin(2*np.pi*self.x_array)
        return 3*np.pi*np.exp(-lambd*np.sin(0.01*offset + np.pi/2))

    def plot_func(self, x_label = None, y_label = None):
        """Animating the function"""
        anim = FuncAnimation(self.fig, self.animate, init_func = self._init,
                             frames=1000, interval=20, blit=True)

        plt.xlim(self.x_lim)
        plt.ylim(0,1500)
        plt.grid()
        #plt.title("These curves though")
        plt.show()

    def _init(self):
        self.line.set_data([], [])
        return self.line,

    def animate(self, offset):
        self.line.set_data(self.x_array, self.function(offset))
        return self.line,

def main():
    plot = Plotter(0.5, 5)
    plot.plot_func()

if __name__ == '__main__':
    main()
