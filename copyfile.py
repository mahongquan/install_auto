# -*- coding: utf-8 -*-
import os
import getpath
destdrive="C:"
bakdrive="C:"
print("copy")
def main(ison):
	#copyto("c:",ison)	
	#copyto("f:",ison)	
	copyto(bakdrive,ison)
	if destdrive!="C:":#only c
		if os.path.splitdrive(getpath.getpath())[0]=="H:":
			copyto("g:",ison)	
		else:
			copyto("h:",ison)	
	else:
		if os.path.splitdrive(getpath.getpath())[0]=="E:":
			copyto("F:",ison)	
		else:
			copyto("E:",ison)	
def copyto(dest,ison):
	# if ison:
	# 	todir='%s\\ONH3000V2.1.31\\' % dest
	# 	if os.path.exists(todir):
	# 		return
	# else:
	# 	todir='%s\\CS3000v1.6.19\\' % dest
	# 	if os.path.exists(todir):
	# 		return
	curpath=getpath.getpath()
	if ison:
		#copy 9111
		cmd="xcopy /s %s\\..\\..\\刻盘\\9111 %s\\9111\\" % (curpath,dest)
		print(cmd)
		if os.path.exists(dest+"\\9111"):
			pass
		else:
			os.system(cmd)
		#
		cmd='xcopy /s "%s\\..\\..\\刻盘\\ONH3000v2.1.33" %s\\ONH3000v2.1.33\\' % (curpath,dest)
		print(cmd)
		if os.path.exists(dest+"\\ONH3000v2.1.33"):
			pass
		else:
			os.system(cmd)
	else:
		cmd='xcopy /s "%s\\..\\..\\刻盘\\CS3000备份" %s\\CS3000备份\\' % (curpath,dest)
		print(cmd)
		if os.path.exists(dest+"\\CS3000备份"):
			pass
		else:
			os.system(cmd)
if __name__=="__main__":
	import reg
	ison=reg.ison()
	main(ison)

