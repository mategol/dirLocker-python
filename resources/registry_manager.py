import winreg
import sys
from lang import *
from configuration_manager import *

def registry_append():
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, 'dirLocker', 0, winreg.REG_SZ, sys.argv[0])
    winreg.CloseKey(registry_key)

def set_registry():
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\*\\shell\\dirLocker')
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\*\\shell\\dirLocker', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, 'MUIVerb', 0, winreg.REG_SZ, 'dirLocker')
    winreg.SetValueEx(registry_key, 'subcommands', 0, winreg.REG_SZ, None)
    winreg.SetValueEx(registry_key, 'Icon', 0, winreg.REG_SZ, sys.argv[0])
    winreg.CloseKey(registry_key)


    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\*\\shell\\dirLocker\\shell')
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\*\\shell\\dirLocker\\shell', 0, winreg.KEY_WRITE)
    winreg.CloseKey(registry_key)



    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\*\\shell\\dirLocker\\shell\\delete')
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\*\\shell\\dirLocker\\shell\\delete', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, None, 0, winreg.REG_SZ, get_text('rightclick-delete', get_locale()))
    #winreg.SetValueEx(registry_key, 'Icon', 0, winreg.REG_SZ, sys.argv[0])
    winreg.CloseKey(registry_key)

    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\*\\shell\\dirLocker\\shell\\delete\\command')
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\*\\shell\\dirLocker\\shell\\delete\\command', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, None, 0, winreg.REG_SZ, sys.argv[0] + ' %1 delete')
    winreg.CloseKey(registry_key)


    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\*\\shell\\dirLocker\\shell\\move')
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\*\\shell\\dirLocker\\shell\\move', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, None, 0, winreg.REG_SZ, get_text('rightclick-move', get_locale()))
    #winreg.SetValueEx(registry_key, 'Icon', 0, winreg.REG_SZ, sys.argv[0])
    winreg.CloseKey(registry_key)

    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\*\\shell\\dirLocker\\shell\\move\\command')
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\*\\shell\\dirLocker\\shell\\move\\command', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, None, 0, winreg.REG_SZ, sys.argv[0] + ' %1 move')
    winreg.CloseKey(registry_key)



    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\Directory\\shell\\dirLocker')
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\Directory\\shell\\dirLocker', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, 'MUIVerb', 0, winreg.REG_SZ, 'dirLocker')
    winreg.SetValueEx(registry_key, 'subcommands', 0, winreg.REG_SZ, None)
    winreg.SetValueEx(registry_key, 'Icon', 0, winreg.REG_SZ, sys.argv[0])
    winreg.CloseKey(registry_key)


    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\Directory\\shell\\dirLocker\\shell')
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\Directory\\shell\\dirLocker\\shell', 0, winreg.KEY_WRITE)
    winreg.CloseKey(registry_key)



    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\Directory\\shell\\dirLocker\\shell\\delete')
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\Directory\\shell\\dirLocker\\shell\\delete', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, None, 0, winreg.REG_SZ, get_text('rightclick-delete', get_locale()))
    #winreg.SetValueEx(registry_key, 'Icon', 0, winreg.REG_SZ, sys.argv[0])
    winreg.CloseKey(registry_key)

    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\Directory\\shell\\dirLocker\\shell\\delete\\command')
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\Directory\\shell\\dirLocker\\shell\\delete\\command', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, None, 0, winreg.REG_SZ, sys.argv[0] + ' %1 delete')
    winreg.CloseKey(registry_key)


    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\Directory\\shell\\dirLocker\\shell\\move')
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\Directory\\shell\\dirLocker\\shell\\move', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, None, 0, winreg.REG_SZ, get_text('rightclick-move', get_locale()))
    #winreg.SetValueEx(registry_key, 'Icon', 0, winreg.REG_SZ, sys.argv[0])
    winreg.CloseKey(registry_key)

    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\Directory\\shell\\dirLocker\\shell\\move\\command')
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Classes\\Directory\\shell\\dirLocker\\shell\\move\\command', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, None, 0, winreg.REG_SZ, sys.argv[0] + ' %1 move')
    winreg.CloseKey(registry_key)