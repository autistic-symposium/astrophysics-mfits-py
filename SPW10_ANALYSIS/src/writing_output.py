from constants import *


def saving_output(l, fc, fcw1, fcw2, fcw3, dataset, outfolder):
    """
    This module writes in a text file the results from the fitting.

    """
    
    file = '/output_dataset%d.txt' %dataset
    out = outfolder + file
    output = open(out, 'w')
    output.write('Set = %d \n' %dataset)
    ''' fc: first index is 0-19 for ls, second is for 5 fits, third is for fc or w '''
    output.write('L/L_Edd       T_eff       fc_1         fc_2         fc_3         fc_4        fc_5        w1*fc_1^4      w2*fc_2^4      w3*fc_3^4\n')
    
    
    for i in range(20): 
        output.write('%.3f        ' % l[i] )
        output.write('%.3f        ' % Teff[i] )
        output.write('%.3f        ' % fc[i][0][1])
        output.write('%.3f        ' % fc[i][1][1])
        output.write('%.3f        ' % fc[i][2][1])
        output.write('%.3f        ' % fc[i][3][1])
        output.write('%.3f        ' % fc[i][4][1])
        output.write('%.3f        ' % fcw1[i])
        output.write('%.3f        ' % fcw2[i])
        output.write('%.3f        ' % fcw3[i])
        output.write('\n' )
    
    print "Output was written in %s" %out
    return 0