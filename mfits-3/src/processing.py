"""
    Process the fits from input to output files.
    If the data file has different format of set%d_fits.dat, you can modify it here.
    You can define in here how the output fit files will look like.
    Marina Wahl, 2013-2014
"""

import numpy
from parser import parsing_name_file
from fitting import performing_fits
from constants import VERBOSE
import logging




def opening_files(num_of_files, array_of_files, path2input):
    """ 
        Process the fits for same sets
    """       
    array_fcs_sets = []  
    
    for n in range(num_of_files):
        
        filename = str(array_of_files[n])
        path = path2input + filename
        
        set_num, lum_num = parsing_name_file(filename)

        """
            Verbose
        """
        if VERBOSE == 1:
            logging.info(path)
            print(path)


        E, H_E = numpy.loadtxt(path, unpack=True)
        
        array_fcs_sets_aux = [set_num, lum_num, performing_fits(E, H_E, lum_num, set_num)]
        array_fcs_sets.append(array_fcs_sets_aux)              
            
    return  sorted(array_fcs_sets)



def saving_output(array_fcs_sets, max_num_set, num_of_files, path2output):
    """
        Write the results from the fits in text files.
    """
    
    sets_used = []
    first = True
    
    """ 
        Looping over all the data files.
    """
    for f in range(num_of_files):
       
        array_for_this_loop = array_fcs_sets[f]
        set_this_loop = array_for_this_loop[0]
        
        outfile = 'set%d_fits.dat' %set_this_loop
        path2outfile = path2output + outfile
        output = open(path2outfile, 'a')
        
        sets_used.append(set_this_loop)
        
        
        """
            write files headers
        """
        for i in range(len(sets_used)-1):
            if sets_used[i] == set_this_loop:
                first = False
        
        if first == True:            
            output.write('\nL/L_Edd      fc1      fc2    fc3    fc4    fc5    w01    w02    w03  \n')
           
            
        """
            write results
        """
        output.write('%.10f      ' % array_for_this_loop[1])           # ENERGY
        output.write('%.10f      ' % array_for_this_loop[2][0][1])    # FIT 1 - fc
        output.write('%.10f      ' % array_for_this_loop[2][1][1])    # FIT 2 - fc
        output.write('%.10f      ' % array_for_this_loop[2][2][1])    # FIT 3 - fc
        output.write('%.10f      ' % array_for_this_loop[2][3][1])    # FIT 4 - fc
        output.write('%.10f      ' % array_for_this_loop[2][4][1])    # FIT 5 - fc
        output.write('%.10f      ' % array_for_this_loop[2][0][0])    # FIT 1 - w0
        output.write('%.10f      ' % array_for_this_loop[2][1][0])    # FIT 2 - w0
        output.write('%.10f      \n' % array_for_this_loop[2][2][0])    # FIT 3 - w0   
        
        output.close()
        first = True 
        
        
        """
            Verbose
        """
        if VERBOSE == 1:
            logging.info("Output was written at %s." %outfile)
            print("Output was written at %s." %outfile)
   
   
   

def processing_fits(max_num_set, num_of_files, array_of_files, path2input, path2output):
    """
        This is the calling module.
    """
    if VERBOSE == 1:
        logging.info("Opening data files and processing the fits...\n")
        print("Opening data files and processing the fits...\n")
        
    array_fcs_sets = opening_files(num_of_files, array_of_files, path2input)
    
    
    if VERBOSE == 1:
        logging.info("Saving the output files...\n")
        print("Saving the output files...\n")
    saving_output(array_fcs_sets, max_num_set, num_of_files, path2output)
