"""
Class containing the lattice system for Game of Life.

author: S2229553
"""

import numpy as np
import GameOfLife_functions as func

class GoL_Lattice():
    '''
    Lattice system
    '''

    def __init__(self, lattice):
        self.lattice = np.array(lattice)
        self.N = int(len(lattice))

    def update_step(self):
        return func.update_step(self.lattice)
    
    def count_live(self):
        return func.count_live(self.lattice)
    
    def return_com(self):
        return func.compute_com(self.lattice)
    
    ############# INITIALISATIONS ############
    
    def set_glider(self):
        return func.state_glider(self.N)
    
    def set_blinker(self):
        return func.state_blinker(self.N)
    
    def set_beehive(self):
        return func.state_beehive(self.N)
    
    def set_flower(self):
        return func.state_flower(self.N)
    
    def set_crab(self):
        return func.state_crab(self.N)
    
    def set_test(self):
        return func.state_test(self.N)

if __name__ == "__main__":
    print(__name__)