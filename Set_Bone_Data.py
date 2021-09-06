from maya import cmds
import maya.api.OpenMaya as om

selected = cmds.select(bone)
#cmds.xform(selected,ws=1,t=(offsetX, offsetY, offsetZ))
cmds.move( offsetX, offsetY, offsetZ, absolute=True, ws=True, pcp=True )