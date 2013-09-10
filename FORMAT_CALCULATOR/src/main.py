
"""

This program format the output file from the simulations to a suitable 
way to calculate the fits.

Marina von Steinkirch, spring/2013

"""


import os
from constants import PATH2_LOG, PATH2_REDUCED_SPW_DATA, NOW
from formatting_spw import reduce_spw_data



def main():
    
    
    """
        Format data files from spw10 to files to each table.
    """
    if len(os.listdir(PATH2_REDUCED_SPW_DATA[0])) < 1:
        reduce_spw_data()
    
    
    

    
    
if __name__ == "__main__":
    main()