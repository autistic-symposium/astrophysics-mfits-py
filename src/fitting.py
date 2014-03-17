"""
    Calculates the fits.
    Marina Wahl, 2013-2014
"""


import scipy.optimize 
import math
import numpy
from constants import CONST_L, X0, Teff, WIEN
from blackbody import blackbody,blackbody_one_param




def fit1(parameters, energy, H_E, index, nset):    
    """
        In the first fit, we minimize the sum
        
        sum^N_n=1 (F_En - w1*B_En(fc1*Teff))^2

        where N is the number of photon energy points in the
        considered band.
    """ 
    
    b = blackbody(parameters, energy, index, nset) 
    
    return H_E - b



def fit2(parameters, energy, H_E, index, nset):
    """
        We fit the photon count flux, not the energy flux, so the
        second fit minimize

        sum^N_n=1 (F_En - w2*B_En(fc2*Teff))^2/E^2_n.
    """
   
    E = []
    
    b = blackbody(parameters, energy, index, nset) 
    
    for i in range (len(energy)):
        if energy[i] > 3.0 and energy[i] < 20.0:
            E.append(energy[i]) 
   
    return (H_E - b)/E 



def fit3(parameters, energy, H_E, index, nset):
    """
        In the third fit we minimize

        sum^N_n=1 (F_En - w3*B_En(fc3*Teff))^2*En.
    """
   
    E = []
   
    b = blackbody(parameters, energy, index, nset) 
   
    for i in range (len(energy)):
        if energy[i] > 3.0 and energy[i] < 20.0:
            E.append(energy[i]) 
   
    return  (H_E - b)*E




def fit4(parameters, energy, H_E, index, nset):    
    """
        The fourth fit is the same as the first with other different
        inputs, i.e. we make w4 = fc4^-4.
    """
    b = blackbody_one_param(parameters, energy, index, nset) 
    return H_E - b



def fit5(nl, E, H_E, index, nset):
    """
        The fifth fit is obtained by dividing the peak energy of H_E to the blakckbody
        spectrum, as done in Madej et al, 2004.
    """
    H_E_max = max(H_E)
    index_H_E = numpy.where(H_E == H_E_max)[0]
    E_F = E[index_H_E]
    b_max = WIEN*Teff[nset-1][index]
    
    return E_F/b_max
        
        

def performing_fits(E, H_E, lum_num, set_num):
    """
        This is the calling module.
    """
        
    array_fcs = []
    for i in range(len(CONST_L)):
        if lum_num == CONST_L[i]:
            break


    """ Fit 1 """
    X01 = scipy.optimize.leastsq(fit1, X0, args=(E, H_E/(4*math.pi), i, set_num))[0]
    array_fcs_aux = [X01[0], X01[1]]
    array_fcs.append(array_fcs_aux)
    
    """ Fit 2 """
    array_fcs_aux0 = scipy.optimize.leastsq(fit2, X0, args=(E, H_E/(4*math.pi), i, set_num))[0]
    array_fcs_aux1 =  [array_fcs_aux0[0], array_fcs_aux0[1]]
    array_fcs.append(array_fcs_aux1)
    
    """ Fit 3 """
    array_fcs_aux0 = scipy.optimize.leastsq(fit3, X01, args=(E, H_E/(4*math.pi), i, set_num))[0]
    array_fcs_aux1 =  [array_fcs_aux0[0], array_fcs_aux0[1]]
    array_fcs.append(array_fcs_aux1)
    
    """ Fit 4 """
    array_fcs_aux0 = scipy.optimize.leastsq(fit4, [X01[1]], args=(E, H_E/(4*math.pi), i, set_num))[0]
    array_fcs_aux1 =  [1/(array_fcs_aux0**4), array_fcs_aux0]
    array_fcs.append(array_fcs_aux1)
    
    """ Fit 5 """
    array_fcs_aux0 = fit5(set_num, E, H_E/(4*math.pi) , i, set_num) 
    array_fcs_aux1 = [1/(array_fcs_aux0**4),array_fcs_aux0]
    array_fcs.append(array_fcs_aux1)

    
    
    return array_fcs
