""" 
    This module gathers all the global constants in the code
    and the arrays as well.

    Marina von Steinkirch, spring/2013
"""

from pylab import math
import time
import datetime



"""
    Initial inputs
"""
X0 = [0.2,1.1]              # initial guess for [w,fc]
RANGE = [3.0, 20.0]         # keV - range of data
MESSAGE = 'Data Range: ' + str(RANGE[0]) + ' - ' + str(RANGE[1]) + ' keV.'
PATH2_INPUT_DATA = "../data/lanl_2012/"
PATH2_OUTPUT_DATA = "../output/lanl_2012/"
PATH2_LOG = "../logs/log.txt"
WIEN = 2.8977685


t = datetime.datetime.utcnow()
EpochSeconds = time.mktime(t.timetuple())
NOW = datetime.datetime.fromtimestamp(EpochSeconds)



"""
    Converting  units
"""
hc_keV = 2 * math.pi * 1.97326938*1e-8 
h_keV = 4.135667516 * 1e-18
erg_to_keV = 6.24150974 * 1e8
cm_to_m = 1e2




"""
    Normalized luminosity (l = L/L_Edd), based on Suleimanov et al 2010
"""
l = [0.001,0.003, 0.010, 0.030, 0.050, 0.070, 0.100, 0.150, 0.200, 0.300, 0.400, 0.500, 0.600, 0.700, 0.750, 0.800, 0.850, 0.900, 0.950, 0.980]
l_str = ['0001','0003', '001', '003', '05', '007', '01', '015', '02', '03', '04', '05', '06', '07', '075', '08', '085', '09', '095', '098']



"""
    Effective temperatures for those luminosities for g = 14 (sets 1,4,7,10,13,16),  based on Suleimanov et al 2010
"""
Teff = [0.303, 0.398, 0.538, 0.709, 0.805, 0.876, 0.957, 1.060, 1.139, 1.260, 1.354, 1.432, 1.498, 1.557, 1.584, 1.610, 1.635, 1.658, 1.681, 1.694 ]