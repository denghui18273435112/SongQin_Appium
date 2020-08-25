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
    content = "好好学习，天天向上"
    driver.implicitly_wait(10)
    driver.find_element_by_id("com.jufa.mt.client:id/iv_quick_img").click()  # 点击教师通知
    time.sleep(10)
    driver.find_element_by_id("com.jufa.mt.client:id/tv_publish").click()
    driver.find_element_by_id("com.jufa.mt.client:id/et_title").send_keys("学校教师通知")
    driver.find_element_by_id("com.jufa.mt.client:id/et_content").send_keys(content)
    driver.find_element_by_id("com.jufa.mt.client:id/tv_add").click()
    time.sleep(10)
    ele = driver.find_elements_by_class_name("android.widget.TextView")
    for eles in ele:
         if eles == content:
             print("发布成功")
             break

except:
    print(traceback.format_exc())

# finally:
#     driver.quit()
