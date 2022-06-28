import configparser
import os

software_version = 1.0
default_secured_directory = 'secured_dir'

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