import matplotlib
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import time, math
import numpy as np

class Plotter:
    def __init__(self, x_min=0, x_max=10, dx = 0.001,
                       y_min=0, y_max=10, rate = 0.01):
        self.rate = rate
        plt.xlim(x_min, x_max)
        plt.ylim(y_min)
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)
        self.data = ([], [])

    def plot_data(self):
        """Plotting data"""
        plt.grid()
        plt.title("These curves though")

    def update(self, data):
        """Updates the data in the plot and the plot itself. useful for live
        data tracking. """
        self.data[0].append(data[0])
        self.data[1].append(data[1])
        self.line.set_data(self.data)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.plot(data[0], data[1])
        plt.draw()
        time.sleep(self.rate)

    def animation(self, offset):
        self.line.set_data(self.x_array, self.function(offset))
        return self.line,

def main():
    plt.ion()

    plot = Plotter(0, 50, rate = 0.1)
    plot.plot_data()
    for i in range(20):
        print(i, math.sin(i))
        plot.update((i, math.sin(i)))


if __name__ == '__main__':
    main()
