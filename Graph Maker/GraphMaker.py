import numpy as np
import matplotlib.pyplot as plot
from matplotlib import style
import warnings
import sys
import getopt
import os

def main(argv):
    err = "Use Case: GraphMaker.py -l <limit> || -f <inputfile>optional[-t <title> -x <xlabel> -y <ylabel> -b <color>]"
    title = ""
    xlabel = ""
    ylabel = ""
    color = ""
    drawLine = False
    readFile = False
    path = ""
    limit = 0

    try:
        opts, args = getopt.getopt(argv, "l:t:x:y:b:f:")
    except getopt.GetoptError:
        print(err)
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-l":
            limit = int(arg)
        elif opt == "-t":
            title = arg
        elif opt == "-x":
            xlabel = arg
        elif opt == "-y":
            ylabel = arg
        elif opt == "-b":
            drawLine = True
            color = arg
        elif opt == "-f":
            readFile = True
            path = arg
        else:
            print(err)
            sys.exit(2)

    x = []
    y = []
    if limit > 0 and not readFile:
        for i in range(limit):
            x.append(float(input("X: ")))

        for i in range(limit):
            y.append(float(input("Y: ")))

        x = np.array(x)
        y = np.array(y)
        pred = line_of_bestFit(x, y)
        show_graph(x, y, pred, title, xlabel, ylabel, drawLine, color)
    elif readFile:
        file = open(path , "r")
        for i in file:
            if limit % 2 == 1:
                x.append(float(i))
            if limit % 2 == 0:
                y.append(float(i))
            limit += 1
        file.close()
        x = np.array(x)
        y = np.array(y)
        pred = line_of_bestFit(x, y)
        show_graph(x, y, pred, title, xlabel, ylabel, drawLine, color)
    else:
        print(err)
        sys.exit(2)

def show_graph(a, b, c, name, x, y, shouldDraw, paint):
    style.use("ggplot")
    plot.scatter(a, b)
    if shouldDraw:
        plot.plot(a, c, ''+paint)
    plot.xlabel(x)
    plot.ylabel(y)
    plot.title(name)
    plot.show()

def line_of_bestFit(a, c):
    with warnings.catch_warnings():

        warnings.simplefilter("ignore", category=RuntimeWarning)
        denominator = a.dot(a) - a.mean() * a.sum()
        m = ( a.dot(c - c.mean()) )/denominator
        b = ( (c.mean() * a.dot(a)) - (a.mean() * a.dot(c)) )/denominator
        y_pred = m * a + b

    return y_pred

if __name__ == "__main__":
    main(sys.argv[1:])