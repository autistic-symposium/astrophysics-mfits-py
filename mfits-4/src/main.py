#!/usr/bin/python3
"""
    Snippets for cleasing data from zcode
    Marina Wahl, 2014
"""

import os
import numpy
from fitting import performing_fits
from processing import saving_output


def read_files_name(pathinput):
    """
        Read all the names of the data file and save them in an array.
    """
    
    array_filenames =  []
    
    for root, dirs, files in os.walk(pathinput):
        
        for name in files:       
            filename = os.path.join(name)
            array_filenames.append(filename)
    
    return array_filenames



def parsing_name_file(filename):
    """
        Parse the name of the data file to extract l and set number.
    """
        
    composition = filename.split("_")[0] 
    teff = int(filename.split("_")[1])/1000.0
    gravity = int(filename.split("_")[2].split(".")[0])/1000.0
    
    return composition, teff, gravity




def opening_files(files_array, pathinput):
    """ 
        Process the fits for same sets
    """       
    array_from_files = []  
    
    for f in files_array:
        
        filename = str(f)     
        composition, teff, gravity = parsing_name_file(f)

	path = pathinput + filename  
        E, H_E = numpy.loadtxt(path, unpack=True)
        
        array_from_files_aux = [composition, teff, gravity, performing_fits(E, H_E, teff)]
        array_from_files.append(array_from_files_aux)              
            
    return  sorted(array_from_files)



def main():
    pathinput = "../data/"
    pathoutput = "../output/"
    files_array = read_files_name(pathinput)
    array_from_files= opening_files(files_array, pathinput)

    saving_output(array_from_files, pathoutput)



         
if __name__ == '__main__':
    main()
