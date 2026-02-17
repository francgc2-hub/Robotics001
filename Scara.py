import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

from sympy import Symbol, Matrix

T0 = transl2(0,0) #Referencia   
trplot2(T0, frame='0', color='k')   

#Rotación de seguida de translación, respecto a T0
TA = trot2(30, "deg") 
trplot2(TA, frame='A', color='b')
plot_circle(4, (0,0), 'b--')