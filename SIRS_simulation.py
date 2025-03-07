"""
Running multiple random simulations to measure infection (fraction) average with fixed p2=0.5. 

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
        print("% nohup python SIRS_simulation.py 1100 0.05 measurements > output.txt &")
        sys.exit(1)
    else:
        iterations = int(sys.argv[1]) 
        resolution = float(sys.argv[2])
        outfile = str(sys.argv[3])

    # parameters
    N = 50
    n_step = iterations
    p1_step = np.arange(0, 1. + resolution, resolution)
    p2 = 0.5
    p3_step = np.arange(0, 1. + resolution, resolution)

    I_array = []
    I_squared_array = []
    var_array = []

    print('Begininning simulation... \n')
    for p1 in p1_step:
        I_array_row = []
        I_squared_array_row =[]
        var_array_row = []

        for p3 in p3_step:
            print(f'Simulating p1: {p1}, p3: {p3}')
            # random initialisation of system
            lattice = random.randint(low=-1,high=2,size=(N,N))
            system = SIRS_Lattice(lattice)

            I_fraction_array = []
            I_count_array = []

            for _ in range(n_step):
                for _ in range(N**2):
                    site = random.choice(N,2)
                    bool_test, updated_site, updated_state = system.update_step(site, p1,p2,p3)

                    i, j = updated_site

                    if bool_test:
                        lattice[i][j] = updated_state
                        system = SIRS_Lattice(lattice)
    
                # count infected number and fraction
                I_frac = system.get_I_fraction()
                I_fraction_array.append(I_frac) 
                _, I_count, _ = system.count_states()
                I_count_array.append(I_count)

            I_average = system.get_I_average(np.array(I_fraction_array))
            I_squared_average = system.get_I_squared_average(np.array(I_fraction_array))
            I_var = system.get_I_variance(np.array(I_count_array))

            print(f'Average Infection (Fraction): {I_average}')
            print(f'Average Infection (Fraction) Squared: {I_squared_average}')
            print(f'Variance Infection : {I_var} \n')

            I_array_row.append(I_average)
            I_squared_array_row.append(I_squared_average)
            var_array_row.append(I_var)
        
        I_array.append(I_array_row)
        I_squared_array.append(I_squared_array_row)
        var_array.append(var_array_row)

    data = {"I_average": np.array(I_array),
            "I_squared_average": np.array(I_squared_array),
            "I_variance": np.array(var_array)
            }

    # to-do
    np.save(outfile, data)

    print('Job Done! :)')
    print(f'Check directory for {outfile}.npy file. Data analysis can be done by using np.load. \n')

if __name__ == '__main__':
    main()  
