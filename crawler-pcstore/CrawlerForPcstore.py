import requests
from bs4 import BeautifulSoup


# 聽說要空兩行，註解要空一格
# 搜尋
def search_title(html):
    key = input("請輸入關鍵字：")  # input key words
    starttag = html.find(key)  # the index of word user wants
    # I got it!
    if starttag != -1:
        # 找到關鍵字之後把往後到下一個標籤之前的字抓起來
        for j in range(starttag, len(html)):
            if html[j].find("<") != -1:
                print("標題止於", j)
                # 現在有關鍵字+往後剩下的標題，該是找關鍵字之前的標題部份了
                for k in range(starttag, 0, -1):
                    if html[k].find(">") != -1:  # 驀然回首，那人卻在燈火闌珊處
                        print("標題始於", k)
                        # 都找到了，印出來吧
                        for i in range(k, j+1):
                            print(html[i], end="")
                        break
                break
        return html.find(key)
    else:
        return "NULL"


""" 
http://blog.castman.net/%E6%95%99%E5%AD%B8/2018/01/27/python-name-main.html

避免被引用的時候本身也執行一次

__name__：模組名稱。當被引用的時候就是模組名稱；如果是被直接執行就會變成__main__

藉此控制式判斷是被直接執行還是引用
"""
if __name__ == '__main__':
    res = requests.get('https://www.pcstore.com.tw/')
    res.encoding = 'big5'  # 網站設定是 big5 編碼
    print("\n關鍵字位於", search_title(res.text))
