# coding=utf-8

# 2018-05-23 15:03

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import math

def generate_serial(n, k):
    if k == 0:
        return []
    
    a = [0] * n
    a[0] = 1
    
    sp = 0
    ep = 0
    s = 0.0
    while ep < n:
        while ep - sp < k:
            s += a[ep]
            ep += 1
            a[ep] = s / k
        
        a[ep] = s / k
        s += a[ep]
        s -= a[sp]
        sp += 1
        ep += 1
        
    return a

def render_serial_1(a):
    l = len(a)
    d_step = 2 * math.pi / l
    
    pts = []
    for i in range(1, l):
        x = i
        #y = -math.log(abs(a[i] - a[i - 1])) * (1 if a[i] > a[i - 1] else -1)
        y = a[i] - a[i - 1]
        
        p2 = [x, y]
        pts.append(p2)
        #plt.scatter(x, y)
    
    for i in range(1, len(pts)):
        plt.plot([pts[i - 1][0], pts[i][0]], [pts[i - 1][1], pts[i][1]], 'o-')
        
    plt.show()


def render_serial_2(a):
    
    l = len(a)
    d_step = 2 * math.pi / l
    
    deltas = []
    for i in range(1, l):
        y = -math.log(abs(a[i] - a[i - 1])) * (1 if a[i] > a[i - 1] else -1)
        deltas.append(y)
        #plt.scatter(x, y)
    
    pts = []
    for i in range(1, len(deltas)):
        x = i
        y = -math.log(abs(deltas[i] - deltas[i - 1])) * (1 if deltas[i] > deltas[i - 1] else -1)
        #y = deltas[i] - deltas[i - 1]
        
        p2 = [x, y]
        pts.append(p2)
        
    for i in range(1, len(pts)):
        plt.plot([pts[i - 1][0], pts[i][0]], [pts[i - 1][1], pts[i][1]], 'o-')
        
    plt.show()
    
    

def newline(p1, p2):
    ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if(p2[0] == p1[0]):
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmax-p1[0])
        ymin = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmin-p1[0])

    l = mlines.Line2D([xmin,xmax], [ymin,ymax])
    ax.add_line(l)
    return l


if __name__ == "__main__":
    a = generate_serial(200, 13)
    print a
    render_serial_1(a)
    #render_serial_2(a)
        
        
        
            
            
    