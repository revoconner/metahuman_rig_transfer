from maya import cmds
import maya.api.OpenMaya as om
import os 

#Enter Wrapped Head Mesh Name below
enter_wrapped_mesh_name = "NewHead"

#Enter folder path below where additional scripts are stored. Do not change slash to forward slash
folder_path = "C:\Maya\Journalist\scripts"
python_folder_path = folder_path.replace("\\", "/")

#Alright lets go


cmds.select( clear=True )
cmds.duplicate('DHIhead:spine_04')

def select_loop_bones():
    from maya import cmds
    import maya.api.OpenMaya as om
    import os 


    #giving OG and old mesh a variable name//edit mesh name here
    cmds.select('head_lod0_mesh')
    ogmesh = cmds.ls( selection=True )

    cmds.select(enter_wrapped_mesh_name)
    newmesh = cmds.ls( selection=True )

    #selecting the bone//edit the bone name here
    cmds.select('spine_05', hierarchy=True)
    bone_List = cmds.ls( selection=True )
    cmds.select( clear=True )

    #Starting bone loop
    boneID = 0
    while boneID < len(bone_List):
        bone = bone_List[boneID]
        
        #run OG_Mesh file
        execfile('%s/OG_Mesh.py'%python_folder_path)
        #run Get_Bone_Data file
        execfile('%s/Get_Bone_Data.py'%python_folder_path)
        #run New_Mesh file
        execfile('%s/New_Mesh.py'%python_folder_path)
        #run Vertex_Offset file
        execfile('%s/Vertex_Offset.py'%python_folder_path)
        #run Set_Bone_data file
        execfile('%s/Set_Bone_Data.py'%python_folder_path)
        
        boneID = boneID+1

select_loop_bones()
cmds.select( clear=True )

def move_constraint():
    #move neck_01 parent bone
    cmds.select('DHIhead:neck_01')
    neck_01DHIB = cmds.ls( selection=True )
    cmds.select('neck_01')
    neck_01B = cmds.ls( selection=True )

    neck_01B_XF = cmds.xform(neck_01B,q=1,ws=1,t=1)
    cmds.move( neck_01B_XF[0], neck_01B_XF[1], neck_01B_XF[2], neck_01DHIB, absolute=True, ws=True )

    #move FACIAL_C_Neck1Root parent bone
    cmds.select('DHIhead:FACIAL_C_Neck1Root')
    FACIAL_C_Neck1RootDHIB = cmds.ls( selection=True )
    cmds.select('FACIAL_C_Neck1Root')
    FACIAL_C_Neck1RootB = cmds.ls( selection=True )

    FACIAL_C_Neck1RootB_XF = cmds.xform(FACIAL_C_Neck1RootB,q=1,ws=1,t=1)
    cmds.move( FACIAL_C_Neck1RootB_XF[0], FACIAL_C_Neck1RootB_XF[1], FACIAL_C_Neck1RootB_XF[2], FACIAL_C_Neck1RootDHIB, absolute=True, ws=True )

    #move neck_02 parent bone
    cmds.select('DHIhead:neck_02')
    neck_02DHIB = cmds.ls( selection=True )
    cmds.select('neck_02')
    neck_02B = cmds.ls( selection=True )

    neck_02B_XF = cmds.xform(neck_02B,q=1,ws=1,t=1)
    cmds.move( neck_02B_XF[0], neck_02B_XF[1], neck_02B_XF[2], neck_02DHIB, absolute=True, ws=True )

    #move FACIAL_C_Neck2Root parent bone
    cmds.select('DHIhead:FACIAL_C_Neck2Root')
    FACIAL_C_Neck2RootDHIB = cmds.ls( selection=True )
    cmds.select('FACIAL_C_Neck2Root')
    FACIAL_C_Neck2RootB = cmds.ls( selection=True )

    FACIAL_C_Neck2RootB_XF = cmds.xform(FACIAL_C_Neck2RootB,q=1,ws=1,t=1)
    cmds.move( FACIAL_C_Neck2RootB_XF[0], FACIAL_C_Neck2RootB_XF[1], FACIAL_C_Neck2RootB_XF[2], FACIAL_C_Neck2RootDHIB, absolute=True, ws=True )


    #move head parent bone
    cmds.select('DHIhead:head')
    headDHIB = cmds.ls( selection=True )
    cmds.select('head')
    headB = cmds.ls( selection=True )

    headB_XF = cmds.xform(headB,q=1,ws=1,t=1)
    cmds.move( headB_XF[0], headB_XF[1], headB_XF[2], headDHIB, absolute=True, ws=True )

    #move FACIAL_C_FacialRoot parent bone
    cmds.select('DHIhead:FACIAL_C_FacialRoot')
    FACIAL_C_FacialRootDHIB = cmds.ls( selection=True )
    cmds.select('FACIAL_C_FacialRoot')
    FACIAL_C_FacialRootB = cmds.ls( selection=True )

    FACIAL_C_FacialRootB_XF = cmds.xform(FACIAL_C_FacialRootB,q=1,ws=1,t=1)
    cmds.move( FACIAL_C_FacialRootB_XF[0], FACIAL_C_FacialRootB_XF[1], FACIAL_C_FacialRootB_XF[2], FACIAL_C_FacialRootDHIB, absolute=True, ws=True )

move_constraint()
cmds.select( clear=True )

def rl4_node_op():

    #getting all bones connected to rl4 node
    rigBoneLists = []
    rigBones = []
    rigBoneStrippedList = []
    jto = 0
    while jto < 2563:
        jto_ID = 'rigLogicNode.jntTranslationOutputs[%s]'%jto
        rigBoneLists.append(cmds.connectionInfo( jto_ID, destinationFromSource = 1))
        rigBones.append(rigBoneLists[jto][0])
        rigBoneStripped = rigBones[jto][:-11]

        
        rigBoneStrippedList.append(rigBoneStripped)
        jto = jto+1
        


    ndBoneList = []
    for nd in rigBoneStrippedList:
        if nd not in ndBoneList:
            ndBoneList.append(nd)
            

    #get same duplicate bone
    dupNDBoneList = []
    offsetLIST = []

    preffix = "DHIhead:"

    ndBoneList_ID1 = 0
    while ndBoneList_ID1 < len(ndBoneList):
        dupBoneNameE = ndBoneList[ndBoneList_ID1]
        duplicateBoneName = dupBoneNameE[len(preffix):]
        dupNDBoneList.append(duplicateBoneName)
        
        #getting each of the two sets of bones
        OriginalBoneListID = ndBoneList[ndBoneList_ID1]
        DuplicateBoneListID = dupNDBoneList[ndBoneList_ID1]
        
        #getting translate value of Original Bone List with each ID
        TranslateX_OBLI = cmds.getAttr("%s.translateX" % OriginalBoneListID)
        TranslateY_OBLI = cmds.getAttr("%s.translateY" % OriginalBoneListID)
        TranslateZ_OBLI = cmds.getAttr("%s.translateZ" % OriginalBoneListID)
        
        #getting translate value of Duplicated Bone List with each ID
        TranslateX_DBLI = cmds.getAttr("%s.translateX" % DuplicateBoneListID)
        TranslateY_DBLI = cmds.getAttr("%s.translateY" % DuplicateBoneListID)
        TranslateZ_DBLI = cmds.getAttr("%s.translateZ" % DuplicateBoneListID)
        
        #calculating different between Duplicated bones and DHI	
        ADL_X = TranslateX_DBLI - TranslateX_OBLI
        ADL_Y = TranslateY_DBLI - TranslateY_OBLI
        ADL_Z = TranslateZ_DBLI - TranslateZ_OBLI
        
        
        offsetLIST.append(ADL_X)
        offsetLIST.append(ADL_Y)
        offsetLIST.append(ADL_Z)
        
        
        ndBoneList_ID1 = ndBoneList_ID1 + 1
        

    del offsetLIST[987]
    del offsetLIST[987]
    del offsetLIST[1951]
    del offsetLIST[1952]
    del offsetLIST[2390]


    #using ADL to RL4 Node


    bone_TransformID = 0
    while bone_TransformID < len(rigBones):
        bone_transform = rigBones[bone_TransformID]
        #Create Add Double Linear Node and connect them
        adlName = 'ADL_%s'%rigBones[bone_TransformID]
        adlName1 = adlName.replace(":","")
        adlName2 = adlName1.replace(".","_")
        
        #create ADL node
        cmds.createNode( 'addDoubleLinear', n=adlName2 )
        rlno = 'rigLogicNode.jntTranslationOutputs[%s]'%bone_TransformID
        adlNNI = '%s.input1'%adlName2
        
        #Connect ADL to RL4
        cmds.connectAttr(rlno, adlNNI)
        bo = rigBones[bone_TransformID]
        adlNNO = '%s.output'%adlName2
        
        #Connect ADL to Joint
        cmds.connectAttr(adlNNO, bo, force=1)
        
        #Give ADL I2 Values	
        adlNNI2 = '%s.input2'%adlName2	
        cmds.setAttr(adlNNI2, offsetLIST[bone_TransformID])
        
        
        bone_TransformID = bone_TransformID+1
        
rl4_node_op()
cmds.select( clear=True )
cmds.delete('spine_04')
#confirm box
cmds.confirmDialog( title='Reset Done', message='Proceed now', button=['Yes'], defaultButton='Yes', dismissString='No' )
