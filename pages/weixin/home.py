import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'aw'))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'common'))
print(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'aw'))
import uiautomator2 as ui2
from phone import PhoneInfo
import logfile as logfile


class Home:

    def __init__(self):
        self.phone = PhoneInfo()
        self.d = ui2.connect(self.phone.getMechine())
        print(self.phone.getMechine())


        self.btn_Add = '//*[@resource-id="com.tencent.mm:id/plus_icon"]'
        self.firstLine = '//*[@resource-id="com.tencent.mm:id/kbq"]'

    

    def addClick(self):
        # driver.findByXpath(self.btn_Add).click()
        self.d(text='小木匠').click()
        pass
        

if __name__=='__main__':
    h = Home()
    h.addClick()