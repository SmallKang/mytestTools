"""
手机信息相关
"""

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'common'))
import subprocess
# from ..common.logfile import Logger as Log
from logfile import Logger
# from .. import common.logfile.Logger as Log

class PhoneInfo():
    def __init__(self) -> None:
        #实例化log对象
        logFile = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs/applog.log')
        self.Log = Logger('phone.log', logFile)

        # self.apkPath = apkPath
        

    def getMechine(self):
        cmdGetMechineInfo = "adb devices"

        # 机器编码
        deviceinfo = subprocess.Popen(cmdGetMechineInfo, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        device = deviceinfo[1].decode().split()[0]
        self.Log.log('mechine num is ' + device)
        return str(device)

    # 获取手机信息：型号、版本、品牌、设备名
    def getPhoneInfo(self, device):
        l_list = {}
        # cmd = "adb -s " + device + " shell cat /system/build.prop"
        cmdVersion = "adb -s " + device + " shell getprop  ro.build.version.release"
        cmdModel = "adb -s " + device + " shell getprop  ro.product.model"
        cmdBrand = "adb -s " + device + " shell getprop  ro.product.brand"
        cmdDevice = "adb -s " + device + " shell getprop  ro.product.device"

        # 版本
        release = subprocess.Popen(cmdVersion, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        # 型号
        model = subprocess.Popen(cmdModel, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        # 品牌
        brand = subprocess.Popen(cmdBrand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        # 设备名
        device = subprocess.Popen(cmdDevice, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        
        l_list["release"] = release[0].decode()
        l_list["model"] = model[0].decode()
        l_list["brand"] = brand[0].decode()
        l_list["device"] = device[0].decode()

        self.Log.log('device info is ' + l_list)

        return l_list

    # 获取手机分辨率, 返回 x, y
    def get_pix(self, devices):
        result = os.popen("adb -s " + devices + " shell wm size", "r")
        x, y =result.readline().split("Physical size:")[1].strip().split('x')
        return int(x), int(y)

if __name__ == "__main__":
    device = PhoneInfo()
    # print(device.getPhoneInfo(getMechine()))
    x, y = device.get_pix(device.getMechine())
    # print(size) #分辨率
    print(x/2, y/2)
    # print(device.getPhoneInfo(getMechine())['release'])
    