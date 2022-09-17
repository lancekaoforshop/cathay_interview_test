from appium import webdriver
from selenium.webdriver.common.by import By
import time
import os

desired_caps = {}  # 空字典 需要給予測試手機相關資訊
desired_caps['platformName'] = 'Android'  # 測試的平台
desired_caps['platformVersion'] = '10.0'  # 手機os版本
desired_caps['deviceName'] = 'TWQA'  # 看你手機的名稱是什麼
desired_caps['automationName'] = "UiAutomator2"  # 一定要的！
desired_caps['autoGrantPermissions'] = True  # 自動同意授權
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main' 
desired_caps['newCommandTimeout'] = 60  # 接收下一個指令的時間(秒)
desired_caps['noReset'] = False  # 改成 True，會保留原先資料，但自動化腳本會失敗
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(15)  # 等待5秒
agree_btn_ele = driver.find_element(By.ID, 'com.android.chrome:id/terms_accept')  # 取得 接受並繼續 元素
print('點擊: {0}'.format(agree_btn_ele.get_attribute('text')))  # 取得 接受並繼續 元素的文字
agree_btn_ele.click()
time.sleep(3)  # 等待3秒

negative_btn_ele = driver.find_element(By.ID, 'com.android.chrome:id/negative_button')  # 取得不用了，謝謝 元素
print('點擊: {0}'.format(negative_btn_ele.get_attribute('text')))  # 取得 不用了，謝謝 元素的文字
negative_btn_ele.click()
print("進入到Googleg首頁")
time.sleep(3)  # 等待3秒

print('進到國泰世華官網')
driver.get("https://www.cathaybk.com.tw/cathaybk/") # 利用https://www.cathaybk.com.tw/cathaybk/ 進到國泰世華官網
time.sleep(10)  # 等待10秒

print('點擊畫面選單按鈕以展開選單')
driver.find_element(By.XPATH, '//android.view.View[@content-desc=" "]/android.widget.Image[1]').click() # 點擊畫面選單按鈕以展開選單
time.sleep(10)  # 等待10秒

print('點擊產品介紹以展開子選單內容')
driver.find_element(By.XPATH, '//android.view.View[@text="產品介紹"]').click() # 點擊產品介紹以展開子選單內容
time.sleep(5) # 等待5秒

print('展開產品介紹後點擊信用卡選項')
driver.find_element(By.XPATH, '//android.view.View[@text="產品介紹"]/../../android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[@text="信用卡"]').click() # 展開產品介紹後點擊信用卡選項
time.sleep(3) # 等待3秒


elements = driver.find_elements(By.XPATH, '//android.view.View[1]/android.view.View[2]/android.view.View[@text="信用卡"]/../android.view.View[@resource-id="lnk_Link"]')
print('個人金融 > 產品介紹 > 信用卡列表下項目數量:', len(elements))
for element in elements:
    print(element.get_attribute('content-desc'))

print('點擊個人金融 > 產品介紹 > 信用卡 > 卡片介紹')
driver.find_element(By.XPATH, '//android.view.View[@content-desc="卡片介紹"]').click()
print('先取得頁面上方顯示之信用卡總類數量')
time.sleep(10) # 等待10秒
total_cards = driver.find_element(By.XPATH, '//android.view.View[@resource-id="layout_0_content_0_updatepanel_0_lbCardsList__amount"]').get_attribute('text') # 頁面上方顯示信用卡種類總數量
print('頁面上方顯示之信用卡總類數量:', total_cards)
