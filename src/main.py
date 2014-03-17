
"""
    X-ray bursting neutron stars in low mass X-ray binaries (LMXB) was recognized
    as a source to constrain masses and radii of neutron stars. For this purpose, an 
    extended set of atmosphere models is necessary.

    This program reproduces the analysis made by Suleimanov et al (2010) to other
    model data sets.

    Marina Wahl 2013-2014

"""

import logging
import os
import time
import datetime
from constants import PATH2_INPUT_DATA, PATH2_OUTPUT_DATA, PATH2_LOG, VERBOSE
from parser import parsing_data
from processing import processing_fits



def main():
        """
            Verbose
        """
        if VERBOSE == 1:
            t = datetime.datetime.utcnow()
            EpochSeconds = time.mktime(t.timetuple())
            NOW = datetime.datetime.fromtimestamp(EpochSeconds)
            logging.basicConfig(filename = PATH2_LOG, level=logging.INFO)
            print("******* MFITS 2.0 Started...\n")
            logging.info("******* MFITS 2.0 Started...\n")
            logging.info(NOW) 

        """
            Processing files
        """
        if not os.path.exists(PATH2_INPUT_DATA):
            os.makedirs(PATH2_INPUT_DATA)
        nfiles, afiles, max_nset = parsing_data(PATH2_INPUT_DATA)
    
    
        """
            Verbose
        """
        if VERBOSE == 1:
            logging.info("\n%s data files are located at %s..." %(str(nfiles), PATH2_INPUT_DATA))
            logging.info("%s\n" %afiles)
            print("\n%s data files are located at %s..." %(str(nfiles), PATH2_INPUT_DATA))
            print("%s\n" %afiles)
        
    
        """
            Calculate the fits
        """
        if not os.path.exists(PATH2_OUTPUT_DATA):
            os.makedirs(PATH2_OUTPUT_DATA)
        processing_fits(max_nset, nfiles, afiles, PATH2_INPUT_DATA, PATH2_OUTPUT_DATA)
        

        """
            Verbose
        """
        if VERBOSE == 1:
            logging.info("Log file generated at folder %s.\nDone!\n" %PATH2_LOG)
            print("\nDone!")
    
    
if __name__ == "__main__":
    main()

