import sympy as sp
from sympy.matrices import rot_axis3
# Para el ejemplo donde generamos la matriz DH
from spatialmath import *
from spatialmath.base import *
# Para poder Graficar
import matplotlib.pyplot as plt
import numpy as np

# Definir los simbolos
theta, d, a, alpha = sp.symbols('theta, d, a, alpha')

T = sp.Matrix([
    [sp.cos(theta), -sp.sin(theta) * sp.cos(alpha),  sp.sin(theta) * sp.sin(alpha), a * sp.cos(theta)],
    [sp.sin(theta),  sp.cos(theta) * sp.cos(alpha), -sp.cos(theta) * sp.sin(alpha), a * sp.sin(theta)],
    [0,              sp.sin(alpha),                 sp.cos(alpha),                 d],
    [0,              0,                             0,                             1]
])

#sp.pprint(T)

#Definimos los angulos para que cada uno sea unico
theta_1, theta_2, theta_3, theta_4, theta_5, theta_6 = \
    sp.symbols('theta_1, theta_2,theta_3, theta_4,theta_5, theta_6')

#De la tabla
T01 = T.subs({d: 0.680, a: 0.200, alpha: -sp.pi/2})
T01 = T01.subs({theta: theta_1})
# sp.pprint(T01)

T12 = T.subs({d: 0, a: 0.890, alpha: 0})  # theta2 - sp.pi/2
T12 = T12.subs({theta: theta_2})
# sp.pprint(T12)

T23 = T.subs({d: 0, a: 0.150, alpha: -sp.pi/2})
T23 = T23.subs({theta: theta_3})
# sp.pprint(T23)

T34 = T.subs({d: 0.880, a: 0, alpha: sp.pi/2})
T34 = T34.subs({theta: theta_4})
# sp.pprint(T34)

T45 = T.subs({d: 0, a: 0, alpha: -sp.pi/2})
T45 = T45.subs({theta: theta_5})
# sp.pprint(T45)

T56 = T.subs({d: 0.140, a: 0, alpha: 0})
T56 = T56.subs({theta: theta_6})
# sp.pprint(T56)