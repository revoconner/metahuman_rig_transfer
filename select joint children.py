from maya import cmds
import maya.api.OpenMaya as om
import os 
children_joints = cmds.listRelatives(allDescendents=True, type='joint')

cmds.select(children_joints, add=True)
print(len(children_joints))
nameC = 0
while nameC < len(children_joints):
	print(children_joints[nameC])
	nameC = nameC+1