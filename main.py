import os
import shutil
import getpass
import sys
from resources.registry_manager import *
from resources.configuration_manager import *
from resources.file_manager import *

software_version = 1.0
software_directory = 'C:\\Program Files\\dirLocker'
default_secured_directory = 'secured_dir'

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