# NCYU 教學意見調查表自動化

[![hackmd-github-sync-badge](https://hackmd.io/98JV6XAWQ3CDQtiVYzOB2w/badge)](https://hackmd.io/98JV6XAWQ3CDQtiVYzOB2w) ![](https://img.shields.io/badge/status-success-green]) 

## 動機
* 每次選課都要重複性的填表單，有幾堂課就要填幾次一樣的問題，且我給老師的評價都會是一致的。因此，我自動化填表單 

## 怎麼使用
* 首先你要是位嘉義大學的學生
* [下載程式碼的壓縮檔](https://github.com/allenlin316/ncyu_autoFill_form/archive/refs/heads/main.zip)
* 你會看到 `ncyu_autoFill_form-main` 的資料夾
* [下載 Python](https://www.python.org/downloads/)
* 在這個資料夾的路徑下開啟終端機
* 執行以下程式碼
    * pip install pipenv
    * pipenv shell 然後按 `Enter`
    * pipenv install selenium 然後按 `Enter`
* 開啟 `webCrawler.py` 檔案(右鍵選擇開啟檔案的方式，建議用 `vs code`)
* 輸入你這學期總共修了幾堂課
* 輸入你的 `校務行政系統` 帳號跟密碼
```=python
# 使用者需要依自己修課狀況自行輸入 (舉例來說)
Ur_ACCOUNT = "10929xx"
Ur_PASSWORD = "123456789"
COURSE_TAKEN_NUM = 9
```
* 打上 `python .\webCrawler.py` 然後按 `Enter` 執行程式碼
* 到了驗證碼必須自己手動輸入，還在研究如何利用模型判斷
> 如果帳密打錯，在終端機打上 `ctrl + c` 中止程式運行，然後再執行一次程式

  
###### tags: automation
