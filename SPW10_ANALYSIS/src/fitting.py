from matplotlib.mlab import *
from scipy.optimize import leastsq
from constants import *
from fits import *


def performing_fits(x0, data):
    """
    This module perform all the five fits and extract fcs and ws.
    In the array, the first is the energy and the second the H_E column.
    
    """
    
    afc =[]
    for i in range(20):
        fc2 = []
        
        x01 = leastsq(fit1,x0, args=(data[0][0], data[0][i+1]/(4*pi), i))[0]
        fc2.append(x01)
        fc2.append(leastsq(fit2,x0, args=(data[0][0], data[0][i+1]/(4*pi), i))[0])
        fc2.append(leastsq(fit3,x01, args=(data[0][0], data[0][i+1]/(4*pi), i))[0])
        fc2.append(leastsq(fit1,x04, args=(data[0][0], data[0][i+1]/(4*pi), i))[0])
        fc2.append(fit5(x01, data[0][0], data[0][i+1]/(4*pi), i))
        
        afc.append(fc2)
   
    return afc



def saving_fcs(fc):
    """
    This module save the fcs in a more suitable way.
    
    """

    fc1 = []
    fc2 = []
    fc3 = [] 
    fc4 = [] 
    fc5 = []
    
    for i in range(20):
        fc1.append(fc[i][0][1])
        fc2.append(fc[i][1][1])
        fc3.append(fc[i][2][1])
        fc4.append(fc[i][3][1])
        fc5.append(fc[i][4][1])
        
    return fc1, fc2, fc3, fc4, fc5



def saving_ws(fc):
    """
    This module save the ws in a more suitable way.
    
    """
    
    w1 = []
    w2 = []
    w3 = [] 
    w4 = []
    fcw1 = []
    fcw2 = []
    fcw3 = []
    
    for i in range(20):
        w1.append(fc[i][0][0])
        w2.append(fc[i][1][0])
        w3.append(fc[i][2][0])
        w4.append(fc[i][3][0])
        fcw1.append(fc[i][0][0]*fc[i][0][1]**4)
        fcw2.append(fc[i][1][0]*fc[i][1][1]**4)
        fcw3.append(fc[i][2][0]*fc[i][2][1]**4)
        
    return w1, w2, w3, w4, fcw1, fcw2, fcw3