import sympy as sp
from sympy.matrices import rot_axis3

# Para el ejemplo donde generamos la matriz DH
from spatialmath import *
from spatialmath.base import *

# Para poder Graficar
import matplotlib.pyplot as plt
import numpy as np

#Para usar el DH
import roboticstoolbox as rtb

L1 = 0.400  #Vamos a usar estos valores
L2 = 0.300

robot = rtb.DHRobot(
    [
        rtb.RevoluteDH(d=0, a=L1, alpha=0, qlim=[-2.61, 2.61]),
        rtb.RevoluteDH(d=0, a=L2, alpha=0, qlim=[-2.61, 2.61]),
    ],
    name="2Links", base=SE3(0, 0, 0)
)

print(robot)

#Validamos con la directa el DH
#Para modificar los angulos comodamente
joint1 = 30  #En grados
joint2 = 30

T = robot.fkine([np.deg2rad(joint1), np.deg2rad(joint2)])
print(T)

Tn = np.array(T).astype(np.float64)  #Convertir a numpy

print(f"Los ángulos en la Cdirecta son ({joint1:.2f},{joint2:.2f})")
print(f"La coordenada es ({Tn[0, 3]:.3f},{Tn[1, 3]:.3f}), que pasamos a la inversa...")
