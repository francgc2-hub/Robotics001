import sympy as sp
from sympy.matrices import rot_axis3

# Para poder Graficar
import matplotlib.pyplot as plt
import numpy as np

# Para generar la matriz DH
from spatialmath import *
from spatialmath.base import *

# Definir los símbolos
theta, d, a, alpha = sp.symbols('theta, d, a, alpha')

# Matriz RzTzTxRx
TDH = trotz(theta) @ transl(0, 0, d) @ transl(a, 0, 0) @ trotx(alpha)
#sp.pprint(TDH)
#print(type(TDH))

# Declarandola explicitamente
T = sp.Matrix([
    [sp.cos(theta), -sp.sin(theta) * sp.cos(alpha),  sp.sin(theta) * sp.sin(alpha), a * sp.cos(theta)],
    [sp.sin(theta),  sp.cos(theta) * sp.cos(alpha), -sp.cos(theta) * sp.sin(alpha), a * sp.sin(theta)],
    [0,              sp.sin(alpha),                 sp.cos(alpha),                  d],
    [0,              0,                             0,                              1]
])

#sp.pprint(T)
#print(type(T))

theta_1, theta_2, theta_3, theta_4, theta_5, theta_6 = sp.symbols(
    'theta_1, theta_2, theta_3, theta_4, theta_5, theta_6'
)

# De la tabla DH
T01 = T.subs({d: 0.365, a: 0.050, alpha: -sp.pi/2})
T01 = T01.subs({theta: theta_1})

#sp.pprint(T01)

T12 = T.subs({d: 0, a: 0.370, alpha: 0})  # theta2 - sp.pi/2 (si aplica, ponlo en theta)
T12 = T12.subs({theta: theta_2})

#sp.pprint(T12)

T23 = T.subs({d: 0, a: 0.050, alpha: -sp.pi/2})
T23 = T23.subs({theta: theta_3})

#sp.pprint(T23)

T34 = T.subs({d: 0.38594, a: 0, alpha: sp.pi/2})  
T34 = T34.subs({theta: theta_4})

#sp.pprint(T34)

T45 = T.subs({d: 0, a: 0, alpha: -sp.pi/2}) # theta5 - sp.pi/2 (si aplica, ponlo en theta)
T45 = T45.subs({theta: theta_5})

#sp.pprint(T45)  

T56 = T.subs({d: 0.080, a: 0, alpha: 0}) # theta6 - sp.pi/2 (si aplica, ponlo en theta)
T56 = T56.subs({theta: theta_6})    

#sp.pprint(T56)

T06 = T01 @ T12 @ T23 @ T34 @ T45 @ T56
T06_s = T06.applyfunc(sp.simplify)
#sp.pprint(T06_s)

# EJEMPLO Y VALIDACION RAPIDA
# Para modificar los angulos comodamente
joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0) - sp.pi/2  # Offset
joint3 = np.deg2rad(0)
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0) 
joint6 = np.deg2rad(0) 

T06_solved = T06_s.subs({
    theta_1: joint1,
    theta_2: joint2,
    theta_3: joint3,
    theta_4: joint4,
    theta_5: joint5,
    theta_6: joint6,
})

sp.pprint(T06_solved)

# Crear figura una sola vez
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

T01_n = np.array(T01.subs({theta_1: joint1})).astype(np.float64)
T02_n = T01_n @ np.array(T12.subs({theta_2: joint2})).astype(np.float64)
T03_n = T02_n @ np.array(T23.subs({theta_3: joint3})).astype(np.float64)
T04_n = T03_n @ np.array(T34.subs({theta_4: joint4})).astype(np.float64)
T05_n = T04_n @ np.array(T45.subs({theta_5: joint5})).astype(np.float64)
T06_n = T05_n @ np.array(T56.subs({theta_6: joint6})).astype(np.float64)
T06_final = np.array(T06_solved).astype(np.float64)

# Crear matriz 4x4 para T0
T0_4x4 = np.eye(4)
T0_4x4[:3, :3] = np.array(rotz(0, unit='deg')).astype(np.float64)

frames = [
    (T0_4x4, 'k', '0'),
    (T01_n, 'b', '1'),
    (T02_n, 'r', '2'),
    (T03_n, 'g', '3'),
    (T04_n, 'm', '4'),
    (T05_n, 'y', '5'),
    (T06_n, 'c', '6'),
    (T06_final, 'purple', 'f'),
]

for frame, color, label in frames:
    frame = np.array(frame).astype(np.float64)
    # Dibujar origen
    ax.scatter(*frame[:3, 3], color=color, s=50)
    # Dibujar ejes
    for i in range(3):
        end = frame[:3, 3] + frame[:3, i] * 0.2
        ax.plot([frame[0, 3], end[0]], [frame[1, 3], end[1]], [frame[2, 3], end[2]], color=color, linewidth=1)
    # Etiqueta
    ax.text(frame[0, 3], frame[1, 3], frame[2, 3], label, fontsize=10, color=color)

ax.grid(True)
ax.set_title('ABB 140-6')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_box_aspect([1,1,1])
plt.show()