"""
    Snippets for file handling, reading, and parsing.
    Marina Wahl, 2013-2014
"""

import os


def finding_max_nsets(array_of_files, num_of_files):
    """
        Find max number of sets
    """
    
    max_num_set= 0
    
    for n in range(num_of_files):
        
        filename = str(array_of_files[n])
        nset, nl = parsing_name_file(filename)
       
        if nset > max_num_set:
            max_num_set = nset
        
    return max_num_set



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
    
    array_filenames =  []
    
    for root, dirs, files in os.walk(path):
        
        for name in files:       
            filename = os.path.join(name)
            array_filenames.append(filename)
    
    return array_filenames



def parsing_name_file(filename):
    """
        Parse the name of the data file to extract l and set number.
    """
        
    str1 = filename.split("t")
    str2 = str1[1].split("l")
    str3 = str2[1].split(".")
    str4 = str3[0][1:]
    str5 = '0.'+ str4
    nset = int(str2[0])
    nl = float(str5)
    
    return nset, nl   




def parsing_data(path):
    """
        This is the calling module.
    """
    
    num_of_files    =   counting_number_of_files(path)
    array_of_files  =   reading_name_files(path)
    max_num_set     =   finding_max_nsets(array_of_files, num_of_files)    
    
    return num_of_files, array_of_files, max_num_set 
