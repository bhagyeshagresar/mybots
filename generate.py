import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])
pyrosim.Send_Cube(name="Box2", pos=[0,0.5,1.5] , size=[1,1,1])

pyrosim.End()

