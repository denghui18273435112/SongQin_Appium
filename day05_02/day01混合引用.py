"""
WebView的自动化
app修改编译
    对WebView对象加入serWebContentsDebuggingEnabled的调用

#调试开关
protected void onCreate(Bundle savedInstancaState){
    super.onCreate(savedInstancaState);
    WebView myWebView =(WebView)findViewById(R.id.jcywebview);
    myWebView.setWebContentsDebuggingEnabled(true)
    }

WebView 的内容不依赖所在app
    只是打开一个url
    直接用chrome浏览器打开对应的页面
    使用手机模式

Appium 自动化webview
    appium中把所有的界面环境称之为context
    native 部分的context名称一般为NATIVE_APP
    webview部分context则为WEBVIEW_XXX(应用 app package包)

    我们怎么查看当前有哪些context？
        driver.contexts

    显示当前context的是？
    driver.current_context

    切换混合页面
    driver.switch_to.context("名称")


    在chrome 浏览器中输入 chrome://inspect
    就可以查看混合页面的链接了

    打开android系统通知
    driver.open_notifications()

    按钮操作
    driver.press_keycode(3)  3,按键对应的数值

"""
