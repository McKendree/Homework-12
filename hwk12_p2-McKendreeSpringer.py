import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import sys

if __name__ == "__main__":
    I = 51 #starting x position
    j = 51 #starting y position

    xCoord = []
    yCoord = []

    #creates figure
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)

    counter = 0
    def animate(i):
        global counter
        global I
        global j
        
        if counter >= 10000:
            #stops after 10000 steps and plots full particle path
            plt.plot(xCoord, yCoord)
            plt.title('Brownian Motion')
            plt.axis([0,101,0,101])
            plt.savefig('Brownian_Motion.png')
            sys.exit()

        #plots new position
        ax1.clear()
        ax1.scatter(I,j,c='purple')
        ax1.axis([0,101,0,101])
        ax1.grid()

        xCoord.append(I)
        yCoord.append(j)
        
        #chooses random direction to move
        rand = random.choice(['north','south','east','west'])
        if rand == 'north':
            if j != 101:
                j += 1
                counter += 1
        if rand == 'south':
            if j != 1:
                j -= 1
                counter += 1
        if rand == 'east':
            if I != 101:
                I += 1
                counter += 1
        if rand == 'west':
            if I != 1:
                I -= 1
                counter += 1

    #animates and shows figure
    ani = animation.FuncAnimation(fig,animate,interval=1)
    plt.title('Brownian Motion')
    plt.show()
    plt.clf()
