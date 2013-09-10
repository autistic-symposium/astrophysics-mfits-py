""" 
    This module formats the SPW10 data (obtained from the author's
    website) in a suitable way.
    
    Marina von Steinkirch, spring/2013
    
"""

from constants import PATH2_RAW_SPW_DATA, PATH2_REDUCED_SPW_DATA, RANGE
from pylab import close


def delete_line(path2file):
    """
        Delete the label lines.
    """   
    infile = open(path2file, 'r')
    output = []
    for line in infile:
        if not " Set" in line:
            if not "   T_eff(keV)=  " in line:
                if not "   L/L_Edd =  " in line:
                    output.append(line)
    infile = close() 
    infile = open(path2file, 'w')
    infile.writelines(output)
    infile.close()
    
    return 0



def saving_final_ls(pathout, rangevalue, E, H_E_l, nset, l):
    """
        Save the files for each l.
    """     
    outfile = 'set%dl%s.dat' %(nset, l)
    path2outfile = pathout + outfile
    output = open(path2outfile, 'a')
    
    for i in range(len(E)):
        if (rangevalue == 1):
            if (E[i]<RANGE[1]) and (E[i]>RANGE[0]):
                output.write('%E       ' %E[i])
                output.write('%E\n' %H_E_l[i])
        if (rangevalue == 0):
                output.write('%E       ' %E[i])
                output.write('%E\n' %H_E_l[i])
        
    output.close()
      
    return 0





def divide_spw_sets_into_l(pathin, pathout, RANGEVALUE):
    """
        Loop to divide each set into 20 files for each column l.
    """
    
    for files in range(18):
        set_this_loop = files + 1
        
        inputfile = 'set%d.dat' %(set_this_loop)       
        path2input = pathin  + inputfile
        
        delete_line(path2input)
        infile = open(path2input, 'r')
        
        E = []
        H_E_001 = []
        H_E_003 = []
        H_E_01 = []
        H_E_03 = []
        H_E_05 = []
        H_E_07 = []
        H_E_10 = []
        H_E_15 = []
        H_E_20 = []
        H_E_30 = []
        H_E_40 = []
        H_E_50 = []
        H_E_60 = []
        H_E_70 = []
        H_E_75 = []
        H_E_80 = []
        H_E_85 = []
        H_E_90 = []
        H_E_95 = []
        H_E_98 = []
        for line in infile: 
            E.append(float(line[4:14]))
            H_E_001.append(float(line[17:27]))
            H_E_003.append(float(line[30:40]))
            H_E_01.append(float(line[43:53]))
            H_E_03.append(float(line[56:66]))
            H_E_05.append(float(line[69:79]))
            H_E_07.append(float(line[82:92]))
            H_E_10.append(float(line[95:105]))
            H_E_15.append(float(line[108:118]))
            H_E_20.append(float(line[121:131]))
            H_E_30.append(float(line[134:144]))
            H_E_40. append(float(line[147:157]))
            H_E_50.append(float(line[160:170]))
            H_E_60.append(float(line[173:183]))
            H_E_70.append(float(line[186:196]))
            H_E_75.append(float(line[199:209]))
            H_E_80.append(float(line[212:222]))
            H_E_85.append(float(line[225:235]))
            H_E_90.append(float(line[238:248]))
            H_E_95.append(float(line[251:261]))
            H_E_98.append(float(line[264:274]))
        
        infile = close()
        
        saving_final_ls(pathout, RANGEVALUE, E,H_E_001, set_this_loop, '0001')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_003, set_this_loop, '0003')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_01, set_this_loop, '001')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_03, set_this_loop, '003')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_05, set_this_loop, '005')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_07, set_this_loop, '007')
        saving_final_ls(pathout, RANGEVALUE,  E,H_E_10, set_this_loop, '01')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_15, set_this_loop, '015')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_20, set_this_loop, '02')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_30, set_this_loop, '03')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_40, set_this_loop, '04')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_50, set_this_loop, '05')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_60, set_this_loop, '06')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_70, set_this_loop, '07')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_75, set_this_loop, '075')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_80, set_this_loop, '08')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_85, set_this_loop, '085')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_90, set_this_loop, '09')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_95, set_this_loop, '095')
        saving_final_ls(pathout, RANGEVALUE, E,H_E_98, set_this_loop, '098')
        
        
    return 0




def divide_spw_into_sets(path2input, path2output):
    """
        Loop in to divide the file on the 18 sets.
    """
    big_file = open(path2input, 'r')    # splitting each set into this length

    alldata = big_file.readlines()
    big_file.close()
    set_this_loop = 1
    split_len = 279 
    
    for lines in range(0,len(alldata)-1, split_len):
        
        output_data = alldata[lines: lines + split_len]
        
        outfile = 'set%d.dat' %(set_this_loop)
        path2outfile = path2output + outfile
        output = open(path2outfile, 'w')
        output.write(' '.join(output_data))
        output.close()  
        
        set_this_loop += 1 
    
    return 0





def reduce_spw_data():
    """
        Formats spw data to a suitable format.
    """
     
    divide_spw_into_sets(PATH2_RAW_SPW_DATA, PATH2_REDUCED_SPW_DATA[0])  
    divide_spw_sets_into_l(PATH2_REDUCED_SPW_DATA[0], PATH2_REDUCED_SPW_DATA[1], RANGEVALUE = 0)
    divide_spw_sets_into_l(PATH2_REDUCED_SPW_DATA[0], PATH2_REDUCED_SPW_DATA[2], RANGEVALUE = 1)  

    return 0