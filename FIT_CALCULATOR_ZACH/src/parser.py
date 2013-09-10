"""
    This module is a set  of snippets for file handling, reading, and parsing.
    
    Marina von Steinkirch, spring/2013
"""

import os


def finding_max_nsets(afiles, nfiles, path2data):
    """
        Find max number of sets
    """
    max_nset = 0
    for n in range(nfiles):
        """
            Verbose
        """
        filename = str(afiles[n])
        nset, nl  = parsing_name_file(filename)
        if nset > max_nset:
            max_nset = nset
        
    return max_nset


def counting_number_of_files(path):
    """
        Count the number of data files in the folder.
    """
    
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    
    return count



def reading_name_files(path):
    """
        Read all the names of the data file and save them in an array.
    """
    
    afilenames =  []
    for root, dirs, files in os.walk(path):
        for name in files:       
            filename = os.path.join(name)
            afilenames.append(filename)
    
    return afilenames



def parsing_name_file(namefile):
    """
        Parse the name of the data file to extract l and set number.
    """
        
    str1 = namefile.split("t")
    str2 = str1[1].split("l")
    str3 = str2[1].split(".")
    str4 = str3[0][1:]
    str5 = '0.'+ str4
    nset = int(str2[0])
    nl = float(str5)
    
    return nset, nl   


def parsing_data(path):
    nfiles = counting_number_of_files(path)
    afiles = reading_name_files(path)
    max_nset = finding_max_nsets(afiles, nfiles, path)    
    
    return nfiles, afiles, max_nset