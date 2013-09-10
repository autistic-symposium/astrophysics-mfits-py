from constants import *

def blackbody(parameters, energy, index):
    """
    The Planck function for a blackbody spectrum.

    """
    
    w0 = parameters[0]
    fc0 = parameters[1]
    T = Teff[index]
    b = (w0/2) * (energy)**3 * (1/(exp(energy/(fc0*T)) -1)) / hc_keV**2 / h_keV * (1/(erg_to_keV))
    return b

