"""
     Convert K <--> eV for Temperatures
     Marina Wahl, 2014
        
    -------------------------------------------------------------
    THEORY:
    
    	--->  1 degree kelvin= 8.621738 X10-5  eV 
    
    
    -------------------------------------------------------------
"""

import math


def converting_keV_to_kelvin(Teff):
    return Teff/(8.621738*10**(-8))
    
def converting_kelvin_to_keV(Teff):
    return Teff*(8.621738*10**(-8))

    
def main():
    Teff_Kelvin = 10**5.6
    Teff_kelvin_to_keV = converting_kelvin_to_keV(Teff_Kelvin)
    print(Teff_kelvin_to_keV)
    
    #Teff_keV = 8.621738*10**(-8)
    #Teff_keV_to_kelvin = converting_keV_to_kelvin(Teff_keV)    
    
    #print('T in kev, T converted to Kelvin: ', Teff_keV, Teff_keV_to_kelvin  )
    #print('T in Kelvin, T converted to kev: ', Teff_Kelvin, Teff_kelvin_to_keV )   
                   
if __name__ == '__main__':
    main()
    
    

