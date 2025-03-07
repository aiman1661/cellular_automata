"""
Functions for simulating the Game of Life on a 50x50 lattice with periodic BC. 
I've also added interesting equilibrium ICs.

author: s2229553
"""

import numpy as np
from numpy import random

# random number generator; don't remove!
rng = random.default_rng()

def update_step(lattice):
    'Update step for game of life'

    # calculating number of live nn
    nn_contribution = (np.roll(lattice, shift=1, axis=0) + 
        np.roll(lattice, shift=1, axis=1) +
        np.roll(lattice, shift=-1, axis=0) +
        np.roll(lattice, shift=-1, axis=1) +
        np.roll(lattice, shift=(1,1), axis=(0,1)) +
        np.roll(lattice, shift=(1,-1), axis=(0,1)) +
        np.roll(lattice, shift=(-1,1), axis=(0,1)) +
        np.roll(lattice, shift=(-1,-1), axis=(0,1)))

    bool_mask_live = ((lattice == 1) & ((nn_contribution == 2) | (nn_contribution == 3))) # condition for live to stay live
    bool_mask_dead = ((lattice == 0) & (nn_contribution == 3)) # condition for dead to be live

    return (bool_mask_live | bool_mask_dead).astype(int) # OR to overlap the live states,
                                                         # FALSE in both live and dead masks are dead

def count_live(lattice):
    'Count number of live sites'
    return np.sum(lattice)

def compute_com(lattice):
    'Calculate the centre of mass of a GLIDER; dont forget to discard boundary calculations'
    N = len(lattice)

    # first check if it crosses bondary; if it does then return None
    boundary_check = (np.sum(lattice[0, :]) > 0 or 
                      np.sum(lattice[N-1, :]) > 0 or
                      np.sum(lattice[:, 0]) > 0 or
                      np.sum(lattice[:, N-1]) > 0)
    
    if boundary_check:
        return None
    
    live_sites = np.where(lattice == 1) # find tuples for all live sites

    if len(live_sites) == 0:
        return None

    # calculate center of mass 
    y_positions = live_sites[0]  
    x_positions = live_sites[1]  
    
    com_y = np.mean(y_positions)
    com_x = np.mean(x_positions)
    
    return np.array([com_x, com_y])

############## EQUILIBRIUM STATES #################

def state_glider(N):
    glider_square = np.array([[0,1,0],[0,0,1],[1,1,1]])
    lattice_square = np.zeros((N,N))

    # find the center indices of the large array
    center_x, center_y = N // 2, N // 2  

    # compute the slice indices
    x_start, x_end = center_x - 1, center_x + 2 
    y_start, y_end = center_y - 1, center_y + 2

    # embed the glider square in the lattice square
    lattice_square[x_start:x_end, y_start:y_end] = glider_square
    return lattice_square

def state_blinker(N):
    blinker_square = np.array([[0,0,0],[1,1,1],[0,0,0]])
    lattice_square = np.zeros((N,N))

    # find the center indices of the large array
    center_x, center_y = N // 2, N // 2  

    # compute the slice indices
    x_start, x_end = center_x - 1, center_x + 2 
    y_start, y_end = center_y - 1, center_y + 2

    # embed the glider square in the lattice square
    lattice_square[x_start:x_end, y_start:y_end] = blinker_square
    return lattice_square

def state_beehive(N):
    beehive_quad = np.array([[0,1,1,0],[1,0,0,1],[0,1,1,0]])
    lattice_square = np.zeros((N,N))

    # find the center indices of the large array
    center_x, center_y = N // 2, N // 2  

    # compute the slice indices
    x_start, x_end = center_x - 1, center_x + 2 
    y_start, y_end = center_y - 2, center_y + 2

    # embed the glider square in the lattice square
    lattice_square[x_start:x_end, y_start:y_end] = beehive_quad
    return lattice_square

def state_flower(N):
    flower_square = np.array([[0,1,0],[1,0,1],[0,1,0]])
    lattice_square = np.zeros((N,N))

    # find the center indices of the large array
    center_x, center_y = N // 2, N // 2  

    # compute the slice indices
    x_start, x_end = center_x - 1, center_x + 2 
    y_start, y_end = center_y - 1, center_y + 2

    # embed the glider square in the lattice square
    lattice_square[x_start:x_end, y_start:y_end] = flower_square
    return lattice_square

def state_crab(N):
    crab_square = np.array([[0,1,0,0],[1,0,1,0],[1,0,0,1],[0,1,1,0]])
    lattice_square = np.zeros((N,N))

    # find the center indices of the large array
    center_x, center_y = N // 2, N // 2  

    # compute the slice indices
    x_start, x_end = center_x - 2, center_x + 2 
    y_start, y_end = center_y - 2, center_y + 2

    # embed the glider square in the lattice square
    lattice_square[x_start:x_end, y_start:y_end] = crab_square
    return lattice_square

def state_test(N):
    test_square = np.array([[0,1,1,1,1,1,1,1,1,0],[1,0,0,0,0,0,0,0,0,1],[0,1,1,1,1,1,1,1,1,0]])
    lattice_square = np.zeros((N,N))

    # find the center indices of the large array
    center_x, center_y = N // 2, N // 2  

    # compute the slice indices
    x_start, x_end = center_x - 1, center_x + 2 
    y_start, y_end = center_y - 5, center_y + 5

    # embed the glider square in the lattice square
    lattice_square[x_start:x_end, y_start:y_end] = test_square
    return lattice_square

def update_step_test(lattice):
    'Update step for game of life (test)'
    N = len(lattice)

    nn_contribution = (np.roll(lattice, shift=1, axis=0) + 
        np.roll(lattice, shift=1, axis=1) +
        np.roll(lattice, shift=-1, axis=0) +
        np.roll(lattice, shift=-1, axis=1) +
        np.roll(lattice, shift=(1,1), axis=(0,1)) +
        np.roll(lattice, shift=(1,-1), axis=(0,1)) +
        np.roll(lattice, shift=(-1,1), axis=(0,1)) +
        np.roll(lattice, shift=(-1,-1), axis=(0,1)))

    bool_mask_live = ((lattice == 1) & ((nn_contribution == 2) | (nn_contribution == 3)))
    bool_mask_dead = ((lattice == 0) & (nn_contribution == 3)) 
    bool_mask = bool_mask_live | bool_mask_dead
    lattice_new = (bool_mask_live | bool_mask_dead).astype(int)

    return nn_contribution, lattice_new, bool_mask, bool_mask_live, bool_mask_dead

if __name__ == '__main__':
    lattice = random.randint(low=0,high=2,size=(5,5))
    print(f'initial : {lattice}')
    lattice_nn, lattice_update, bool_mask, bool_live, bool_dead  = update_step_test(lattice)
    print(f'number of nn alive : {lattice_nn}')
    print(f'bool_mask : {bool_mask}')
    print(f'bool_live : {bool_live}')
    print(f'bool_dead : {bool_dead}')
    print(f'updated lattice : {lattice_update}')
    