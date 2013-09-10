
"""


X-ray bursting neutron stars in low mass X-ray binaries (LMXB) was recognized
as a source to constrain masses and radii of neutron stars. For this purpose, an 
extended set of atmosphere models is necessary.

This program is based on Suleimanov et al (2010). We perform similar analysis
shown in that paper, reproducing their results.

(Steinkirch and Medin, Fall/2012)


"""


if __name__ == '__main__':
    pass


from processing import *


"""

Processing data from SPW,2010

"""

source = 'spw'
print "Processing data from source %s..." %source



dataset = 4

Afile = "set%d.dat" %dataset
outfolder = "../output/" + source
folder = "../data/%s/" %source 
path = folder + Afile

print "Processing data from set %d..." %dataset
processing_data(path, dataset, outfolder)




dataset = 8  

Afile = "set%d.dat" %dataset
outfolder = "../output/" + source
folder = "../data/%s/" %source 
path = folder + Afile

print "Processing data from set %d..." %dataset
processing_data(path, dataset, outfolder)


