from win32com.client import Dispatch
import os
from tkinter import Tk, filedialog
import zipfile
from resources.configuration_manager import *
from resources.encryption import *


def open_file(target_file, encryption_key):
    if os.path.isfile(target_file) and target_file[:-6] == '.dlock':
        path_to_paste = get_manual_path()
        if path_to_paste != '':
            filename = target_file.split('\\')[-1]
            decrypt_file(target_file, path_to_paste + '\\' + filename[:-6], encryption_key)
            secure_delete(target_file, 1)
            if target_file.split('.')[-2] == 'directory':
                unzip(path_to_paste + '\\' + filename, path_to_paste)
                secure_delete(path_to_paste + '\\' + filename)

def get_manual_path():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    open_dir = filedialog.askdirectory()
    root.destroy()
    return open_dir

def generate_name(input_name, is_directory):
    extension = input_name.split('.')[-1]
    file_name = '.'.join(input_name.split('.')[:-1])

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
                return file_name + '_' + str(loop_number) + '.' + extension + additional_extension
            else:
                continue
    else:
        return input_name + additional_extension

def unzip(path_to_zip_file, directory_to_extract_to):
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

def zip(source_dir, output_filename):
    relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(source_dir):
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename):
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)

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