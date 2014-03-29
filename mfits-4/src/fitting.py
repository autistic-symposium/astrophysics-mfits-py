"""
    Calculates the fits.
    Marina Wahl, 2013-2014
"""


import scipy.optimize 
import math
import numpy as np
from constants import X0, WIEN
from blackbody import blackbody,blackbody_one_param




def fit1(parameters, E, H_E, teff):    
    """
        In the first fit, we minimize the sum
        
        sum^N_n=1 (F_En - w1*B_En(fc1*Teff))^2

        where N is the number of photon energy points in the
        considered band.
    """ 
    
    b = blackbody(parameters, E, teff) 
    
    return H_E - b



def fit2(parameters, E, H_E, teff):
    """
        We fit the photon count flux, not the energy flux, so the
        second fit minimize

        sum^N_n=1 (F_En - w2*B_En(fc2*Teff))^2/E^2_n.
    """
   
    b = blackbody(parameters, E, teff) 

    return (H_E - b)/E 



def fit3(parameters, E, H_E, teff):
    """
        In the third fit we minimize

        sum^N_n=1 (F_En - w3*B_En(fc3*Teff))^2*En.
    """
   
    b = blackbody(parameters, E, teff) 
   

    return  (H_E - b)*E




def fit4(parameter, E, H_E, teff):    
    """
        The fourth fit is the same as the first with other different
        inputs, i.e. we make w4 = fc4^-4.
    """

    b = blackbody_one_param(parameter, E,  teff) 

    return H_E - b



def fit5(E, H_E, teff):
    """
        The fifth fit is obtained by dividing the peak energy of H_E to the blakckbody
        spectrum, as done in Madej et al, 2004.
    """
    H_E_max = max(H_E)
    index_H_E = np.where(H_E == H_E_max)[0]
    E_F = E[index_H_E]
    b_max = WIEN*teff
    return (E_F/b_max)[0]
        
      

  
def clean_data(E_dirty, H_E_dirty):
    E = []
    H_E = []

    for i in range (len(E_dirty)):
        if  H_E_dirty[i] != 0:# and E_dirty[i]>0.1 and E_dirty[i]<5:
            H_E.append(H_E_dirty[i]/4.0*math.pi) 	
	    E.append(E_dirty[i]) 

    return np.array(E), np.array(H_E)



def performing_fits(E_dirty, H_E_dirty, teff):
    """
        This is the calling module.
    """
   
    array_fcs = []
    E, H_E = clean_data(E_dirty, H_E_dirty)



    """ Fit 1 """
    array_fcs_aux0 = scipy.optimize.leastsq(fit1, X0, args=(E, H_E,  teff))[0]
    array_fcs_aux = [array_fcs_aux0[0], array_fcs_aux0[1]]
    array_fcs.append(array_fcs_aux)

    
    """ Fit 2 """
    array_fcs_aux0 = scipy.optimize.leastsq(fit2, X0, args=(E, H_E, teff))[0]
    array_fcs_aux1 =  [array_fcs_aux0[0], array_fcs_aux0[1]]
    array_fcs.append(array_fcs_aux1)
    

    """ Fit 3 """
    array_fcs_aux0 = scipy.optimize.leastsq(fit3, X0, args=(E, H_E, teff))[0]
    array_fcs_aux1 =  [array_fcs_aux0[0], array_fcs_aux0[1]]
    array_fcs.append(array_fcs_aux1)


    """ Fit 4 """
    X01 = scipy.optimize.leastsq(fit1, X0, args=(E, H_E,  teff))[0]
    array_fcs_aux1 =  [1/(X01[1]**4), X01[1]]
    array_fcs.append(array_fcs_aux1)
    

    """ Fit 5 """
    array_fcs_aux0 = fit5(E, H_E/(4*math.pi), teff) 
    array_fcs_aux1 = [1/(array_fcs_aux0**4), array_fcs_aux0]
    array_fcs.append(array_fcs_aux1)


    return array_fcs
