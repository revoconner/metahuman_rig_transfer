# metahuman_rig_transfer
A series of python scripts to modify the metahuman rig into a new one for Maya.

Link to youtube video demo - https://www.youtube.com/watch?v=qF-z1aZQUYE

##PREREQUISITE:
1. The new head to which the bones are to be rigged must share the same UV and topology as the original metahuman head. A program like R3DS Wrap will help with it. 
2. The file you download from Metahuman will have its embeddedNodeRL4 node named after the DNA_RL file, something like Kristopher_rl or rl4Embedded_Kristofer_rl, if the name of the metahuman was Kristopher. Change that to rigLogicNode
![image](https://user-images.githubusercontent.com/88772846/132264485-74e9d98e-38d9-4227-ab56-1ca9fc5effd5.png)

![image](https://user-images.githubusercontent.com/88772846/132264420-1128a2eb-d1f0-4ec2-bbdc-ea97e150c197.png)


##INSTRUCTIONS: 

(written in Py 2.7)

1. Save all the files in some folder, preferrably the script folder of your maya project.
2. Open the Combined_MH.py script in maya. You don't have to touch the others.
3. Copy and paste the location of the said folder into the script. No need to change the forward slash or anything else.
![image](https://user-images.githubusercontent.com/88772846/132264121-a525cc5c-e89f-4a88-be70-74efe3d18be1.png)
3. Copy and paste the name of the newly formed head as shown in the image. Replace "NewHead" with that mesh's name. 
4. 

