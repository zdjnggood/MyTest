# urs/bin/python
# encoding:utf-8

import time
from appium import webdriver
import unittest

#com.jiongji.andriod.card/com.baicizhan.main.activity.MainTabActivity

class MyTestCase(unittest.TestCase):
    #脚本初始化,获取操作实例
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'V6V7N14930009555'
        #desired_caps['appPackage'] = 'com.android.calculator2'
        #desired_caps['appActivity'] = '.Calculator'
        #desired_caps['appPackage'] = 'com.android.customlocale2'
        #desired_caps['appActivity'] = '.CustomLocaleActivity'
        desired_caps['appPackage'] = 'com.jiongji.andriod.card'
        desired_caps['appActivity'] = 'com.baicizhan.main.activity.MainTabActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    #释放实例,释放资源
    def tearDown(self):
        self.driver.quit()



    def teststart_study_button(self):

        schedule_progress_text = self.driver.find_element_by_id("schedule_progress_text")
        schedule_progress_text_str = schedule_progress_text.text
        schedule_progress_text = self.driver.find_element_by_id("schedule_progress_text")
        schedule_progress_text_str = schedule_progress_text.text
        startIndex = schedule_progress_text_str.index(u"成")
        endIndex = schedule_progress_text_str.index(u"/")
        finishWordNumbBefore = int(schedule_progress_text_str[startIndex + 1:endIndex])



        #Locate 定位一个元素
        start_study_button = self.driver.find_element_by_id("start_study_button")
        # Operate 操作一个元素
        start_study_button.click()

        time.sleep(10)

        for x in range(4):
            # Locate 定位一个元素
            hint_button = self.driver.find_element_by_id("hint")
            # Operate 操作一个元素
            hint_button.click()

        time.sleep(5)

        # Locate 定位一个元素
        continue_learn_button = self.driver.find_element_by_id("continue_learn")
        # Operate 操作一个元素
        continue_learn_button.click()

        # Locate 定位一个元素
        home_button = self.driver.find_element_by_id("home")
        # Operate 操作一个元素
        home_button.click()

        time.sleep(2)

        # Verify 验证操作的结果
        startIndex=schedule_progress_text_str.index(u"成")
        endIndex=schedule_progress_text_str.index(u"/")
        finishWordNumb=schedule_progress_text_str[startIndex+1:endIndex]
        print u"今日完成单词 ：" + finishWordNumb
        finishWordNumbAfter=int(finishWordNumb)
        self.assertEqual(finishWordNumbAfter, finishWordNumbBefore)



        #Verify 验证操作的结果

        #Exception 处理异常的情况
    # def testOtherAPI(self):
    #     '''elements = self.driver.find_elements_by_id("digit8")
    #     elements[0].click()
    #     time.sleep(5)
    #     print(len(elements))'''
    #     time.sleep(3)
    #     #self.driver.press_keycode(8)
    #     #self.driver.press_keycode(7)
    #     input = self.driver.find_element_by_class_name("android.widget.EditText")
    #     input.send_keys("10")
    #
    #     element = self.driver.find_element_by_accessibility_id(u"除")
    #     element.click()
    #
    #     self.driver.press_keycode(12)
    #
    #     equal = self.driver.find_element_by_id("equal")
    #     equal.click()
    #     time.sleep(5)

    # #其他更多APIs的使用实例
    # def testMoreAPIs(self):
    #     #获取元素列表
    #     els = self.driver.find_elements_by_class_name('android.widget.CheckedTextView')
    #     #滚动API scroll 的用法
    #     #self.driver.scroll(els[10], els[1])
    #     #拖拽API drag_and_drop的用法
    #     #self.driver.drag_and_drop(els[10], els[3])
    #     #滑动API swipe的用法
    #     #self.driver.swipe(100, 750, 100, 100)
    #     #点击API tap的用法
    #     #self.driver.tap([(100, 750)])
    #
    #     #快速滑动 API flick的用法
    #     #self.driver.flick(100, 750, 100, 100)
    #     #当前activity API current_Activity的用法
    #     #print self.driver.current_activity
    #     #将某一个App置于后台
    #     #self.driver.background_app(3)
    #     #等待指定activity显示 API wait_activity的用法
    #     #print self.driver.wait_activity(".CustomLocaleActivity", 3, 1)
    #
    #     #判断app是否安装了
    #     #print self.driver.is_app_installed("com.example.zhangjian.minibrowser2")
    #     #删除app
    #     #self.driver.remove_app("com.example.zhangjian.minibrowser2")
    #     #安装app
    #     #self.driver.install_app("/Users/zhangjian/Downloads/app-debug.apk")
    #     #启动app
    #     #self.driver.launch_app()
    #
    #     #关闭app
    #     #self.driver.close_app()
    #     #self.driver.launch_app()
    #     #启动activity
    #     self.driver.start_activity("com.example.zhangjian.minibrowser2",
    #                                            ".myapplication.NewActivity")
    #     time.sleep(3)
    #     #截屏
    #     self.driver.get_screenshot_as_file("test.png")
    #     time.sleep(5)


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(MyTestCase('testMoreAPIs'))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

