"""
app应用相关
"""

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'common'))
print(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'common'))
import subprocess
import logfile as logfile
import time
import uiautomator2 as u2
from phone import PhoneInfo




'''
安装apk
'''
class App:
    def __init__(self) -> None:
        #实例化log对象
        logFile = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs/applog.log')
        self.log = logfile.Logger('applog', logFile)

        device = PhoneInfo()
        d = u2.connect(device.getMechine)

    #安装app
    def appInstall(self, appPath=None):
        cfgPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #添加configs文件夹为系统路径
        sys.path.append(cfgPath) 
        from configs import config
        if appPath == 'default' or appPath is None:
            appPath = config.AppPath
        print (appPath)
        cmdInstallApp = "adb install -t " + appPath
        re, error = subprocess.Popen(cmdInstallApp, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        # print(cmdInstallApp)
        print(re.decode('utf-8'))
        print(error.decode('utf-8'))

        #日志记录安装结果
        if "Success" in error.decode():
            self.log.log("apk install success!")
            return True
        else:
            self.log.log("apk install faild, reason is： " + error.decode('utf-8'))
            return False
    
    #卸载app
    def uninstallApp(self, packageName):
        check0, error = subprocess.Popen("adb uninstall --user 0 " + packageName, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate() 
        isIns = check0.decode('utf-8')
        print(isIns)
        if 'not installed' in isIns:
            print("应用未安装")
            self.log.log("应用未安装")
        else:        
            check1, error = subprocess.Popen("adb shell pm list packages -f " + packageName, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

            # print(type(check1.decode('utf-8')))
            if check1.decode('utf-8') == '':
                print("卸载成功")
                self.log.log("卸载成功")
            else:
                print("卸载失败")
                self.log.log("卸载失败")
            
            # cmdUninstall = "adb uninstall --user 0 " + packageName
            # re = subprocess.Popen(cmdUninstall, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 

        
    
    #打开应用activity界面
    def startActivity(self, activity='default'):
        cfgPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        if activity == None or activity == 'default':
            #添加configs文件夹为系统路径
            sys.path.append(cfgPath) 
            from configs import config
            self.activity = config.TestAppActivity
            #移除添加的系统路径
            sys.path.remove(cfgPath)
        else: 
            self.activity = activity
        self.log.log('the activity is opened is: ' + self.activity)

        cmdStartAty = "adb shell am start -n "+ self.activity

        re, error = subprocess.Popen(cmdStartAty, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        print(re.decode('utf-8') + error.decode('utf-8'))
        self.log.log('result of open activity is: ' + (re.decode('utf-8') +' errormsg is：'+ error.decode('utf-8')))

        

    #获取当前界面 uiautomator2 current
    def getCurrentActivity(self):
        cfgPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #添加configs文件夹为系统路径    

        cmdStartAty = "adb shell dumpsys activity activities | findstr mResumedActivity"
        result = subprocess.Popen(cmdStartAty, shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE).stdout.readlines()
        
        activity = result[0].decode().split()[-2]
        return activity
    
    #启动应用    
    def openApp(self, packageName):
        self.packageName = packageName
        d.app_start(self.packageName)

    #关闭应用    
    def openApp(self, packageName):
        self.packageName = packageName
        d.app_stop(self.packageName)





if __name__ == "__main__":
    app = App()
    device = PhoneInfo()
    # app.appInstall()
    # time.sleep(5)
    # app.uninstallApp("com.xunmeng.pinduoduo")
    # app.startActivity('com.tencent.mm/.ui.LauncherUI')
    print(device.getMechine())
    d = u2.connect(device.getMechine())
    # d.app_start('com.tencent.mm')
    d.app_stop('com.tencent.mm')


