"""
配置相关
"""
import sys, os

testversion=''

RootPath =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(RootPath)
AppPath = os.path.join(RootPath, 'files/apks/pinduoduo.apk')
print('AppPath is '+ AppPath)
TestAppActivity = r"com.lbe.security.miui/com.android.packageinstaller.permission.ui.GrantPermissionsActivity"

Test_mechine_type = "Android"