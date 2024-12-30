import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'aw'))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'common'))
print(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'aw'))
import uiautomator2 as ui2
from pathlib import Path
from phone import PhoneInfo
from logfile import Logger
from adb import ADB
import time


class Home:

    def __init__(self):
        self.phone = PhoneInfo()
        self.d = ui2.connect(self.phone.getMechine())
        self.log = Logger('case', os.path.join(Path(__file__).parent.parent.parent, 'logs/cases.log'))


        self.btn_Add = '//*[@resource-id="com.tencent.mm:id/plus_icon"]'
        self.firstLine = '//*[@resource-id="com.tencent.mm:id/kbq"]'

    

    def itemClickByText(self, Text):
        # driver.findByXpath(self.btn_Add).click()
        self.d(text=Text).click()
        
        time.sleep(1)
    
    def sendMsgByClass(self, clsname, msg):
        self.d(className=clsname).clear_text()
        print("清楚文本")
        time.sleep(5)
        self.d(className=clsname).send_keys(msg)
        print("输入文本")
        # self.d(Xpath=xpath).clear_text()
        # self.d(Xpath=xpath).send_keys(msg)
        time.sleep(1)
    
    def btnClickByClass(self, clsname):
        self.d(className = clsname).click()
        time.sleep(1)

    def btnClickByText(self, text):
        self.d(text=text).click()
        print("点击小木匠")
        time.sleep(1)

    
    

        

# if __name__=='__main__':
#     h = Home()
#     h.addClick()