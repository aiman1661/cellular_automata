"""
Functions for simulating SIRS on a 50x50 lattice with periodic BC. 

author: s2229553
"""

import numpy as np
from numpy import random

# random number generator; don't remove!
rng = random.default_rng()

def update_step(lattice, site, p1, p2, p3):
    'Update step for SIRS'
    n = len(lattice)

    p = rng.random()
    bool_test = False
    site_i, site_j = site
    state_of_site = lattice[site_i][site_j]

    # susceptible site
    if lattice[site_i][site_j] == 0:
        prox_check = np.array([ lattice[(site_i+1)%n][site_j],
                       lattice[(site_i-1)%n][site_j],
                       lattice[site_i][(site_j+1)%n],
                       lattice[site_i][(site_j-1)%n] ]) # check neighbours for infection
        
        if np.any(prox_check == -1):
            bool_test = (p < p1)
            state_of_site = np.where(bool_test, -1, 0)

    # infected site
    if lattice[site_i][site_j] == -1:
        bool_test = (p < p2)
        state_of_site = np.where(bool_test, 1, -1)

    # recovered site
    if lattice[site_i][site_j] == 1:
        bool_test = (p < p3)
        state_of_site = np.where(bool_test, 0, 1)

    return bool_test, [site_i,site_j], state_of_site

def count_states(lattice):
    'Count number of sites for different states'
    susceptible = np.sum(lattice == 0)
    infected = np.sum(lattice == -1)
    recovered = np.sum(lattice == 1)
    return susceptible, infected, recovered

def random_init_immune_generator(lattice, frac_imm):
    'Randomly generate sites with immunisation'
    N = len(lattice)

    immune_count = int((N**2) * frac_imm)
    sites_immune = random.choice(N**2, immune_count, replace=False) # randomly choose sites with immunisation
    lattice.ravel()[sites_immune] = 2 # setting immune sites to take value 2

    return lattice

############### STATISTICS ################

def average_infection(data_I):
    'Calculate average infected sites'
    return np.mean(data_I[100:])

def average_infection_squared(data_I):
    'Calculate average infected sites squared'
    return np.mean(data_I[100:]**2)

# to do (jacknife resampling)
def resampling(I_var, data_I, N):
    'Returns the error bars for the variance plot (jacknife)'
    # remove initial 100 data
    data_I = data_I[100:]

    n_resampling = len(data_I) - 1

    var_list = []
    for i in range(n_resampling):
        I_resampled = np.delete(data_I, i)

        mean_I = np.mean(I_resampled)
        mean_squared_I = np.mean(I_resampled**2)

        var_i = (mean_squared_I - mean_I**2)/(N**2)
        var_list.append(var_i)

    var_array  = np.array(var_list)

    sigma_var = np.sqrt(np.sum((var_array - I_var)**2))
    return sigma_var

if __name__ == "__main__":
    print(__name__)