import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

if __name__ == "__main__":
    #rolls three 6-sided dice 10000 times
    numRolls = 100000
    rolls = np.random.randint(1,7,3*numRolls)
    sets = []
    for i in range(int(len(rolls)/3)):
        set = np.array([rolls[i*3],rolls[i*3+1],rolls[i*3+2]])
        sets.append(set)

    #tests probability of rolling three 6's
    counter = 0
    for set in sets:
        if set[0] == 6 and set[1] == 6 and set[2] == 6:
            counter += 1
    print('Estimated Probability of Rolling Three Sixes:', counter/numRolls*100, '%')

    #tests probability of rolling a sum of 11
    counter = 0
    for set in sets:
        if set.sum() == 11:
            counter += 1
    print('Estimated Probability of Rolling a Sum of 11:', counter/numRolls*100, '%')

    #creates list of sum values
    numSum = []
    for set in sets:
        numSum.append(set.sum())

    #plots sum frequency
    plt.hist(numSum, density=True, bins=16, )
    plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=1))
    plt.title('Probability of Sum for Three Six-Sided Dice')
    plt.xlabel('Sum')
    plt.savefig('ThreeDiceSum.png')
    plt.show()
