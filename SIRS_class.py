"""
Class containing the lattice system for SIRS.

author: S2229553
"""

import numpy as np
import SIRS_functions as func

class SIRS_Lattice():
    '''
    Lattice system
    '''

    def __init__(self, lattice):
        self.lattice = np.array(lattice)
        self.N = int(len(lattice))

    def update_step(self, site, p1, p2, p3):
        return func.update_step(self.lattice, site, p1, p2, p3)
    
    def count_states(self):
        return func.count_states(self.lattice)
    
    def get_I_fraction(self):
        _, count_I, _ = self.count_states()
        I_frac = count_I/(self.N**2)
        return I_frac
    
    def get_I_average(self, I_data):
        average = func.average_infection(I_data)
        return average
    
    def get_I_squared_average(self, I_data):
        average = func.average_infection_squared(I_data)
        return average
    
    def get_I_variance(self, I_data):
        return (self.get_I_squared_average(I_data) - (self.get_I_average(I_data))**2)/(self.N**2)
    
    def get_errorbar(self, I_data):
        return func.resampling(self.get_I_variance(I_data), I_data, self.N)
    
    def get_lattice_immune(self, frac_imm):
        return func.random_init_immune_generator(self.lattice, frac_imm)
    
    ########## INITIALISATIONS ########

    def set_initialisation_absorbing():
        return [0.2, 0.7, 0.7]
    
    def set_initialisation_wave():
        return [0.85, 0.35, 0.05]
    
    def set_initialisation_dynamiceq():
        return [0.8, 0.4, 0.5]

if __name__ == "__main__":
    print(__name__)
