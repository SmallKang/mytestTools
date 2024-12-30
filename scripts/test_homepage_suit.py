import sys, os
import pytest
from pathlib import Path
s1 = os.path.join(Path(__file__).parent.parent, 'aw')
sys.path.append(s1)
sys.path.append(os.path.join(Path(__file__).parent.parent, 'pages/weixin'))
from phone import PhoneInfo
from app import App
from logfile import Logger
import time
from home import Home
import allure




logpath = os.path.join(Path(__file__).parent.parent, 'logs/cases.log')
log = Logger('cases', logpath)
devidce = PhoneInfo()
home = Home()
app = App()


class TestHomePage:  

    #脚本执行前
    def setup_method(self):
        log.log(os.path.basename(__file__) + ' is running started now')
        app.openApp('com.tencent.mm')

    #脚本执行结束
    def teardown_method(self):
        app.closeApp('com.tencent.mm')
        

    
    @allure.title("给微信联系人发送消息")
    def test_sendmsg001(self):
        with allure.step("点击联系人，进入聊天页面"):
            home.btnClickByText("小木匠")
            time.sleep(1)
        
        
        home.btnClickByClass("android.widget.ScrollView")
        time.sleep(1)
        home.sendMsgByClass("android.widget.EditText", msg='发送消息的case')
        time.sleep(1)
        home.btnClickByText('发送')
        assert 1==1
    
    @allure.title("给微信文件传输助手发送当前时间")
    def test_sendtime001(self):
        with allure.step("点击联系人，进入聊天页面"):
            home.btnClickByText("文件传输助手")
            time.sleep(1)
        
        
        home.btnClickByClass("android.widget.ScrollView")
        time.sleep(1)
        home.sendMsgByClass("android.widget.EditText", msg=str(time.asctime().format('yy-mm-dd hh-mm-ss')))
        time.sleep(1)
        home.btnClickByText('发送')
        assert 1==1
    
    @pytest.mark.skip(reason="测试skip")
    def test_skip(self):
        assert True





if __name__ == '__main__':
    # pytest.main("-s test_homepage_suit.py") 
    # pytest.main()
    pytest.main(["-s", "scripts", "--alluredir=reports"])
    os.system("allure serve reports")
    