try:
    from roboticstoolbox.robot.BaseRobot import BaseRobot
    print('import succeeded')
except Exception as e:
    print('import failed', type(e), e)
