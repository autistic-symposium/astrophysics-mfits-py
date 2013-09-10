from blackbody import *

"""
These are the five fit techniques performed by Suleimanov et al, 2010.

obs: we use H_E = Flux/ 4pi

"""




def fit1(parameters, energy, H_E, index):
    
    """
    In the first fit, we minimize the sum
    
    sum^N_n=1 (F_En - w1*B_En(fc1*Teff))^2

    where N is the number of photon energy points in the
    considered band.

    """ 
    
    b = blackbody(parameters, energy, index) 
    return  H_E - b





def fit2(parameters, energy, H_E, index):
    """
    We fit the photon count flux, not the energy flux, so the
    second fit minimize

    sum^N_n=1 (F_En - w2*B_En(fc2*Teff))^2/E^2_n.

    """
    
    b = blackbody(parameters, energy, index) 
    return  (H_E - b)/energy





def fit3(parameters, energy, H_E, index):
    """
    In the third fit we minimize

    sum^N_n=1 (F_En - w3*B_En(fc3*Teff))^2*En.

    """
    
    b = blackbody(parameters, energy, index) 
    return  (H_E - b)*energy


"""
The fourth fit is the same as the first with other different
inputs, i.e. we make w4 = fc4^-4.

"""




def fit5(parameters, energy, H_E, index):
    """
    The fifth fit is obtained by dividing the peak energy of H_E to the blakckbody
    spectrum, as done in Madej et al, 2004.

    """
    
    b = blackbody(parameters, energy, index) 
    b_max = max(b)
    H_E_max = max(H_E)
    return 0.2, (b_max/2)/(H_E_max)