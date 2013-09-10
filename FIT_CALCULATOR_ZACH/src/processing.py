import numpy
from parser import parsing_name_file
from fitting import performing_fits
from constants import MESSAGE
import time
import datetime
import logging



def opening_files(max_nset, nfiles, afiles, path2input):
    """ 
        Process the fits for same sets
    """       
    
    afcs_sets = []  
    for n in range(nfiles):
        filename = str(afiles[n])
        path = path2input + filename
        nset, nl = parsing_name_file(filename)
        E, H_E = numpy.loadtxt(path, unpack=True)
        afcs_set_aux = [nset, nl, performing_fits(E, H_E, nl)]
        afcs_sets.append(afcs_set_aux)              
            
    return  sorted(afcs_sets)



def saving_output(afcs_sets, max_nset, nfiles, path2output):
    """
        Writes in a text file the results from the fit.
    """
    sets_used = []
    first = True
    """ 
        Looping in all data files.
    """
    for n in range(nfiles):
        array_for_this_loop = afcs_sets[n]
        set_this_loop = array_for_this_loop[0]
        outfile = 'set%d_fits.dat' %set_this_loop
        path2outfile = path2output + outfile
        output = open(path2outfile, 'a')
        sets_used.append(set_this_loop)
        
        for i in range(len(sets_used)-1):
            if sets_used[i] == set_this_loop:
                first = False
        
        if first == True:
            t = datetime.datetime.utcnow()
            EpochSeconds = time.mktime(t.timetuple())
            now = datetime.datetime.fromtimestamp(EpochSeconds)
            output.write('\nSet = %d            -         Generated on '  %set_this_loop)   
            output.write(now.ctime())    
            output.write('\n\n%s:' %MESSAGE)
            output.write('\n------------------------------------------------------------------------------------------------------------------')
            output.write('\nL/L_Edd      fc_1         fc_2         fc_3         fc_4        fc_5        w1*fc_1^4     w2*fc_2^4     w3*fc_3^4') 
            output.write('\n------------------------------------------------------------------------------------------------------------------\n')
       
        output.write('%.3f        ' % array_for_this_loop[1])
        output.write('%.3f        ' % array_for_this_loop[2][0][1])
        output.write('%.3f        ' % array_for_this_loop[2][1][1])
        output.write('%.3f        ' % array_for_this_loop[2][2][1])
        output.write('%.3f        ' % array_for_this_loop[2][3][1])
        output.write('%.3f        ' % array_for_this_loop[2][4][1])
        output.write('%.3f        ' % (array_for_this_loop[2][0][0]*array_for_this_loop[2][0][1]**4))
        output.write('%.3f        ' % (array_for_this_loop[2][1][0]*array_for_this_loop[2][1][1]**4 ))
        output.write('%.3f        \n' % (array_for_this_loop[2][2][0]*array_for_this_loop[2][2][1]**4 ))
        
        output.close()
        first = True 
           

    logging.info("Output was written at %s." %outfile)
   
   
    return 0


def processing_fits(max_nset, nfiles, afiles, path2input, path2output):
    afcs_sets = opening_files(max_nset, nfiles, afiles, path2input)
    saving_output(afcs_sets, max_nset, nfiles, path2output)
    
