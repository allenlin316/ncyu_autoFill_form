
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller
from PIL import Image
import io
import ddddocr

def crack_captcha(chrome, img_element):
    # Get the location and size of the image element
    location = img_element.location
    size = img_element.size
    # Take a screenshot of the entire page
    screenshot = chrome.get_screenshot_as_png()
    # Convert the screenshot to a PIL Image
    screenshot = Image.open(io.BytesIO(screenshot))
    # Calculate the bounding box of the image element
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    # Crop the screenshot to the bounding box of the image element
    cropped_image = screenshot.crop((left, top, right, bottom))
    # Save the cropped image to a BytesIO object to get the binary data
    image_bytes = io.BytesIO()
    cropped_image.save(image_bytes, format='jpeg')
    image_binary = image_bytes.getvalue()
    res = ocr.classification(image_binary).upper()
    return res

ocr = ddddocr.DdddOcr()
chromedriver_autoinstaller.install()
# check if the current version of chromedriver exists, if not download it automatically, then add it to current directory
chromedriver_autoinstaller.install(cwd=True)
chrome = webdriver.Chrome()

chrome.get('https://web085004.adm.ncyu.edu.tw/NewSite/Login.aspx?Language=zh-TW')

account = chrome.find_element(By.ID, 'TbxAccountId')
pwd = chrome.find_element(By.ID, 'TbxPassword')
captcha_input = chrome.find_element(By.ID, 'TbxCaptcha')
captcha = chrome.find_element(By.ID, 'Image1')
check_in_btn = chrome.find_element(By.ID, 'BtnPreLogin')
total_question = 21

# 使用者需要依自己修課狀況自行輸入
Ur_ACCOUNT = "校務行政系統帳號"
Ur_PASSWORD = "校務行政系統密碼"
COURSE_TAKEN_NUM = 7 #輸入修課的數量

account.send_keys(Ur_ACCOUNT)
pwd.send_keys(Ur_PASSWORD)
# 透過 python library 自動填寫驗證碼
keys = crack_captcha(chrome, captcha)
captcha_input.send_keys(keys)
check_in_btn.click()
print('嘗試登入嘉大校務行政系統')
time.sleep(2)

while True:
    try: # 登入成功
        menu_btn = chrome.find_element(By.ID, 'BtnMenu')
        break
    except: # 登入失敗
        print("帳號或密碼可能打錯了")
        close_btn = WebDriverWait(chrome, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/button'))
        )
        close_btn.click()
        captcha_input.clear()
        keys = crack_captcha(chrome, captcha)
        captcha_input.send_keys(keys)
        check_in_btn.click()
        print('嘗試登入嘉大校務行政系統')
        time.sleep(2)

menu_btn.click()
time.sleep(2)
evaluation_btn = chrome.find_element(By.XPATH, '//*[@id="application-menu-main"]/div[2]/div[7]/span[2]/a')
evaluation_btn.click()

print('switch to iframe')
chrome.switch_to.frame("application-frame-main")
form_btn = chrome.find_element(By.ID, 'ctl00_ContentPlaceHolder1_BtnEntAns')
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