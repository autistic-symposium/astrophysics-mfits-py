"""
    Calculates the blackbody function, using either one (fc) or
    two parameters (fc and w).
    Marina Wahl, 2013-2014
"""

from constants import hc_keV, h_keV, erg_to_keV, Teff
from math import exp



def blackbody(parameters, energy, index, nset):
   
    b = []
    w0 = parameters[0]
    fc0 = parameters[1]
    T = Teff[nset-1][index]
   
    for i in range(len(energy)):
        b.append((w0/2.0) * (energy[i])**3 * (1.0/(exp(energy[i]/(fc0*T)) - 1.0)) / hc_keV**2 / h_keV * (1.0/(erg_to_keV)))    
   
    return b



def blackbody_one_param(parameter, energy, index, nset):
   
    b = []
    fc0 = parameter[0]
    T = Teff[nset-1][index]
    
    for i in range(len(energy)):
        b.append(((1/(fc0**4))/2.0) * (energy[i])**3 * (1.0/(exp(energy[i]/(fc0*T)) - 1.0)) / hc_keV**2 / h_keV * (1.0/(erg_to_keV)))    
   
    return b

