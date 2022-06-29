from win32com.client import Dispatch
import os

def create_shortcut(path, target='', wDir='', icon=''):    
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target[0]
    shortcut.Arguments = target[1]
    shortcut.WorkingDirectory = wDir
    if icon != '':
        shortcut.IconLocation = icon
    shortcut.save()

def secure_delete(path, passes=1):
    length = os.path.getsize(path)
    with open(path, "br+", buffering=-1) as f:
        for i in range(passes):
            f.seek(0)
            f.write(os.urandom(length))
        f.close()
    os.remove(path)