import os, sys
import subprocess
from logfile  import Logger
from pathlib import Path
import time


class ADB:
    def __init__(self):
        logpath = os.path.join(Path(__file__).parent.parent, 'logs/adb.log')
        self.log = Logger('adb', logpath)


    def runShell(self, shellCmd):
        execCmd = 'adb shell '+ shellCmd
        re, msg = subprocess.Popen(execCmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.log.log('run adb commad: '+ execCmd + ' and re&msg is ' + re + msg)
        return (re, msg)


    def runCmd(self, cmd):
        re = subprocess.run(cmd, capture_output=True, text=True)
        self.log.log('run commad: '+ cmd + ' and re&msg is ' + str(re))
        return re


    """
        :param filePath: 本地路径， 默认为resource下
        :param targetPath: 手机目录
    """
    def pullFile(self, filePath, targetPath):
        cmd = 'adb pull ' + targetPath + ' ' + filePath
        re, msg = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.log.log('run commad: '+ cmd + ' and re&msg is ' + re + msg)



# if __name__ == '__main__':
    # adb = ADB()
    # print(adb.runCmd('adb devices'))

