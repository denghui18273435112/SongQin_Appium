from appium  import  webdriver
import time,traceback

# 启动迷信

desired_caps = {}  # 字典存储  配置自动化参数
desired_caps["platformName"] = "Android"  # 运行平台
desired_caps["platformVersion"] = "6"   #  android设备系统的的版本
desired_caps["deviceName"] = "test"
#desired_caps["app"] = r"E:\teacher.apk"   #apk的位置  如果已经安装在模拟器中，可以不填
desired_caps["appPackage"] = "com.huawei.appmarket"   # 应用app的包名  唯一的
desired_caps["appActivity"] ="com.huawei.appmarket.MainActivity"  # 应用某一个操作界面
desired_caps["unicodeKeyboard"] = True  # 编码集  模拟器中安装一个输入法
desired_caps["resetKeyboard"] = True  #
desired_caps["noReset"] = True  #  不会把应用清除掉
desired_caps["newCommandTimeout"] = 6000
# desired_caps["automationName"] = "uiautomator2"

# 启动Remote RPC
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  #  地址是固定，启动session
try:
   print()
   #id 等于com.huawei.appmarket:id/tabLayout的节点元素（childSelector）,根据文本找
   code = 'new UiSelector().resourceId(“com.huawei.appmarket:id/tabLayout”).childSelector(new UiSelector().text("排行"))'
   driver.find_element_by_android_uiautomator(code).click()

   javaCode ='new UiSelector().text("总榜").resourceId("com.huawei.appmarket:id/ItemTitle")'
   ele = driver.find_element_by_android_uiautomator(javaCode)
   destPosY = ele.location["y"]
   xPos = ele.location["x"]
except:
    print(traceback.format_exc())
finally:
    driver.quit()
