"""
    Calculates the l from Teff
     Marina Wahl, 2014
        
    -------------------------------------------------------------
    THEORY:
    
    	---> The effective temperature via l is expressed as:
    		Teff = l^1/4 * Tedd
    	---> Tedd:
    			sigma_sb * Tedd^4 = gc/sigma_e
    		where
    			sigma_e --> 0.2 (1 + X) 
    			g = 10**(14,14.3,14.6)
                constants: sigma_sb, c
    
    
    -------------------------------------------------------------
"""

import math

def calculating_sigma_e(X):
    """ cm2 g-1 electron scattering (Thomson) opacity"""
    sigma_e = 0.2*(1.0+X)
    return sigma_e


def calculating_Tedd(g, sigma_e):
    SIGMA_SB = 5.67051*10.0**(-5.0)       #     erg cm-2 K-4 s-1
    COST_C = 2.99792458*10.0**10.0          #     cm s-1
    Tedd = ((g*COST_C)/(sigma_e*SIGMA_SB))**(0.25)
    return Tedd


def converting_keV_to_kelvin(Teff):
    return Teff/(8.621738*10**(-8))
    
def converting_kelvin_to_keV(Teff):
    return Teff*(8.621738*10**(-8))


def calculating_l():
	#T=0.075, 0.1, 0.125 keV; g=14.0, 14.3, 14.6 for pure H and pure He
	X = [1.0, 0]
	g = [10.0**14.0, 10.0**14.3, 10.0**14.6, 10**14.385]
	Teff =  [0.075, 0.1, 0.125, 0.272643294692, 0.008621738, 0.0343237572043
, 0.08621738] # keV
   
   	print("X    log g    Teff (keV)    l" )
   	for i in range(len(X)):
   		X_here = X[i]
   		sigma_e_here = calculating_sigma_e(X_here)
   		for j in range(len(g)):
   			g_here = g[j]
   			Tedd = calculating_Tedd(g_here, sigma_e_here)
   			
   			for k in range(len(Teff)):
   				T_here = Teff[k]
				Teff_K = converting_keV_to_kelvin(T_here) 
				l = (Teff_K/Tedd)**4 
			    	print(X_here, math.log10(g_here), T_here, l )

    
    
    
def main():
    calculating_l()
    #t = converting_kelvin_to_keV(10**(6.5))
    #print(t)
    
                   
if __name__ == '__main__':
    main()
    
    

