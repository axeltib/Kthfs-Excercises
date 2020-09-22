import numpy as np

f = open("sin_data.txt", "w")
for i in range(100):
    scaler = 0.1
    x = scaler*i
    f.write(str(round(x, 2)) + ", " + str(round(np.sin(x), 2)) + "\n")

f.close()
f = open("sin_data.txt", "r")
for line in f.readlines():
    data = line.split(", ")
    print(data)
