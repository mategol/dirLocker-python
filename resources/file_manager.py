from win32com.client import Dispatch
import os
from resources.configuration_manager import *

def generate_name(input_name, is_directory):
    extension = input_name.split('.')[-1]
    file_name = input_name.split('.')[:-1]

    if is_directory:
        additional_extension = '.directory'
    else:
        additional_extension = ''

    list_of_encryption_directory = os.listdir(get_secured_directory())
    if input_name + additional_extension + '.dlock' in list_of_encryption_directory:
        loop_number = 0
        while True:
            loop_number += 1
            if file_name + '_' + str(loop_number) + extension + additional_extension + '.dlock' not in list_of_encryption_directory:
                return file_name + '_' + str(loop_number) + extension + additional_extension
            else:
                continue
    else:
        return input_name + additional_extension

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