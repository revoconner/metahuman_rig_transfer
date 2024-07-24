from maya import cmds
import pymel.core as pm
import maya.api.OpenMaya as om
from collections import OrderedDict



class MetaHumanTransfer(object):
    '''
    Transfer MH rig between mesh of similar topology.
    Then rig weights and BS can be transferred to custom topology
    that matches MH head shape via Wrap3D.


    rigHead = (str) The name of the MH head mesh that is rigged and exported from Bridge
    newHead = (str) The name of the head you want to transfer MH rig to
    rlName  = (str) Name of the character that comes from the RL node:
    
    rlName:
        i.e. 'rl4Embedded_CharName_Identity_rl'
        Searh for 'rl4Embedded_*_Identity_rl' to located the character name on the node.


    To Use:
        import metahuman_transfer as mht
        a=None
        a=mht.MetaHumanTransfer('head_lod0_mesh', 'Object0000', 'Kioko')
        a.run()
    '''

    def __init__(self, rigHead, newHead, rlName):
        self.hierarchyDict = OrderedDict()
        self.rigHead = rigHead
        self.newHead = newHead
        self.rlName  = rlName

    def initDict(self):
        self.hierarchyDict = OrderedDict()


    def run(self):
        self.create_temp_hierarchy(self.rigHead, self.newHead)
        self.move_rigged_hierarchy()
        self.offset_rigged_hierarchy()



    def get_rig_mesh_data(self, headNme):
        # get the mesh vertex position
        
        # get the dag path 
        selection_list = om.MSelectionList()
        selection_list.add(headNme)
        dag_path = selection_list.getDagPath(0)
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

        return(length, mfn_mesh1)

    def get_new_mesh_data(self,headNme, minDistID):
        # get the mesh vertex position
        sel2 = cmds.ls(headNme)
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

        return(M2X, M2Z, M2Y)

    def get_bone_data(self, bone, length, mfnMsh):
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
            distance  = BonePoint.distanceTo(mfnMsh.getPoint(R, space=om.MSpace.kWorld)) 
            distList.append(distance)
            R=R+1

        #find the min distance vertex ID
        minDist = (min(distList))
        minDistID = (distList.index(min(distList)))

        #giving the M1 variables the coordinates of the closest vertex to the bone
        pointMin = mfnMsh.getPoint(minDistID, space=om.MSpace.kWorld)    
        M1X = pointMin.x
        M1Z = pointMin.z
        M1Y = pointMin.y

        return(bx, by, bz, M1X, M1Z, M1Y, minDistID)

    def get_vertex_offset(self, M2X, M2Z, M2Y, M1X, M1Z, M1Y, bx, by, bz):
        offsetX = M2X-(M1X-bx)
        offsetY = M2Y-(M1Y-by)
        offsetZ = M2Z-(M1Z-bz)

        return(offsetX, offsetY, offsetZ)

    def get_transform_offset(self, source, target, trs, axis):
        srcVal = cmds.getAttr(source+'.'+trs+axis.upper())
        tgtVal = cmds.getAttr(target+'.'+trs+axis.upper())
        offset = srcVal - tgtVal

        return offset

    def set_bone_data(self, bone, offsetX, offsetY, offsetZ):
        selected = cmds.select(bone)
        cmds.move( offsetX, offsetY, offsetZ, absolute=True, ws=True, pcp=True )

    def getHierarchyPM(self, source):
        '''
        Recursive method to list items in source hierarchy (pymel)
        '''
        if source.getChildren():
            for child in source.getChildren():
                self.hierarchyDict[child]=source
                self.getHierarchyPM(child)
        return self.hierarchyDict


    ####################################################################################

    def create_temp_hierarchy(self, rigHead, newHead):
        '''
        duplicate the neck and face joint structure
        and move it to match the newHead mesh

        rigHead = (str) Name of head that has MH rig and skincluster
        newhead = (str) Name of head you want to transfer rig to
        '''
        rigHead = self.rigHead
        newHead = self.newHead

        # Delete if exists
        if cmds.objExists('spine_04'):
            cmds.delete('spine_04')

        # Duplicate hierarchy and delete constraints
        cmds.duplicate('DHIhead:spine_04')
        allHier = pm.listRelatives('spine_04', ad=True)
        for i in allHier:
            if pm.objectType(i) != 'joint':
                pm.delete(i)

        # Place duplicate heiarachy on target head mesh
        bneLst = cmds.listRelatives('spine_05', ad=True, type='joint')
        bneLst.insert(0, 'spine_05')

        for num,bone in enumerate(bneLst):
            length, mfn_mesh1 = self.get_rig_mesh_data(rigHead)
            bx, by, bz, M1X, M1Z, M1Y, minDistID = self.get_bone_data(bone, length, mfn_mesh1)
            M2X, M2Z, M2Y = self.get_new_mesh_data(newHead, minDistID)
            offsetX, offsetY, offsetZ = self.get_vertex_offset(M2X, M2Z, M2Y, M1X, M1Z, M1Y, bx, by, bz)
            self.set_bone_data(bone, offsetX, offsetY, offsetZ)

    def move_rigged_hierarchy(self):
        '''
        Move the rigged neck and head joints to match temp hierarchy
        '''

        for jnt in ['neck_01', 'FACIAL_C_Neck1Root', 'neck_02', 'FACIAL_C_Neck2Root', 'head', 'FACIAL_C_FacialRoot']:
            nmeSpcJnt = 'DHIhead:'+jnt
            xf = cmds.xform(jnt,q=1,ws=1,t=1)
            cmds.xform(nmeSpcJnt, t=xf, ws=True)

    def offset_rigged_hierarchy(self):
        # Store RL connections to be retreived when connecting ADL node
        jntNum = len(cmds.listAttr('rl4Embedded_{}_Identity_rl.jntTranslationOutputs[*]'.format(self.rlName)))-1 # Last multi-port is not connected
        rlJntDict = OrderedDict()
        jto = 0
        while jto < jntNum:
            jto_ID = 'rl4Embedded_{}_Identity_rl.jntTranslationOutputs[{}]'.format(self.rlName, jto)
            rlJntDict[cmds.connectionInfo(jto_ID, destinationFromSource = 1)[0]]=jto_ID
            jto = jto+1

        # Get and apply offsets
        jntOrderDict = OrderedDict()
        jntOrderDict = self.getHierarchyPM(source=pm.PyNode('spine_04'))
        for k,v in jntOrderDict.items(): # new joint, new joint parent
            newJnt = k
            rigJnt = 'DHIhead:'+k

            for trs in ['translate']:
                for axis in 'XYZ':
                    if rlJntDict.get(rigJnt+'.'+trs+axis):
                        difVal = self.get_transform_offset(newJnt, rigJnt, trs, axis)

                        adlName = 'ADL_'+newJnt+'_'+trs+'_'+axis
                        adlName1 = adlName.replace(":","")
                        adlName2 = adlName1.replace(".","_")
                        
                        #create ADL node
                        ADL = pm.createNode('addDoubleLinear', n=adlName2, ss=True)
                        
                        #Connect RL to ADL
                        pm.connectAttr(rlJntDict.get(rigJnt+'.'+trs+axis), ADL+'.input1')
                        pm.setAttr(ADL+'.input2', difVal)
                        
                        #Connect ADL to Joint
                        pm.connectAttr(ADL+'.output', rigJnt+'.'+trs+axis, force=1)

        if cmds.objExists('spine_04'):
            cmds.delete('spine_04')