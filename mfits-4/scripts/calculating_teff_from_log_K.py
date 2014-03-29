"""
     Convert K <--> eV for Temperatures
     Marina Wahl, 2014
        
    -------------------------------------------------------------
    THEORY:
    
    	--->  1 degree kelvin= 8.621738 X10-5  eV 
    
    
    -------------------------------------------------------------
"""

import math


def converting_kelvin_to_keV(Teff):
    return Teff*(8.621738*10**(-8))

    
def main():
    Teff_Kelvin = [10**4.7, 10**5.0, 10**5.3, 10**5.6, 10**5.9, 10**6.2, 10**6.5]
    for i in Teff_Kelvin:
	Teff_kelvin_to_keV = converting_kelvin_to_keV(i)
    	print("Teff in Kelvin, Teff in keV: ", math.log10(i), Teff_kelvin_to_keV)
    
                   
if __name__ == '__main__':
    main()
    
    

