from win32com.client import Dispatch

def create_shortcut(path, target='', wDir='', icon=''):    
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target[0]
    shortcut.Arguments = target[1]
    shortcut.WorkingDirectory = wDir
    if icon != '':
        shortcut.IconLocation = icon
    shortcut.save()