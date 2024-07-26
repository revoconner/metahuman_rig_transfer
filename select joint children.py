from maya import cmds
children_joints = cmds.listRelatives(allDescendents=True, type='joint')
cmds.select(children_joints, add=True)
