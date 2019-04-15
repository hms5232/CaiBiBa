import requests
from bs4 import BeautifulSoup


# 聽說要空兩行，註解要空一格
res = requests.get('https://www.pcstore.com.tw/')
res.encoding = 'big5'  # 網站設定是 big5 編碼
print(res.text)
