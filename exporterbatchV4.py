import maya.cmds as cmds
import maya.mel as mel
import sys

if(cmds.window('uiWindow', q=1, ex=1)):
	cmds.deleteUI('uiWindow')

def startExport(path):
	objectSelection = cmds.ls(sl=1,fl=1)
	filePathStr = cmds.textFieldButtonGrp('Dir', query = True, text = True)
	for item in objectSelection:
		itemRename = item
		itemRename = itemRename.replace('|','_')
		itemRename = itemRename.split(':', 1)[0]
		#itemRename = itemRename[:5]
		itemRename = itemRename + "_UV"
		finalExportPath = "%s/%s.obj"%(filePathStr, itemRename)
		cmds.select(item)
		mel.eval('file -force -options "groups=0;ptgroups=0;materials=0;smoothing=1;normals=1" -typ "OBJexport" -pr -es "%s";'%(finalExportPath))
		print "Exported: %s"%(finalExportPath)
	sys.stdout.write('Exporting Complete!\n')

def dirPath(filePath, fileType):
	cmds.textFieldButtonGrp('Dir', edit=True, text=str(filePath))
	return 1

def browsePath():
	cmds.fileBrowserDialog(m=4, fc=dirPath, ft='directory', an='Choose Directory')
	return

def createUI():
	uiWindow = cmds.window('uiWindow', title="Super Cool Batch OBJ Exporter", iconName='uiWindow', widthHeight=(300,150))
	cmds.columnLayout('uiColWrapper', w = 375, adjustableColumn=False)
	cmds.textFieldButtonGrp('Dir', label='Directory Path: ', cw3 = [100,190,50], buttonLabel='Browse', buttonCommand=browsePath)
	cmds.button('startExport', label = "Export Selected!", width = 400, command = startExport)
	cmds.showWindow(uiWindow)

createUI()