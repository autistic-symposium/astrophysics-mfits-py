"""
    Process the fits from input to output files.
    Marina Wahl, 2014
"""

import numpy


def saving_output(array_from_files, pathoutput):
    """
        Write the results from the fits in text files.
    """
    

    for f in array_from_files:

        fc1 = f[3][0][1] 
        w01 = f[3][0][0] 
        fc2 = f[3][1][1] 
        w02 = f[3][1][0] 
        fc3 = f[3][2][1] 
        w03 = f[3][2][0] 
        fc4 = f[3][3][1] 
        w04 = f[3][3][0] 
        fc5 = f[3][4][1] 
        w05 = f[3][4][0] 

        composition_here = f[0]
	teff_here = f[1]
	gravity_here = f[2]
        
        outfile = 'fit_' + composition_here + '_' + str(gravity_here) + '.out'
        path2outfile = pathoutput + outfile
        
        output = open(path2outfile, 'a')
        
        """
            write files headers
        """

	output.write('%.3f   ' % teff_here)           
        output.write('%.3f   ' % fc1)
        output.write('%.3f   ' % fc2)
        output.write('%.3f   ' % fc3)
        output.write('%.3f   ' % fc4)
        output.write('%.3f   ' % fc5)
        output.write('%.3f   ' % w01)
        output.write('%.3f   ' % w02)
        output.write('%.3f   ' % w03)
        output.write('%.3f   ' % w04)
        output.write('%.3f    \n' % w05)
        
        output.close()

        

