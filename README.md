# Metahuman Rig Transfer Script (deprecated)
## IMPORTANT NOTE: With the ability to edit DNA files directly in Maya, after the UE5.6 update, this plugin will not get any more updates, as it has been rendered obsolete with the new official pipelines. It works with UE5.4 as of the latest update, future updates of metahuman will not be supported. I will continue to make new projects based on problems I face in my work, and those will always be publicly available free of charge. Thank you all for the massive support and interest in this little project of mine that was my first real experience learning coding. 
### For official way of modifying the rig, please take a look at https://dev.epicgames.com/documentation/en-us/metahuman/expression-editor 
Python script to modify the metahuman rig into a new one for Maya. For unreal use Mesh to Metahuman or houdini.

Link to youtube video demo - https://www.youtube.com/watch?v=qF-z1aZQUYE (Outdated)

<img width="410" alt="image" src="https://github.com/user-attachments/assets/51ef1a70-d0f0-49a3-bab9-6279b4d2dfa9">

## Table of Content
1. [Prerequisite](https://github.com/revoconner/metahuman_rig_transfer#prerequisite)
2. [Instruction](https://github.com/revoconner/metahuman_rig_transfer#instructions)
3. [Optional Instruction](https://github.com/revoconner/metahuman_rig_transfer#optional)
4. [License](https://github.com/revoconner/metahuman_rig_transfer#license)
5. [FAQ](https://github.com/revoconner/metahuman_rig_transfer#FAQ)

## PREREQUISITE:
(written in Python 3)
#### Will not work in Maya 2020 and below.
1. The new head to which the bones are to be rigged must share the same UV and topology as the original metahuman head. A program like Wrap3D will help with it. 
2. Select the original metahuman head mesh and go to Channel box and paste the rl4Embedded... into the text box.
<img width="400" alt="image" src="https://github.com/user-attachments/assets/eff75e46-011d-4afe-90d2-b810ccc72f43">


### Good Practices
It's advised to save a copy of your maya file before attempting this, as it creates new nodes in the rig logic network and is not undoable. 


## INSTRUCTIONS: 


1. Run the script.
2. Select the original Metahuman Head and press the **OG mesh** button on the UI
3. Select the wrapped new head mesh and press the **W mesh** button on the UI. Make sure the Head is not in a group or heirarchy, and its transforms have been frozen.
4. Execute the file, and wait for a prompt that says **MetaHumanTransfer completed successfully.**
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
  
###  Q. Error: ValueError: file <maya console> line 32: More than one object matches name: spine_05
check DAG  paths for the meshes and bones involved. Also check namespaces.  
	
### Q. kInvalidParameter: No element at given index"
Check if the new mesh's name is correctly written in the UI and its not part of a group of heirarchy. 
	
## Recently updated by cemccabe77 in the community. Big thanks! 
## Compatible with UE 5.4 Metahumans
