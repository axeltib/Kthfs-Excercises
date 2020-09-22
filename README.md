This repo consists of the two excercises given by Kthfs; Kth Formula Student. I am most proficient in python, which is the language I wrote all the scripts and classes in.

## Excersise 1

To run the nodes you must first have rospy, installed by running the command in command window (I used Ubuntu):

```
sudo apt-get install python-rospy
```

Here two nodes were to be created, where one published to the topic 'tibbling', and the other listened to 'tibbling', and bouced a value, depending on the value from 'tibbling', to '/kthfs/result'.

Node a and b are both modifications of ROS.org's simple subscriber and publisher(guide)[http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29].

To run, you first have to run the roscore, which is done by running the command:

```
roscore
```

Then, to launch the nodes, you run the command (the same command is used to launch both nodes, but change "nodename" with a respectively b ) below for each node, in two instances:

```
rosrun package2 node_"nodename".py
```

To then see what is published to the topics in another instance, type the command

```
rostopic echo "name_of_topic"
```

or you can launch PlotJuggler or rqt_plot to get a graphical represantation. 


## Excersise 2

Here I have made three classes. One for simple one time plots, one for animation of a function, and lastly one for live data plotting.

To run all of these you will need matplotlib and numpy. These can be downloaded using

```
pip install numpy
pip install matplotlib
```

Alternetavely, use pip3 instead of pip.

When writing the one time plot class, I used matplotlib's [example](https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html) on simple plots.

When writing the animation class, I initially copied Jake Vanderplas'[code](https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/), and modified it to fit my purpose. Later, when it did not work I used [matplotlib's documentation for its animation api](https://matplotlib.org/api/animation_api.html), as a reference.

For the live update, I used [this](https://stackoverflow.com/questions/4098131/how-to-update-a-plot-in-matplotlib), from Stackoverflow, thread as a guide.

I run my programs through the ubuntu terminal, and had issue getting the plot window to come up. To solve this I installed [Xming](https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html), which runs a server on your computer that ubuntu can show windows through. It worked like a charm and I recommend it if you are having the same issue.  
