import ctypes, sys
from getpath import getpath
from main2 import main
initpath=getpath()
sys.path.insert(0,initpath+"\Lib")
print(sys.path)
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    # 将要运行的代码加到这里
    main()
else:
    if sys.version_info[0] == 3:
    	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    	main()
