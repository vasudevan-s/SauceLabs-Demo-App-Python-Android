from configparser import ConfigParser

import os

#
# Created By: Vasudevan Sampath
#
#  Common.py is a generalised class with utility methods

class Common:

    def __init__(self):
        global config
        os.chdir("..")
        config = ConfigParser()
        config.read(os.getcwd() + '/config/deviceconfig.ini')

    def read_device_config(self, category, key):
        return config.get(category, key)


