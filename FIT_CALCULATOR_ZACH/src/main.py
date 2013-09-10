
"""
    X-ray bursting neutron stars in low mass X-ray binaries (LMXB) was recognized
    as a source to constrain masses and radii of neutron stars. For this purpose, an 
    extended set of atmosphere models is necessary.

    This program reproduces the analysis made by Suleimanov et al (2010) to other
    model data sets.

    Marina von Steinkirch, spring/2013

"""

import logging
from constants import PATH2_INPUT_DATA, PATH2_OUTPUT_DATA, PATH2_LOG, NOW 
from parser import parsing_data
from processing import processing_fits
import os
import numpy


def main():
    
    # create folder for logs
    try: 
        os.makedirs("../logs/")
    except OSError:
        if not os.path.isdir("../logs/"):
            raise
    numpy.seterr(divide='ignore')

    
    
    """
        Log definitions.
    """
    logging.basicConfig(filename = PATH2_LOG, level=logging.INFO)
    logging.info("Program started.\n")
    logging.info(NOW)
    
    
    
    """
       Opening and counting data files.
    """
    nfiles, afiles, max_nset = parsing_data(PATH2_INPUT_DATA)

    """ 
        Verbose.
    """
    logging.info("\n%s data files are located at %s..." %(str(nfiles), PATH2_INPUT_DATA))
    logging.info("%s\n" %afiles)
    
    
    
    """
        Calculate the fits.
    """
    processing_fits(max_nset, nfiles, afiles, PATH2_INPUT_DATA, PATH2_OUTPUT_DATA)
    
    

    """ 
        Verbose .
    """
    logging.info("Log file generated at folder %s.\nDone!\n" %PATH2_LOG)
    print("\nDone!")
    
    
if __name__ == "__main__":
    main()