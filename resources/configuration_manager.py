import configparser
import time
import os
import threading

def get_secured_directory():
    global configuration
    return configuration['CONFIGURATION']['secured_directory']

def get_locale():
    global configuration
    return configuration['CONFIGURATION']['locale']

def update_configuration():
    global locale, secured_directory, configuration
    while True:
        configuration = configparser.ConfigParser()
        if 'configuration.ini' not in os.listdir('.'):
            configuration['CONFIGURATION'] = {'secured_directory': default_secured_directory,
                                              'locale': 'en'}
            with open('configuration.ini', 'w') as configuration_file:
                configuration.write(configuration_file)
        else:
            configuration.read('configuration.ini')
            locale = configuration['CONFIGURATION']['locale']
            secured_directory = configuration['CONFIGURATION']['secured_directory']
        time.sleep(10)

def configuration_initialize(default_directory):
    global default_secured_directory, configuration
    default_secured_directory = default_directory
    threading.Thread(target=update_configuration).start()