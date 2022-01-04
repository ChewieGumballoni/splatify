import ot
import random
import math
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

def getx(rad, angle):
    xvalue=rad*math.cos(angle)
    return xvalue

def gety(rad, angle):
    yvalue=rad*math.sin(angle)
    return yvalue

def f2b(list):
    list.append(list[0])
    return list

def main():
    # Parameters of initial and final states
    N=10
    m1 = .3
    m2 = .75
    s1 = 0.25
    s2 = .75
    numbites = 1000
    dT = 2*math.pi/numbites
    border = (max(m2,m1)+s2)*1.25
    Directory = "INSERT DIRECTORY PATH HERE"

    theta=[]
    test1=[]
    test2=[]
    x1=[]
    x2=[]
    y1=[]
    y2=[]


    #Make amplitude damper
    N_damp = 100
    duration = 1
    time_constant = duration*.1
    DR = 0.35
    lamb = 1/time_constant
    omega = lamb/DR
    t, A = [], []

    for q in range(0,N_damp):
        t.append(q*duration/N_damp)
        A.append(1-math.exp(-lamb*q*duration/N_damp)*math.cos(omega*q*duration/N_damp))

    plt.plot(t, A)
    plt.show()



    for a in range(0,N-1):
        theta.append(math.pi*2/(N)*a)
        test1.append(random.random()*s1 + m1)
        test2.append(random.random()*s2 + m2)
        x1.append(getx((test1[a]),(theta[a])))
        x2.append(getx((test2[a]),(theta[a])))
        y1.append(gety((test1[a]),(theta[a])))
        y2.append(gety((test2[a]),(theta[a])))

    #Close each loop
    test1.append(test1[0])
    test2.append(test2[0])
    x1.append(x1[0])
    x2.append(x2[0])
    y1.append(y1[0])
    y2.append(y2[0])
    theta.append(2*math.pi)

    R1, R2, T = [test1[0]], [test2[0]],[theta[0]]

    start = 0
    for bites in range(1, numbites):
        xbite = bites * dT
        # print(xbite, tList[start],rList[start])
        if xbite == theta[start]:
            start += 1
            T.append(xbite)
            R1.append(test1[start-1])
            R2.append(test2[start-1])
        elif xbite < theta[start]:
            xdist = theta[start] - theta[start - 1]
            ydist1 = test1[start] - test1[start - 1]
            ydist2 = test2[start] - test2[start - 1]
            R1.append((test1[start - 1] + (ydist1) * (1 - math.cos((xbite - theta[start - 1]) * math.pi / xdist)) / 2))
            R2.append((test2[start - 1] + (ydist2) * (1 - math.cos((xbite - theta[start - 1]) * math.pi / xdist)) / 2))
            T.append(xbite)
        else:
            start += 1
            xbite -= dT




    X2_PROJ = []
    Y2_PROJ = []

    for listitems in range(0,len(R1)):
        X2_PROJ.append(getx(R2[listitems],T[listitems]))
        Y2_PROJ.append(gety(R2[listitems],T[listitems]))


    for tok in range(0,len(t)):
        print(str(tok+1) +" of "+str(len(t)))
        X1_PROJ = []
        Y1_PROJ = []

        for listitems in range(0,len(R1)):
            X1_PROJ.append(getx(R1[listitems]+(R2[listitems]-R1[listitems])*A[tok],T[listitems]))
            Y1_PROJ.append(gety(R1[listitems]+(R2[listitems]-R1[listitems])*A[tok],T[listitems]))

        fig = plt.figure()
        ax = fig.add_subplot(111)

        plt.plot(X1_PROJ, Y1_PROJ,'r-')
        plt.plot(X2_PROJ, Y2_PROJ,'b-')
        plt.title("splatify")
        plt.xlabel("X")
        plt.ylabel("Y")

        plt.xlim([-border,border])
        plt.ylim([-border,border])
        ax.set_aspect('equal', adjustable='box')
        # plt.aspect('equal', adjustable='box')
        plt.savefig(Directory+"_"+str(tok)+'.png')
        plt.close('all')
    
if __name__ = '__main__':
    main()
