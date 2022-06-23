from maya import cmds
import maya.api.OpenMaya as om
# get the mesh vertex position
sel2 = cmds.ls(newmesh)
# get the dag path
selection_list = om.MSelectionList ()
selection_list.add(sel2[0])
dag_path = selection_list.getDagPath (0)
# creating Mfn Mesh
mfn_mesh2 = om.MFnMesh(dag_path)

#creating M2 variables to store coordinate of the closest vertex in the new mesh 
points2 = mfn_mesh2.getPoint(minDistID, space=om.MSpace.kWorld)

M2X = points2.x
M2Z = points2.z
M2Y = points2.y
