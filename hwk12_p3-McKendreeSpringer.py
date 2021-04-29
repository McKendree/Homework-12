import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    Bi213 = 10000 #initial atoms
    Tl209 = 0 #initial atoms
    Pb209 = 0 #initial atoms
    Bi209 = 0 #initial atoms

    hl_Bi213 = 2760 #half life in seconds
    hl_Tl209 = 132 #half life in seconds
    hl_Pb209 = 198 #half life in seconds

    timestep = 1 #second
    tmax = 20000 #maximum time in seconds
    times = np.arange(0,tmax,timestep)

    Bi213_decay = 1-2**(-timestep/hl_Bi213) #probability of decay over 1 second
    Tl209_decay = 1-2**(-timestep/hl_Bi213) #probability of decay over 1 second
    Pb209_decay = 1-2**(-timestep/hl_Bi213) #probability of decay over 1 second

    Bi213_list = []
    Tl209_list = []
    Pb209_list = []
    Bi209_list = []
    for time in times:
        Bi213_list.append(Bi213)
        Tl209_list.append(Tl209)
        Pb209_list.append(Pb209)
        Bi209_list.append(Bi209)
        for i in range(Pb209):
            if np.random.random()<Pb209_decay: #if atom decays
                Bi209 += 1
                Pb209 -= 1
        for i in range(Tl209):
            if np.random.random()<Tl209_decay: #if atom decays
                Pb209 += 1
                Tl209 -= 1
        for i in range(Bi213):
            if np.random.random()<Bi213_decay: #if atom decays
                if np.random.random()>0.0209:
                    Pb209 += 1
                    Bi213 -= 1
                else:
                    Tl209 += 1
                    Bi213 -= 1

    #plots the amount of each isotope is present over time
    plt.plot(times,Bi213_list,color='indigo')
    plt.plot(times,Tl209_list,color='cyan')
    plt.plot(times,Pb209_list,color='green')
    plt.plot(times,Bi209_list,color='red')
    plt.yscale('log')
    plt.legend(['Bi213','Tl209','Pb209','Bi209'])
    plt.title('Decay of Bi213 and its Daughter Isotopes')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Number of Atoms')
    plt.savefig('Decay_of_Bi213.png')
    plt.show()

