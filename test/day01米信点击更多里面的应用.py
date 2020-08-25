from appium  import  webdriver
import time,traceback

# 启动迷信

desired_caps = {}  # 字典存储  配置自动化参数
desired_caps["platformName"] = "Android"  # 运行平台
desired_caps["platformVersion"] = "6"   #  android设备系统的的版本
desired_caps["deviceName"] = "test"
#desired_caps["app"] = r"E:\teacher.apk"   #apk的位置  如果已经安装在模拟器中，可以不填
desired_caps["appPackage"] = "com.jufa.mt.client"   # 应用app的包名  唯一的
desired_caps["appActivity"] ="com.jufa.mt.client.ui.LogoActivity"  # 应用某一个操作界面
desired_caps["unicodeKeyboard"] = True  # 编码集  模拟器中安装一个输入法
desired_caps["resetKeyboard"] = True  #
desired_caps["noReset"] = True  #  不会把应用清除掉
desired_caps["newCommandTimeout"] = 6000
# desired_caps["automationName"] = "uiautomator2"

# 启动Remote RPC
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  #  地址是固定，启动session

try:
    driver.implicitly_wait(10)   #等待时间
    code = 'new UiSelector().text("更多").className("android.widget.TextView")'  #通过UiSelector找元素
    driver.find_element_by_android_uiautomator(code).click()   # 点击更多
    time.sleep(2)   # 等待两秒
    driver.find_elements_by_id("com.jufa.mt.client:id/tv_function")  #定位元素

    chuang = driver.find_element_by_id("com.jufa.mt.client:id/listview")
    location = chuang.location  # x y
    size = chuang.size  # width height
    x = int(size["width"])*0.5
    y1 = (location["y"] + int(size["height"]))*0.8
    y2 = location["y"]*2

    t = False
    Name = "备忘小结"
    while True:
        ele = driver.find_elements_by_id("com.jufa.mt.client:id/tv_quick_txt")
        for e in ele:
            #print(e.text)
            if Name in e.text:
                t = True
                break
        if t:
            break
        else:
            driver.swipe(x, y1, x, y2,500)
            time.sleep(0.5)
    c = 'new UiSelector().text("备忘小结").resourceId("com.jufa.mt.client:id/tv_quick_txt")'
    driver.find_element_by_android_uiautomator(c).click()
    time.sleep(1)


    tianjia = 'new UiSelector().text("添加").className("android.widget.TextView").resourceId("com.jufa.mt.client:id/tv_right")'
    driver.find_element_by_android_uiautomator(tianjia).click()


    tianjia = 'new UiSelector().text("请输入标题").className("android.widget.EditText").resourceId("com.jufa.mt.client:id/et_title")'
    driver.find_element_by_android_uiautomator(tianjia).send_keys("标题")
    tianjia1 = 'new UiSelector().text("请输入内容...").className("android.widget.EditText")'
    driver.find_element_by_android_uiautomator(tianjia1).send_keys("内容")
    tianjia2 = 'new UiSelector().text("保存").className("android.widget.TextView").resourceId("com.jufa.mt.client:id/tv_right")'
    driver.find_element_by_android_uiautomator(tianjia2).click()
except:
    print(traceback.format_exc())
# finally:
#      driver.quit()
