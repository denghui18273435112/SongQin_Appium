from appium  import  webdriver
import time,traceback

# 今日头条的登录

desired_caps = {}  # 创建字典，存储自动化参数
desired_caps["platformName"] = "Android"  # 运行平台 android还是ios
desired_caps["platformVersion"] = "6"   #  设备系统的的版本，模拟器中查看
desired_caps["deviceName"] = "test"     # 固定的
#desired_caps["app"] = r"E:\teacher.apk"   #当虚拟器中没有安装apk时，系统会在指定路径去找apk并安装
desired_caps["appPackage"] = "com.jufa.mt.client"   # app的包名(唯一)
desired_caps["appActivity"] ="com.jufa.mt.client.ui.LogoActivity"   #应用某一个操作界面
desired_caps["unicodeKeyboard"] = True  # 编码集  模拟器中安装一个输入法
desired_caps["resetKeyboard"] = True
desired_caps["noReset"] = True  #  # 固定
desired_caps["newCommandTimeout"] = 6000
# desired_caps["automationName"] = "uiautomator2"

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  #  地址是固定；启动Remote RPC

try:
    driver.implicitly_wait(10)

    # 根据id元素找到，并点击 id 和html元素的id不同
    driver.find_element_by_id("io.manonog.developerdaily:id/tab_bar_plus").click()
    time.sleep(1)
    driver.find_element_by_id("io.manonog.developerdaily:id/btn_email").click()
    time.sleep(1)

    # 输入用户名和账号
    ele = driver.find_element_by_id("io.manonog.developerdaily:id/edt_email")
    ele.send_keys("jcyrss@163.com")
    ele = driver.find_element_by_id("io.manonog.developerdaily:id/edt_password")
    ele.send_keys("sdfsdf")

    time.sleep(2)
    # 点击登录
    driver.find_element_by_id("io.manonog.developerdaily:id/btn_login").click()

except:
    print(traceback.format_exc())