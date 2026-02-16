import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

from sympy import Symbol, Matrix

#theta = Symbol('theta')
#R = Matrix(rot2(theta))

theta_deg = 30
theta_rad = np.deg2rad(30)

R = rot2(theta_rad)
print(R)

#Ahora quiero la matriz de rotación con sympy   
R2 = trot2(theta_rad)
print(R2)

"""trplot2(R) #Dibujamos en plot la rotación 2D
plt.axis('equal')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Rotación 2D')
plt.show() """

T0 = transl2(0,0) #Referencia
trplot2(T0, frame='0', color='k')

#Traslación de 2,2 seguida de
TA = transl2(1,2)
print(TA)
trplot2(TA, frame='A', color='b')   

plt.axis('equal')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Transformación 2D')
plt.show()