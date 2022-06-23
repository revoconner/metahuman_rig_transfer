from maya import cmds
import maya.api.OpenMaya as om
import os 
import maya.mel as mel

cmds.select( clear=True )
cmds.select('DHIhead:spine_04')
children_joints = cmds.listRelatives(allDescendents=True, type='joint')
cmds.select(children_joints, add=True)
nameC = 0
while nameC < len(children_joints):
	#print(children_joints[nameC])
	cmds.rename ("%s"%(children_joints[nameC]), ":root:%s"%(children_joints[nameC]))
	nameC = nameC+1


cmds.rename ('DHIhead:spine_04', ':root:spine_04')