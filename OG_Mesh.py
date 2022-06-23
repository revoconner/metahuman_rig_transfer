from maya import cmds
import maya.api.OpenMaya as om
# get the mesh vertex position
sel1 = cmds.ls(ogmesh)
# get the dag path 
selection_list = om.MSelectionList ()
selection_list.add(sel1[0])
dag_path = selection_list.getDagPath (0)
# creating Mfn Mesh
mfn_mesh1 = om.MFnMesh(dag_path)

#get the full number of vertex in mesh for loop
pp = mfn_mesh1.getPoints()
length = len(pp)

#looping to get vertex coordinates of all points in first mesh
Q = 0
while Q < length:
	points1 = mfn_mesh1.getPoint(Q, space=om.MSpace.kWorld)	
	Q = Q+1

