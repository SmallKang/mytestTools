"""
app应用相关
"""

import os, sys
import subprocess
import logfile

#实例化log对象
logFile = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs/applog.log')
log = logfile.Logger('applog', logFile)


'''
安装apk
'''
def appInstall(appPath):
    cfgPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #添加configs文件夹为系统路径
    sys.path.append(cfgPath) 
    from configs import config
    if appPath == 'default':
        appPath = config.appPath
    print (appPath)
    cmdInstallApp = "adb install -t " + appPath
    re = subprocess.Popen(cmdInstallApp, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()

    #移除添加的系统路径
    sys.path.remove(cfgPath)

    #日志记录安装结果
    if "Success" in re[1].decode():
        log.log("apk install success!")
        return True
    else:
        log.log("apk install faild, reason is " + re[1].decode() + "!")
        return False
    



if __name__ == "__main__":
    appInstall('default')