"""
    This module calculate the five fits shown by Suleimanov et al, 2010.

    Marina von Steinkirch, spring/2013/
"""
from matplotlib.mlab import *
from scipy.optimize import *
from numpy import *
from constants import l, X0, Teff, WIEN, erg_to_keV, cm_to_m
from blackbody import blackbody,blackbody_one_param




"""
    These are the five fit techniques performed by Suleimanov et al, 2010.
"""



def fit1(parameters, energy, H_E, index):    
    """
        In the first fit, we minimize the sum
        
        sum^N_n=1 (F_En - w1*B_En(fc1*Teff))^2

        where N is the number of photon energy points in the
        considered band.
    """ 
    b = blackbody(parameters, energy, index) 
    return H_E - b



def fit2(parameters, energy, H_E, index):
    """
        We fit the photon count flux, not the energy flux, so the
        second fit minimize

        sum^N_n=1 (F_En - w2*B_En(fc2*Teff))^2/E^2_n.
    """
    b = blackbody(parameters, energy, index) 
    return (H_E - b)/energy #final



def fit3(parameters, energy, H_E, index):
    """
        In the third fit we minimize

        sum^N_n=1 (F_En - w3*B_En(fc3*Teff))^2*En.
    """
    b = blackbody(parameters, energy, index) 
    return  (H_E - b)*energy




def fit4(parameters, energy, H_E, index):    
    """
        The fourth fit is the same as the first with other different
        inputs, i.e. we make w4 = fc4^-4.
    """
    b = blackbody_one_param(parameters, energy, index) 
    return H_E - b



def fit5(nl, E, H_E, index):
    """
        The fifth fit is obtained by dividing the peak energy of H_E to the blakckbody
        spectrum, as done in Madej et al, 2004.
    """
    H_E_max = max(H_E)
    index_H_E = where(H_E == H_E_max)[0]
    E_F = E[index_H_E]
    b_max = WIEN*Teff[index]
    
    return E_F/b_max
        
        

def performing_fits(E, H_E, nl):
    """
        This module perform all the five fits and extract fcs and ws.        
    """
    afcs = []
    for i in range(len(l)):
        if nl == l[i]:
            break


    """ Fit 1 """
    X01 = leastsq(fit1, X0, args=(E, H_E/(4*pi), i))[0]
    afcs_aux = [X01[0], X01[1]]
    afcs.append(afcs_aux)
    
    """ Fit 2 """
    afcs_aux0 = leastsq(fit2, X0, args=(E, H_E/(4*pi), i))[0]
    afcs_aux1 =  [afcs_aux0[0], afcs_aux0[1]]
    afcs.append(afcs_aux1)
    
    """ Fit 3 """
    afcs_aux0 = leastsq(fit3, X01, args=(E, H_E/(4*pi), i))[0]
    afcs_aux1 =  [afcs_aux0[0], afcs_aux0[1]]
    afcs.append(afcs_aux1)
    
    """ Fit 4 """
    afcs_aux0 = leastsq(fit4, [X01[1]], args=(E, H_E/(4*pi), i))[0]
    afcs_aux1 =  [1/(afcs_aux0**4), afcs_aux0]
    afcs.append(afcs_aux1)
    
    """ Fit 5 """
    afcs_aux0 = fit5(nl, E, H_E/(4*pi) , i) 
    afcs_aux1 = [1/(afcs_aux0**4),afcs_aux0]
    afcs.append(afcs_aux1)

    
    
    return afcs