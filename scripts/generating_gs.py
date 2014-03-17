"""
     Calculating different g's
     Marina Wahl, 2014
        
    -------------------------------------------------------------
    THEORY:
    
    	In zavlin, g14 = f/10**14
    	How to find this in terms of log g for the code?
    	This code compute the ranges...
    
    
    -------------------------------------------------------------
"""

import math


def print_g_ranges():
    rangeg = [x / 1000.0 for x in range(14000, 14600, 1)] 
    for i, g in enumerate(rangeg):
    	print('index, log g = ', g, 10**rangeg[i]/10**14 )
    

    
def main():
    print_g_ranges() 
                   
if __name__ == '__main__':
    main()
    
    

