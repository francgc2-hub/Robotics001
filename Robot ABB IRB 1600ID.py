import sympy as sp
import numpy as np


theta, d, a, alpha = sp.symbols('theta d a alpha', real=True)

T = sp.Matrix([
    [sp.cos(theta), -sp.sin(theta), 0, a],
    [sp.sin(theta)*sp.cos(alpha), sp.cos(theta)*sp.cos(alpha), -sp.sin(alpha), -d*sp.sin(alpha)],
    [sp.sin(theta)*sp.sin(alpha), sp.cos(theta)*sp.sin(alpha),  sp.cos(alpha),  d*sp.cos(alpha)],
    [0, 0, 0, 1]
])

# Variables
theta_1, theta_2, theta_3, theta_4, theta_5, theta_6 = sp.symbols(
    'theta_1 theta_2 theta_3 theta_4 theta_5 theta_6', real=True
)

# Parametros

T01 = T.subs({
    d: 0.4865,
    a: 0.0,
    alpha: 0,
    theta: theta_1
})

T12 = T.subs({
    d: 0.0,
    a: 0.150,
    alpha: -sp.pi/2,
    theta: theta_2 - sp.pi/2
})

T23 = T.subs({
    d: 0.0,
    a: 0.700,
    alpha: 0,
    theta: theta_3
})

T34 = T.subs({
    d: 0.640,
    a: 0.110,
    alpha: -sp.pi/2,
    theta: theta_4
})

T45 = T.subs({
    d: 0.0,
    a: 0.0,
    alpha: sp.pi/2,
    theta: theta_5
})

T56 = T.subs({
    d: 0.200,
    a: 0.0,
    alpha: -sp.pi/2,
    theta: theta_6 + sp.pi
})

# Cinematica directa
T06 = sp.simplify(T01 @ T12 @ T23 @ T34 @ T45 @ T56)

sp.pprint(T06)

# Evaluacion

joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0)
joint3 = np.deg2rad(0)
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0)
joint6 = np.deg2rad(0)

T06_num = T06.subs({
    theta_1: joint1,
    theta_2: joint2,
    theta_3: joint3,
    theta_4: joint4,
    theta_5: joint5,
    theta_6: joint6
})

T06_num = sp.N(T06_num, 6)

sp.pprint(T06_num)

T06_np = np.array(T06_num.tolist(), dtype=float)

# Posicion
x_mm = T06_np[0, 3] * 1000
y_mm = T06_np[1, 3] * 1000
z_mm = T06_np[2, 3] * 1000

# Rotacion

R = T06_np[0:3, 0:3]

def rot_to_euler_zyx(R):
    rotZ = np.arctan2(R[1, 0], R[0, 0])
    rotY = np.arctan2(-R[2, 0], np.sqrt(R[2, 1]*2 + R[2, 2]*2))
    rotX = np.arctan2(R[2, 1], R[2, 2])
    return rotZ, rotY, rotX

rotZ, rotY, rotX = rot_to_euler_zyx(R)

rotZ_deg = np.rad2deg(rotZ)
rotY_deg = np.rad2deg(rotY)
rotX_deg = np.rad2deg(rotX)