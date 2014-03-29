"""
    Calculates the blackbody function, using either one (fc) or
    two parameters (fc and w).
    Marina Wahl, 2013-2014
"""

from constants import hc_keV, h_keV, erg_to_keV
from math import exp



def blackbody(parameters, energy, teff):
   
    b = []
    w0 = parameters[0]
    fc0 = parameters[1]

    for i in range(len(energy)):
        b.append((w0/2.0) * (energy[i])**3 * (1.0/(exp(energy[i]/(fc0*teff)) - 1.0)) / hc_keV**2 / h_keV * (1.0/(erg_to_keV)))    
   
    return b



def blackbody_one_param(parameters, energy, teff):
   
    b = []
    fc0 = parameters[1]
    w0 = 1/(fc0**4)
  
    for i in range(len(energy)):
        b.append((w0/2.0) * (energy[i])**3 * (1.0/(exp(energy[i]/(fc0*teff)) - 1.0)) / hc_keV**2 / h_keV * (1.0/(erg_to_keV)))     
   
    return b

