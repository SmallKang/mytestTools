import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'common'))
from adb import ADB
from logfile import Logger



class homepage:

    def __init__(self):
        self.adb = ADB()
        self.log = Logger('')

