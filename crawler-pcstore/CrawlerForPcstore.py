import requests
from bs4 import BeautifulSoup


# 聽說要空兩行，註解要空一格


""" 
http://blog.castman.net/%E6%95%99%E5%AD%B8/2018/01/27/python-name-main.html

避免被引用的時候本身也執行一次

__name__：模組名稱。當被引用的時候就是模組名稱；如果是被直接執行就會變成__main__

藉此控制式判斷是被直接執行還是引用
"""
if __name__ == '__main__':
    res = requests.get('https://www.pcstore.com.tw/')
    res.encoding = 'big5'  # 網站設定是 big5 編碼
    print(res.text)
