import sympy as sp
from sympy.matrices import rot_axis3

import numpy as np
import matplotlib.pyplot as plt
plt.ion()

from spatialmath import *
from spatialmath.base import *

import roboticstoolbox as rtb

# Definimos robot scara
scara = rtb.DHRobot([
    rtb.RevoluteDH(d=0.160, a=0.350, alpha=0, qlim=[-2.58, 2.58]),
    rtb.RevoluteDH(d=0, a=0.300, alpha=0, qlim=[-2.61, 2.61]),
    rtb.PrismaticDH(theta=0, a=0, alpha=np.pi, offset=0.210, qlim=[-0.370, 0]),
    rtb.RevoluteDH(d=0, a=0, alpha=0, qlim=[-6.28, 6.28])
], name='SR6iA', base=SE3(0, 0, 0))
print(scara)

# Asignar las variables de los angulos y valores de desplazamiento
joint1 = np.deg2rad(30)  # Angulo de la primera articulación
joint2 = np.deg2rad(-60)  # Angulo de la segunda articulación
joint3 = -0.420  # Desplazamiento de la tercera articulación (offset +210)
joint4 = np.deg2rad(45)  # Angulo de la cuarta articulación

T04D=scara.fkine([joint1, joint2, joint3, joint4])
print(T04D)

q=np.array([[0, 0, 0, 0],
           [joint1, 0, 0, 0],
           [joint1, joint2, 0, 0],
           [joint1, joint2, joint3, 0],
           [joint1, joint2, joint3, joint4],
           [joint1, joint2, joint3, 0],
           [joint1, joint2, 0, 0],
           [joint1, 0, 0, 0],
           [0, 0, 0, 0]]
           )

# Graficar con posiciones q, una cada 3 segundos
scara.plot(q=q, backend='pyplot', dt=3, limits=[-0.8, 0.8, -0.8, 0.8, -0.4, 0.6], shadow=True, jointaxes=True)
plt.show(block=True)

# Graficar con controlador
q1=np.array([0, 0, 0, 0])
scara.teach(q1)