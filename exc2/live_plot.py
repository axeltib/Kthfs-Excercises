
import matplotlib.pyplot as plt
import time, math
import numpy as np

class LivePlotter:
    "Used to live plot data. "
    def __init__(self, x_min=0, x_max=10, dx = 0.01,
                       y_min=0, y_max=10, rate = 0.01):
        self.rate = rate
        plt.xlim(x_min, x_max)
        plt.ylim(y_min)
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)
        self.data = ([], [])    #For exporting uses

    def init(self, title = "These curves though"):
        """Plotting data"""
        plt.grid()
        plt.title(title)

    def update(self, data):
        """Updates the data in the plot and the plot itself. useful for live
        data tracking. data should be a tuple on the form (x,y)."""
        self.data[0].append(data[0])
        self.data[1].append(data[1])
        plt.plot(data[0], data[1])

        self.line.set_data(self.data)
        #self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        time.sleep(self.rate)


def main():
    """Test function for the class."""
    plt.ion()

    plot = LivePlotter(0, 50, rate = 0.1)
    plot.init()
    for i in range(200):
        x = 0.1*i
        plot.update((x, math.sin(x)))


if __name__ == '__main__':
    main()
