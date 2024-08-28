"""
手机信息相关
"""

import os
import subprocess

class ApkInfo():
    def __init__(self, apkPath) -> None:
        self.apkPath = apkPath

    def getMechine(self):
        cmdGetMechineInfo = "adb devices"

        # 机器编码
        deviceinfo = subprocess.Popen(cmdGetMechineInfo, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        device = deviceinfo[1].decode().split()[0]
        return device

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

        return l_list

    # 获取手机分辨率
    def get_pix(self, devices):
        result = os.popen("adb -s " + devices + " shell wm size", "r")
        return result.readline().split("Physical size:")[1]

if __name__ == "__main__":
    device = ApkInfo()
    print(device.getPhoneInfo(getMechine()))
    print(device.get_pix(getMechine())) #分辨率
    print(device.getPhoneInfo(getMechine())['release'])
    