## NOT IN ACTIVE DEVELOPMENT

# Metahuman Rig Transfer Script
A series of python scripts to modify the metahuman rig into a new one for Maya. For unreal use Mesh to Metahuman or houdini.

Link to youtube video demo - https://www.youtube.com/watch?v=qF-z1aZQUYE

## Table of Content
1. [Prerequisite](https://github.com/revoconner/metahuman_rig_transfer#prerequisite)
2. [Instruction](https://github.com/revoconner/metahuman_rig_transfer#instructions)
3. [Optional Instruction](https://github.com/revoconner/metahuman_rig_transfer#optional)
4. [License](https://github.com/revoconner/metahuman_rig_transfer#license)
5. [FAQ](https://github.com/revoconner/metahuman_rig_transfer#FAQ)

## PREREQUISITE:
(written in Py 3.4)
#### Will not work in Maya 2020 and below. Use py-2 branch for older maya versions 
1. The new head to which the bones are to be rigged must share the same UV and topology as the original metahuman head. A program like R3DS Wrap will help with it. 
2. The file you download from Metahuman will have its embeddedNodeRL4 node named after the DNA_RL file, something like Kristopher_rl or rl4Embedded_Kristofer_rl, if the name of the metahuman was Kristopher. **Change that to rigLogicNode**
3. ![image](https://user-images.githubusercontent.com/88772846/132264485-74e9d98e-38d9-4227-ab56-1ca9fc5effd5.png)
4. ![image](https://user-images.githubusercontent.com/88772846/132264420-1128a2eb-d1f0-4ec2-bbdc-ea97e150c197.png)

### Good Practices
It's advised to save a copy of your maya file before attempting this, as it creates new nodes in the rig logic network and is not undoable. 


## INSTRUCTIONS: 


1. Save all the files in some folder, preferrably the script folder of your maya project.
2. Open the **Combined_MH.py** script in maya. You don't have to touch the others.
3. Copy and paste the location of the said folder into the script. No need to change the forward slash or anything else.
![image](https://user-images.githubusercontent.com/88772846/132264121-a525cc5c-e89f-4a88-be70-74efe3d18be1.png)
3. Copy and paste the name of the newly formed head as shown in the image. Replace "NewHead" with that mesh's name. 
4. Execute the file, and wait for a prompt that says **Proceed now**
5. Now the bones should be aligned to the surface of the new mesh. It's time to rig the new head and transfer bone weights.
6. Select **DHIhead:spine_04** and then the **New mesh** together in the outliner in that order. Go to Skin >> bind skin (options) and make sure you have the settings like this
7.  ![image](https://user-images.githubusercontent.com/88772846/132264992-14f758d7-3061-4cb3-ae5c-24eb1464d548.png)
8.  Now its time to copy skin weights. Select the **original metahuman head** and the **new head** in the outliner in this order, then to go skin >> copy skin weights and make sure the settings looks like this. 
9.  ![image](https://user-images.githubusercontent.com/88772846/132265047-68307310-67fa-44ef-9059-cfc6b9e2ae58.png)
10.  You are now done, play with your new rigged head.

## Optional
If the joints are too big for you to see how they are aligned, you can select DHI:spin_04 from the outliner, and then run the **select joint children.py** script to select all joints in the heirarchy. You can now go to the channel box and change the bone's radius to something like 0.2 instead of the original 1. 

# License
Update 12/06/22: Open for use under MIT license. If you continue to use this, you are bound by this new license agreement.


# FAQ
###  Q. Error: IOError: file <maya console> line 42:
File path error, make sure the files are in the same folder, and the correct path is specified in the script as per tutorial.
  
###  Q. Error: ValueError: file <maya console> line 32: More than one object matches name: spine_05
check DAG  paths for the meshes and bones involved. Also check namespaces.
  
### Q. Error: ValueError: file <maya console> line 125: No object matches name: rigLogicNode.jntTranslationOutputs[0]
Check the tutorial properly and make sure to rename rig logic node
	
### Q. New_Mesh.py line 13: (kInvalidParameter): No element at given index"
Check if the new mesh's name is correctly written in the script and its not part of a group of heirarchy. 
	
