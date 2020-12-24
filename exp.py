import pywinauto
import time
from pywinauto import *
import win32gui
import time
from pywinauto.timings import Timings, WaitUntil, TimeoutError, WaitUntilPasses
import win32process
import win32event
import os
from subprocess import Popen
from pywinauto.timings import always_wait_until_passes
import reg
def findExp():
    find=False
    while not find:
        wins=findwindows.find_windows()
        for win in wins:
            try:
                title=handleprops.text(win)
                print(handleprops.text(win))
                if "库" in title:
                    return win
            except UnicodeEncodeError as e:
                pass
        time.sleep(1)
def findNCSexe():
    wins=findwindows.find_windows()
    for win in wins:
        try:
            title=handleprops.text(win)
            print(handleprops.text(win))
            if "NCS.exe" in title:
                return win
        except UnicodeEncodeError as e:
            pass
    return None
def findPCI():
    wins=findwindows.find_windows()
    for win in wins:
        try:
            title=handleprops.text(win)
            print(handleprops.text(win))
            if "PCI 数据" in title:
                return win
        except UnicodeEncodeError as e:
            pass
    return None

class AccessDeniedError(Exception):
    """Raise when current user is not an administrator."""
    def __init__(self, arg):
        self.args = arg


class NoExistGroupError(Exception):
    """Raise when group Administrators is not exist."""
    def __init__(self, arg):
        self.args = arg


def is_user_an_admin():
    """ Check user admin """
    import os
    if os.name == 'nt':
        try:
            # only windows users with admin privileges can read the C:\windows\temp
            os.listdir(os.sep.join([os.environ.get('SystemRoot', 'C:\\windows'), 'temp']))
        except Exception:
            return False
        else:
            return True
    else:
        return 'SUDO_USER' in os.environ and os.geteuid() == 0

def main():
    if is_user_an_admin():
        os.system(r'start explorer.exe')
        h=findExp()
        if h==None:
            return 
        d=pywinauto.controls.hwndwrapper.DialogWrapper(h)
        d.maximize()
        cs=d.children()
        i=0
        for c in cs:
            if "Address" in c.class_name():
                edit=c
            if "Search" in c.class_name():
                search=c
            print(c.class_name(),":",c.window_text())
            # img=c.CaptureAsImage()
            # if img!=None:
            #     img.save(str(i)+c.class_name()+".png")
            i+=1
        edit.set_focus() 
        edit.click_input()
        isonh=reg.ison()
        if isonh:
            edit.type_keys("C:\\Program{SPACE}Files\\NCS\\ONH3000{ENTER}")
        else:
            edit.type_keys("C:\\Program{SPACE}Files\\NCS\\CS3000{ENTER}")
        search.set_focus()
        #屏幕分辨率=1366*768
        time.sleep(1)
        d.click_input(button='right', pressed='', coords=(217,472), double=False, absolute=False)
        time.sleep(1)
        #属性
        d.click_input(button='left', pressed='', coords=(217+20,472-20), double=False, absolute=False)
        time.sleep(1)
        h=findNCSexe()
        d2=pywinauto.controls.hwndwrapper.DialogWrapper(h)
        #兼容
        d2.click_input(button='left', pressed='', coords=(89,47), double=False, absolute=False)
        time.sleep(1)
        #管理员身份
        d2.click_input(button='left', pressed='', coords=(52,368), double=False, absolute=False)
        time.sleep(1)
        #确定
        d2.click_input(button='left', pressed='', coords=(167,455), double=False, absolute=False)
        time.sleep(1)
        #open ncs.exe
        d.click_input(button='left', pressed='', coords=(217,472), double=True, absolute=False)
    else:
        print('\nYou are not an administrator')
if __name__=="__main__":        
    main()