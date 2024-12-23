from uiautomator2 import Device

class Home():

    def __init__(self):
        self.dricer = Device.driver
        self.btn_Add = '//*[@resource-id="com.tencent.mm:id/plus_icon"]'
        self.firstLine = '//*[@resource-id="com.tencent.mm:id/kbq"]'

    

    def addClick(self. btn):
        self.btn = self.btn_Add
        

