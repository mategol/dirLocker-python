import os
import shutil
import getpass
import sys
import time
import psutil
import pyautogui
from resources.registry_manager import *
from resources.configuration_manager import *
from resources.file_manager import *
from resources.gui import *
from resources.encryption import *

software_version = 1.0
software_directory = 'C:\\Users\\' + getpass.getuser() + '\\dirLocker'
default_secured_directory = 'secured_dir'
encryption_key = 'zaq1@WSX'     # Change here

'''if sys.argv[0] != (software_directory + '\\' + sys.argv[0].split('\\')[-1]):
    try:
        shutil.copyfile(sys.argv[0], software_directory + '\\' + sys.argv[0].split('\\')[-1])
        os.system('start ' + software_directory + '\\' + sys.argv[0].split('\\')[-1])
        sys.exit(0)
    except:
        try:
            os.mkdir(software_directory)
            shutil.copyfile(sys.argv[0], software_directory + '\\' + sys.argv[0].split('\\')[-1])
            os.system('start ' + software_directory + '\\' + sys.argv[0].split('\\')[-1])
            sys.exit(0)
        except Exception as err:
            print(err)
            sys.exit(0)'''

configuration_initialize(software_directory + '\\' + default_secured_directory)
time.sleep(1)

if not os.path.exists('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs'):
    create_shortcut('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\dirLocker.lnk', [sys.argv[0], 'gui'])

registry_append()
set_registry()

if len(sys.argv) == 1:
    process_check = False
    for process in psutil.process_iter():
        if process.name() == sys.argv[0].split('\\')[-1]:
            if not process_check:
                process_check = True
            else:
                sys.exit(0)
    while True:
        time.sleep(3)
        for element in os.listdir(get_secured_directory()):
            if element[-6:] != '.dlock' and os.path.isfile(get_secured_directory() + '\\' + element):
                try:
                    filename = generate_name(element, False)
                    encrypt_file(get_secured_directory() + '\\' + element, get_secured_directory() + '\\' + filename + '.dlock', encryption_key)
                    secure_delete(get_secured_directory() + '\\' + element, 5)
                    break
                except Exception as error:
                    pyautogui.alert(error, 'Error occurred!')
                    pass
            elif os.path.isdir(get_secured_directory() + '\\' + element):
                zip(get_secured_directory() + '\\' + element, get_secured_directory() + '\\' + element + '.directory')
                shutil.rmtree(get_secured_directory() + '\\' + element)

elif len(sys.argv) == 2:
    if sys.argv[1] == 'gui':
        launch_gui()
    else:
        open_file(sys.argv[1], encryption_key)

elif len(sys.argv) == 3:
    if sys.argv[2] == 'delete':
        if os.path.isfile(sys.argv[1]):
            secure_delete(sys.argv[1], 5)
        else:
            shutil.rmtree(sys.argv[1])

    elif sys.argv[2] == 'move':
        if os.path.isfile(sys.argv[1]):
            shutil.copy2(sys.argv[1], secured_directory)
            secure_delete(sys.argv[1], 5)
        else:
            shutil.copytree(sys.argv[1], secured_directory)