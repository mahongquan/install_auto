from __future__ import print_function
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def admin_code():

if is_admin():
    # 将要运行的代码加到这里
    admin_code()
else:
    if sys.version_info[0] == 3:
    	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    	admin_code()