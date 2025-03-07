"""
Running multiple random simulations to measure time taken to reach equilibrium without visualisation.

author: s2229553
"""

import sys
import numpy as np
from numpy import random
from GameOfLife_class import GoL_Lattice

def main():
    # Read inputs from command lines
    if len(sys.argv) != 4 :
        print("You left out the name of the files when running.")
        print("In command line, run like this instead:")
        print(f"% nohup python {sys.argv[0]} <inner iterations> <outer iterations> <output .npy file name> > output.txt &")
        print("For example:")
        print("% nohup python GameOfLife_Simulation.py 500 500 measurements > output.txt &")
        sys.exit(1)
    else:
        inner_iterations = int(sys.argv[1]) 
        outer_iterations = int(sys.argv[2])
        outfile = str(sys.argv[3])

    # random initialisation
    N = 50
    #lattice = random.randint(low=0,high=2,size=(N,N))

    # set system
    #system = GoL_Lattice(lattice)

    outer_count_array = np.zeros((outer_iterations, inner_iterations))
    equilibrium_array = np.zeros(outer_iterations)
    print('Begininning simulation... \n')
    for i in range(outer_iterations):
        lattice = random.randint(low=0,high=2,size=(N,N))
        system = GoL_Lattice(lattice) # setting random initialised lattice

        print(f'Simulation number {i}')
        live_eq_counter = 0
        for j in range(inner_iterations):

            lattice_new = system.update_step()
            system = GoL_Lattice(lattice_new)

            live_sites = system.count_live()
            outer_count_array[i][j] = live_sites

            if j == 0:
                pass

            if j != 0:
                if outer_count_array[i][j] - outer_count_array[i][j-1] == 0: # checking for eq
                    live_eq_counter += 1
                else:
                    live_eq_counter = 0 # counter reset if not consecutive

                if live_eq_counter == 5: # criteria for eq
                    print(f'Simulation {i} reaches equilibrium!')
                    print(f'Equilibrium after {j-5} steps. \n')
                    equilibrium_array[i] = (j-5) 
                    break

                if j == (inner_iterations-1):
                    print(f'No equilibrium found in simulation {i}. \n')

    data = {"Equilibrium_Steps": equilibrium_array,
            "Simulation_data": outer_count_array
            }

    np.save(outfile, data)

    print('Job Done! :)')
    print(f'Check directory for {outfile}.npy file. Data analysis can be done by using np.load. \n')

if __name__ == '__main__':
    main()  
