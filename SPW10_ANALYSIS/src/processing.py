from numpy import *
from plots import  *
from writing_output import *
from fitting import *

"""
This function process all the fitings, save and plot the results, for the input set of data.

"""


def processing_data(path, dataset, outfolder):
	data = [] 
	fc = []
	
	
	"""
	Loading data
	"""
	
	print "Loading dataset %d..." %dataset
	
	data.append(load(path, unpack=True))        # open/read the defined dataset
                                                #the columns are saved as arrays so data[0][0] is E, data[0][1] is H_E for l=0.001, etc...)
	print "Done!"
	
	

	""" 
	Fitting and saving
	"""
	
	print "Starting fittings for dataset %d..." %dataset
	
	fc = performing_fits(x0, data)                      # 2d array fc[19][4] for fc[luminosities=20][number of fittings = 5] for all 5 fittings in the defined dataset
	fc1, fc2, fc3, fc4, fc5 = saving_fcs(fc)            # 1d arrays fci[20] with all fcs for every luminosity in the defined dataset
	w1, w2, w3, w4, fcw1, fcw2, fcw3 =  saving_ws(fc)   # 1d arrays wi[20], fcwi[20] (dilution factor and wi*fci**4) for every luminosity in the defined dataset
	saving_output(l, fc, fcw1, fcw2, fcw3, dataset, outfolder)                    # writing output text file (table for the defined dataset)
	
	print "Done!"
		
		
	
	"""
	Plotting
	"""
	
	print "Starting plots for dataset %d..." %dataset
    
	#plot_fig3(data, dataset, outfolder)
	#plot_fig7(data, fc, dataset, outfolder)
	#plot_fig8(data, fc, dataset, outfolder)
	plot_fig9_a(l, fc1, fc2, fc3, fc4, fc5, dataset, outfolder)
	#plot_fig9_b(l, fc1, fc2, fc3, fc4, fc5, dataset, outfolder)
	#plot_fig10_a(l, w1, w2, w3, w4, dataset, outfolder)
	#plot_fig10_b(l, w1, w2, w3, w4, dataset, outfolder)
	
	print "Done!"