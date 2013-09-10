""" 
    This module gathers all the global constants in the code
    and the arrays as well.

    Marina von Steinkirch, spring/2013
    
"""

from pylab import math
import time
import datetime



"""
    Output Names and Constants
"""
PATH2_RAW_SPW_DATA = "../data/spw/spectra_burst.dat"
PATH2_REDUCED_SPW_DATA = ["../output/spw/all_sets_all_energies/", "../output/spw/entire_range/", "../output/spw/cut_range/"] 
PATH2_LOG = "../logs/log.txt"

RANGE = [3.0, 20.0]         # keV - range of data

t = datetime.datetime.utcnow()
EpochSeconds = time.mktime(t.timetuple())
NOW = datetime.datetime.fromtimestamp(EpochSeconds)

