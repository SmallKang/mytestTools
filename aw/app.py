"""
app应用相关
"""

import os, sys
import subprocess
import logfile
import time

#实例化log对象
logFile = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs/applog.log')
log = logfile.Logger('applog', logFile)


'''
安装apk
'''
class App:
    def __init__(self) -> None:
        pass

    #安装app
    def appInstall(self, appPath):
        cfgPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #添加configs文件夹为系统路径
        sys.path.append(cfgPath) 
        from configs import config
        if appPath == 'default':
            appPath = config.AppPath
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
    
    #卸载app
    def uninstallApp(self, packageName):
        check0 = subprocess.Popen("adb shell pm list packages -f " + packageName, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        print(check0)

        # cmdUninstall = "adb uninstall --user 0 " + packageName
        # re = subprocess.Popen(cmdUninstall, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        
        check1 = subprocess.Popen("adb shell pm list packages -f " + packageName, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        print(check1)
        if check1 == None:
            print("卸载成功")
        else:
            print("卸载失败")

        
    
    #启动app    
    def startActivity(self):
        cfgPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #添加configs文件夹为系统路径
        sys.path.append(cfgPath) 
        from configs import config
        activity = config.TestAppActivity

        cmdStartAty = "adb shell am start -n "+ activity

        re = subprocess.Popen(cmdStartAty, shell=True)

        #移除添加的系统路径
        sys.path.remove(cfgPath)

    #获取当前界面
    def getCurrentActivity(self):
        cfgPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #添加configs文件夹为系统路径

        cmdStartAty = "adb shell dumpsys activity activities | findstr mResumedActivity"
        result = subprocess.Popen(cmdStartAty, shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE).stdout.readlines()
        
        activity = result[0].decode().split()[-2]
        return activity





    



if __name__ == "__main__":
    app = App()
    app.appInstall('default')
    # time.sleep(5)
    # app.uninstallApp("com.xunmeng.pinduoduo")


