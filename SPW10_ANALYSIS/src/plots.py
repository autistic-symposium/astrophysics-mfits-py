import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})#
rc('text', usetex=True)
from blackbody import *

"""
This module has the functions for all the plots from Suleimanov et al, 2011.

"""



def plot_fig3(data, dataset, outfolder):
    """
    This function just plot the H_E vs E from the table (just visualization of the data).
    
    """
    
    plt.figure()
    file = '/set_%d_fig3.png' %dataset
    out = outfolder + file
    
    plt.loglog(data[0][0], data[0][1])
    plt.loglog(data[0][0], data[0][3])
    plt.loglog(data[0][0], data[0][7])
    plt.loglog(data[0][0], data[0][12])
    
    plt.xlabel('$E (keV)$',fontdict={'fontsize':20})
    plt.ylabel('$H_E$(erg s$^{-1}$ cm$^{-2}$ keV$^{-1}$)',fontdict={'fontsize':20})
    plt.title('Emergent (unredshifted) spectra for dataset %d' %dataset,fontdict={'fontsize':14})
    plt.legend(('$l=0.001$',  '$l=0.01$', '$l=0.1$','$l=0.5$'),
           'lower left', shadow=True, fancybox=True)
    plt.axis([3.2, 20,1e14,1e24], fontdict={'fontsize':18},gridsize=10)
    
    plt. savefig(out)
    print "Fig. 3 from was written in %s." %out
    return 0



def plot_fig7(data, fc, dataset, outfolder):
    """
    This plot compares the first and the fourth fits, to verify the accuracy of a one-parameter
    fitting to a two-parameter fitting.
    
    """
    
    plt.figure()
    file = '/set_%d_fig7.png' %dataset
    out = outfolder + file
    
    plt.loglog(data[0][0], (blackbody(fc[0][0], data[0][0], 0)), 'm')
    plt.loglog(data[0][0], (blackbody(fc[0][3], data[0][0], 0)), 'm--')
    plt.loglog(data[0][0], (blackbody(fc[19][0], data[0][0], 19)), 'r')
    plt.loglog(data[0][0], (blackbody(fc[19][3], data[0][0], 19)), 'r--')
    plt.loglog(data[0][0], (blackbody(x0, data[0][0], 0)), 'b')
    plt.loglog(data[0][0], (blackbody(x0, data[0][0], 19)), 'b')
    
    
    plt.xlabel('$E (keV)$',fontdict={'fontsize':20})
    plt.ylabel('$H_E$(erg s$^{-1}$ cm$^{-2}$ keV$^{-1})$',fontdict={'fontsize':20})  
    plt.title(' Examples of computed Spectra by the $1^{rt}$ and $4^{nd}$ Fit Procedure, for dataset %d' %dataset,fontdict={'fontsize':12})
    plt.axis([3.2, 20,1e14,1e24], fontdict={'fontsize':18},gridsize=10)
    plt.legend(('$l=0.001$, first fit', '$l=0.001$, fourth fit', '$l=0.95$, first fit', '$l=0.95$, fourth fit', '$l=0.001$, BB', '$l=0.95$, BB'),'lower left', shadow=True, fancybox=True)
    
    plt. savefig(out) 
    print "Fig. 7 from was written in %s." %out
    return 0




def plot_fig8(data, fc, dataset, outfolder):
    """
    This plot compares the first and the second fits, to verify the residual energy dependence.
    
    """
    
    plt.figure()
    file = '/set_%d_fig8.png' %dataset
    out = outfolder + file
    
    plt.semilogx(data[0][0], (0.2+blackbody(fc[7][0], data[0][0], 7)/(data[0][8]/(4*pi)) ) -1, 'm')
    plt.semilogx(data[0][0], (0.2+blackbody(fc[7][1], data[0][0], 7)/(data[0][8]/(4*pi))) -1, 'm--')
    plt.semilogx(data[0][0], (0.1+blackbody(fc[12][0], data[0][0], 12)/(data[0][13]/(4*pi))) -1, 'b')
    plt.semilogx(data[0][0], (0.1+blackbody(fc[12][1], data[0][0], 12)/(data[0][13]/(4*pi))) -1, 'b--')
    plt.semilogx(data[0][0], (blackbody(fc[19][0], data[0][0], 19)/(data[0][20]/(4*pi))) -1, 'r')
    plt.semilogx(data[0][0], (blackbody(fc[19][1], data[0][0], 19)/(data[0][20]/(4*pi)))-1, 'r--')
    
    plt.xlabel('$E (keV)$',fontdict={'fontsize':20})
    plt.ylabel('$H_E(fit)$/$H_E^{-1}$',fontdict={'fontsize':20})
    plt.title('Relative Errors of the Computed Spectra by the $1^{rt}$ and $2^{nd}$ Fit Procedure, for dataset %d' %dataset,fontdict={'fontsize':12})
    plt.axis([3.2, 20,-0.05,0.3], fontdict={'fontsize':18},gridsize=10)
    plt.legend(('$l=0.1$, first fit', '$l=0.1$, second fit', '$l=0.5$, first fit', '$l=0.5$, second fit', '$l=0.95$, first fit', '$l=0.95$, second fit'),
           'upper left', shadow=True, fancybox=True)
    
    plt. savefig(out)
    print "Fig. 8 from was written in %s." %out
    return 0




def plot_fig9_a(l, fc1, fc2, fc3, fc4, fc5, dataset, outfolder):
    """
    This plot show the dependence of the color correction factor on the relative luminosity 
    for the surface gravity calculated by the 5 procedures.
    
    """
    
    plt.figure()
    file = '/set_%d_fig9a.png' %dataset
    out = outfolder + file
    
    plt.plot(l, fc1,  'b')
    plt.plot(l, fc2,  'b--')
    plt.plot(l, fc3, 'b-.')
    plt.plot(l, fc4, 'b.')
    plt.plot(l, fc5, 'bo')
    
    plt.xlabel('$L/L_{Edd}$',fontdict={'fontsize':20})
    plt.ylabel('Color correction $f_{c}$',fontdict={'fontsize':20})
    plt.title('Dependence of the Color Correction Factors to the Luminosity, for dataset %d' %dataset,fontdict={'fontsize':12})
    plt.axis([-0.05, 1.0,1.0,2.1], fontdict={'fontsize':18},gridsize=10)
    plt.legend(('First fit', 'Second fit', 'Third fit', 'Fourth fit', 'Fifth fit'),'lower right', shadow=True, fancybox=True)
    
    plt. savefig(out)
    print "Fig. 9a from was written in %s." %out
    return 0
    
    
def plot_fig9_b(l, fc1, fc2, fc3, fc4, fc5, dataset, outfolder):
    """
    This plot show the dependence of the normalized color correction factor 
    (to the first fit procedure) on the relative luminosity for the surface.
    """
    
    plt.figure()
    file = '/set_%d_fig9b.png' %dataset
    out = outfolder + file
    
    afc1 = array(fc1)
    afc2 = array(fc2)
    afc3 = array(fc3)
    afc4 = array(fc4)
    afc5 = array(fc5)

    plt.plot(l, afc2/afc1,  'r--')
    plt.plot(l, afc3/afc1, 'bo')
    plt.plot(l, afc4/afc1, 'g')
    plt.plot(l, afc5/afc1, '-.')

    plt.xlabel('$L/L_{Edd}$',fontdict={'fontsize':20})
    plt.ylabel('$f_{c,i}/f_{c,1}$',fontdict={'fontsize':20})
    plt.title('Ratio of the first Color Correction Factor to the other 4 fits  vs Luminosity, for dataset %d' %dataset,fontdict={'fontsize':12})
    plt.axis([0, 1.0,0.5,1.2], fontdict={'fontsize':18},gridsize=10)
    plt.legend(('$f_{c,2}/f_{c,1}$', '$f_{c,3}/f_{c,1}$', '$f_{c,4}/f_{c,1}$', '$f_{c,5}/f_{c,1}$'),'lower right', shadow=True, fancybox=True)
    
    plt. savefig(out)
    print "Fig. 9b from was written in %s." %out
    return 0



def plot_fig10_a(l, w1, w2, w3, w4, dataset, outfolder):
    """
    This plot show the dependence of dilution factor on the relative luminosity 
    for the surface gravity calculated by the 4 procedures.
    
    """
    
    plt.figure()
    file = '/set_%d_fig10a.png' %dataset
    out = outfolder + file
    
    plt.plot(l, w1,  'y.-')
    plt.plot(l, w2,  'r--')
    plt.plot(l, w3, 'bo')
    plt.plot(l, w4, '-.')
    
    plt.xlabel('$L/L_{Edd}$',fontdict={'fontsize':20})
    plt.ylabel('Dilution factor $w$',fontdict={'fontsize':20})
    plt.title('Dependence of the Dilution Factors to the Luminosity, for dataset %d' %dataset,fontdict={'fontsize':12})
    plt.axis([0, 1.0,0,0.7], fontdict={'fontsize':18},gridsize=10)
    plt.legend(('First fit', 'Second fit', 'Third fit', 'Fourth fit'),'lower right', shadow=True, fancybox=True)
    
    plt. savefig(out)
    print "Fig. 10a from was written in %s." %out
    return 0
    
    
def plot_fig10_b(l, w1, w2, w3, w4, dataset, outfolder):
    """
    This plot show the dependence of the normalized dilution factor
    (to the first fit procedure) on the relative luminosity for8 the surface.
    """
    
    plt.figure()
    file = '/set_%d_fig10b.png' %dataset
    out = outfolder + file
    
    aw1 = array(w1)
    aw2 = array(w2)
    aw3 = array(w3)
    aw4 = array(w4)

    plt.plot(l, aw2/aw1,  'r--')
    plt.plot(l, aw3/aw1, 'bo')
    plt.plot(l, aw4/aw1, 'g')
    
    plt.xlabel('$L/L_{Edd}$',fontdict={'fontsize':20})
    plt.ylabel('$w_{c,i}/w_{c,1}$',fontdict={'fontsize':20})
    plt.title('Ratio of the first dilution factor to the other 4 fits vs Luminosity, for dataset %d' %dataset,fontdict={'fontsize':12})
    plt.axis([0, 1.0,0.8,1.8], fontdict={'fontsize':18},gridsize=10)
    plt.legend(('$w_{2}/w_{1}$', '$w_{3}/w_{1}$', '$w_{4}/w_{1}$'),'lower right', shadow=True, fancybox=True)
    
    plt. savefig(out)
    print "Fig. 10b from was written in %s." %out
    return 0