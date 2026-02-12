import roboticstoolbox as rtb
import numpy as np

print(f"Version de roboticstoolbok¿ {rtb.__version__}")
print(f"Version de numpy¿ {np.__version__}")

robot = rtb.models.DH.Puma560()

#Variables articulares
q = ([0, np.deg2rad(30), -np.deg2rad(160), 0, 0, 0])

# Visualizar

#robot.plot(q, block=True, backend='pyplot')
#Si se downgradeo matplotlib 3.83
robot.teach(robot.q)