"""
    Calculates the Teff from l
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

def calculating_sigma_e(X):
    """ cm2 g-1 electron scattering (Thomson) opacity"""
    sigma_e = 0.2*(1.0+X)
    return sigma_e


def calculating_Tedd(g, sigma_e):
    SIGMA_SB = 5.67051*10.0**(-5.0)       #     erg cm-2 K-4 s-1
    COST_C = 2.99792458*10.0**10.0          #     cm s-1
    Tedd = ((g*COST_C)/(sigma_e*SIGMA_SB))**(0.25)
    return Tedd

def converting_kelvin_to_keV(Teff):
    return Teff*8.621738*10**(-8)




def calculating_Teff():
	X = [1.0,  0.7374360, 0]
	g = [10.0**14.0, 10.0**14.3, 10.0**14.6]
	l = 0.1
   
   	X_here = X[0]
   	g_here = g[0]
   	
	sigma_e_here = calculating_sigma_e(X_here)
        Tedd = calculating_Tedd(g_here, sigma_e_here)
        
        
        Teff = l**(0.25)*Tedd
        Teff_keV = converting_kelvin_to_keV(Teff)
 
	print("Teff (keV) for the l is ", Teff_keV )

    
    
    
def main():
    calculating_Teff()
    
                   
if __name__ == '__main__':
    main()
