
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
# check if the current version of chromedriver exists, if not download it automatically, then add it to current directory
chromedriver_autoinstaller.install(cwd=True)
chrome = webdriver.Chrome()

chrome.get('https://web085004.adm.ncyu.edu.tw/NewSite/Login.aspx?Language=zh-TW')

account = chrome.find_element_by_id('TbxAccountId')
pwd = chrome.find_element_by_id('TbxPassword')
captcha = chrome.find_element_by_id('TbxCaptcha')
check_in_btn = chrome.find_element_by_id('BtnPreLogin')
total_question = 21

# 使用者需要依自己修課狀況自行輸入
Ur_ACCOUNT = "校務行政系統的帳號"
Ur_PASSWORD = "校務行政系統的密碼"
COURSE_TAKEN_NUM = 7 #輸入修課的數量

account.send_keys(Ur_ACCOUNT)
pwd.send_keys(Ur_PASSWORD)
# 必須得自己手動輸入驗證碼
element = WebDriverWait(chrome, 20).until(lambda driver: len(captcha.get_attribute("value")) == 4)
check_in_btn.click()
print('嘗試登入嘉大校務行政系統')
time.sleep(2)

while True:
    try: # 驗證碼打對
        menu_btn = chrome.find_element_by_id('BtnMenu')
        break
    except: # 驗證碼打錯
        close_btn = chrome.find_element_by_xpath('/html/body/div[1]/div[1]/button')
        close_btn.click()
        captcha.clear()
        element = WebDriverWait(chrome, 20).until(lambda driver: len(captcha.get_attribute("value")) == 4)
        check_in_btn.click()
        print('嘗試登入嘉大校務行政系統')
        time.sleep(2)

menu_btn.click()
time.sleep(2)
evaluation_btn = chrome.find_element_by_xpath('//*[@id="application-menu-main"]/div[2]/div[7]/span[2]/a')
evaluation_btn.click()

print('switch to iframe')
chrome.switch_to.frame("application-frame-main")
form_btn = chrome.find_element_by_id('ctl00_ContentPlaceHolder1_BtnEntAns')
form_btn.click()
time.sleep(2)


for totalQ in range(1, COURSE_TAKEN_NUM+1):
    print("進入到表單頁面")
    menu_confirm_btn =  chrome.find_element(By.ID, "ctl00_ContentPlaceHolder1_BtnSure")
    menu_confirm_btn.click()
    time.sleep(2)
    for qIndex in range(1, total_question+1):
        print("開始填表單")
        try:
            q = chrome.find_element(By.ID, "ctl00_ContentPlaceHolder1_RBAns" + str(qIndex) + "_0")
            q.click()
        except:
            time.sleep(2)
            break
    print("表單完成")
    submit = chrome.find_element(By.ID, "ctl00_ContentPlaceHolder1_BtnSave")
    submit.click()
    go_back_btn = chrome.find_element(By.ID, "ctl00_ContentPlaceHolder1_BtnEntAns")
    go_back_btn.click()
    time.sleep(2)