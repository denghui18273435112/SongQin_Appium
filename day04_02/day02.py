from appium  import  webdriver
import time,traceback

# 启动迷信

desired_caps = {}  # 字典存储  配置自动化参数
desired_caps["platformName"] = "Android"  # 运行平台
desired_caps["platformVersion"] = "6"   #  android设备系统的的版本
desired_caps["deviceName"] = "test"
#desired_caps["app"] = r"E:\teacher.apk"   #apk的位置  如果已经安装在模拟器中，可以不填
desired_caps["appPackage"] = "io.manong.developerdaily"   # 应用app的包名  唯一的
desired_caps["appActivity"] ="io.toutiao.android.ui.activity.LaunchActivity"  # 应用某一个操作界面
desired_caps["unicodeKeyboard"] = True  # 编码集  模拟器中安装一个输入法
desired_caps["resetKeyboard"] = True  #
desired_caps["noReset"] = True  #  不会把应用清除掉
desired_caps["newCommandTimeout"] = 6000
# desired_caps["automationName"] = "uiautomator2"

# 启动Remote RPC
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  #  地址是固定，启动session
try:
    command = 'new UiSelector().text("我的").className("android.widget.TextView")'
    driver.find_element_by_android_uiautomator(command).click()
    time.sleep(3)

    ele1 = driver.find_element_by_id("io.manong.developerdaily:id/nav_btn_favorite")  #找元素
    screenSize = driver.get_window_size()
    screenW = screenSize["width"]
    screenH = screenSize["height"]
    x = screenW / 2
    y1 = int(screenH * 0.8)
    y2 = int(screenH * 0.4)
    driver.swipe(x, y1, x, y2, 500)
    driver.find_element_by_id(
        "io.manong.developerdaily:id/nav_btn_setting"
    ).click()
    print("运行完成")
except:
    print(traceback.format_exc())

finally:
    driver.quit()
