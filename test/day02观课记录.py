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
driver.implicitly_wait(10)   #等待时间
try:
    kecheng = "语文课程"
    teacher = "黄老师"
    neirong = "好好学习，天天向上"
    guanKeJiLu = 'new UiSelector().text("观课记录").className("android.widget.TextView")'
    driver.find_element_by_android_uiautomator(guanKeJiLu).click()  # 点击观课记录
    time.sleep(3)
    driver.find_element_by_id("com.jufa.mt.client:id/tv_right").click() #点击添加按钮
    driver.find_element_by_id("com.jufa.mt.client:id/et_course_name").send_keys(kecheng)  # 选择课程课题并输入数据
    driver.find_element_by_id("com.jufa.mt.client:id/et_course_teacher").send_keys(teacher) # 填写任课教师
    driver.find_element_by_id("com.jufa.mt.client:id/tv_select_class").click()  # 点击班级
    className = 'new UiSelector().text("五年级4班").className("android.widget.TextView")'
    driver.find_element_by_android_uiautomator(className).click()  # 点击观课记录
    time.sleep(1)
    driver.find_element_by_id("com.jufa.mt.client:id/tv_select_subject").click()
    guanKeJiLu = 'new UiSelector().text("英语").className("android.widget.TextView")'
    driver.find_element_by_android_uiautomator(guanKeJiLu).click()  # 选择科目
    driver.find_element_by_id("com.jufa.mt.client:id/et_content").send_keys(neirong)
    driver.find_element_by_id("com.jufa.mt.client:id/tv_right").click()


    title = driver.find_elements_by_id("com.jufa.mt.client:id/tv_item_title")
    content = driver.find_elements_by_id("com.jufa.mt.client:id/tv_item_content")
    for t in title:
        print(t.text)
        if kecheng  in t.text:
            break
        print("发布成功")




except:
    print(traceback.format_exc())


