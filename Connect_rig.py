from maya import cmds
import pymel.core as pm

cmds.createEmbeddedNodeRL4(
n="rigLogicNode", 
dfp="C:\Users\Rev Oconner\Desktop\Zoe01\Maya\Journalist\scripts\Kristofer_rl.dna",
jn="DHIhead:<objName>.<attrName>", 
amn="FRM_WMmultipliers.<objName>_<attrName>", 
bsn="<objName>_blendShapes.<attrName>", 
cn="<objName>.<attrName>"
)