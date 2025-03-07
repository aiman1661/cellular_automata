"""
Running a set of simulations to calculate the average infection wrt
immune fraction.

author: s2229553
"""

import sys
import numpy as np
from numpy import random
from SIRS_class import SIRS_Lattice

def main():
    # Read inputs from command lines
    if len(sys.argv) != 4 :
        print("You left out the name of the files when running.")
        print("In command line, run like this instead:")
        print(f"% nohup python {sys.argv[0]} <iterations> <resolution> <output .npy file name> > output.txt &")
        print("For example:")
        print("% nohup python SIRS_immune_sim.py 1100 0.2 measurements > output.txt &")
        sys.exit(1)
    else:
        iterations = int(sys.argv[1]) 
        resolution = float(sys.argv[2])
        outfile = str(sys.argv[3])

    # parameters
    N = 50
    n_step = iterations
    p1 ,p2, p3 = [.5]*3
    frac_im_step = np.arange(0., 1. + resolution, resolution) # immunisation

    I_array = []

    print('Begininning simulation... \n')
    for frac_im in frac_im_step:
        print(f'Simulating with immune fraction: {frac_im}')
        # initialisation step
        lattice = random.randint(low=-1, high=2, size=(N,N)) # randomly initialise lattice
        system = SIRS_Lattice(lattice)

        # promote some sites to be immune
        lattice = system.get_lattice_immune(frac_im)
        system = SIRS_Lattice(lattice)

        I_fraction_array = []

        for _ in range(n_step):
            for _ in range(N**2):
                site = random.choice(N,2)
                bool_test, updated_site, updated_state = system.update_step(site, p1,p2,p3)

                i, j = updated_site

                if bool_test:
                    lattice[i][j] = updated_state
                    system = SIRS_Lattice(lattice)

            I_frac = system.get_I_fraction()
            I_fraction_array.append(I_frac) 

        I_average = system.get_I_average(np.array(I_fraction_array))

        print(f'Average Infection (Fraction): {I_average} \n')
        
        I_array.append(I_average)

    data = {"I_average": np.array(I_array),
            "im_frac": frac_im_step
            }

    # to-do
    np.save(outfile, data)

    print('Job Done! :)')
    print(f'Check directory for {outfile}.npy file. Data analysis can be done by using np.load. \n')

if __name__ == '__main__':
    main()  