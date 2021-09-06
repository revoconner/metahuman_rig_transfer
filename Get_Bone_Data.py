from maya import cmds
import maya.api.OpenMaya as om

selected = cmds.select(bone)
b = cmds.xform(selected,q=1,ws=1,t=1)
bx = b[0]
by = b[1]
bz = b[2]
BonePoint = om.MPoint(b)


#loop to get distances of each verts from the selected bone 
R = 0
distList = []
while R < length:
	distance  = BonePoint.distanceTo(mfn_mesh1.getPoint(R, space=om.MSpace.kWorld))	
	distList.append(distance)
	R=R+1
	

#find the min distance vertex ID
minDist = (min(distList))
minDistID = (distList.index(min(distList)))

#giving the M1 variables the coordinates of the closest vertex to the bone
pointMin = mfn_mesh1.getPoint(minDistID, space=om.MSpace.kWorld)	
M1X = pointMin.x
M1Z = pointMin.z
M1Y = pointMin.y
