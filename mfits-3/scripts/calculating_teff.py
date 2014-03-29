"""
    Calculates the Teffs. 
     Marina Wahl, 2014
        
    -------------------------------------------------------------
    THEORY:
    
    	The effective temperature via l is expressed as:
    		Teff = l^1/4 * Tedd
    		
    	---> ls are given
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


def printing_table(results):
    print("Calculated Effective Temperature (Teff)\n")
    print("log[Surface Gravity(cm s-2)]        Relative Luminosity (L/LEdd)        sigma_e(cm2 g-1)        Teff(keV)\n")
    for i in range(len(results)):
        print(str(results[i][0]) + "    " + str(results[i][1]) + "    " + str(results[i][2]) + "    " + str(results[i][3]) )



def calculating_Teff():
    X = [1.0, 0.7374360, 0]
    l = [0.001, 0.003, 0.010, 0.030, 0.050, 0.070, 0.100, 0.150, 0.200, 0.300, 0.400, 0.500, 0.600, 0.700, 0.750, 0.800, 0.850, 0.900, 0.950, 0.980]
    g = [10.0**14.0, 10.0**14.3, 10.0**14.6]
    g_log = [14.0, 14.3, 14.6]
   
  
    for xx in range(len(X)):
        sigma_e_here = calculating_sigma_e(X[xx])
        for yy in range(len(g)):
		g_here = g[yy]
		g_here_log = g_log[yy]
		Tedd = calculating_Tedd(g_here, sigma_e_here)
		T_eff_calculated_here = []
		print("g, kappa --> ", g_here_log, sigma_e_here)
		for ll in range(len(l)):
		        l_here = l[ll]
		        Teff = l_here**(0.25)*Tedd
		        Teff_keV = converting_kelvin_to_keV(Teff)
		        print("l, Teff_keV --> ", l_here,Teff_keV)

   
    
    
def main():
    calculating_Teff()
    
                   
if __name__ == '__main__':
    main()
