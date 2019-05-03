"""
CreditCardForeignTradeCalculation
如題
只是計算手中卡片國外消費該用哪張卡比較划算的小程式
因為懶得每次都要拿計算機或心算（重點有的還無條件捨去所以要算到小數點才準確
"""


price = float(input("輸入價格："))  # 輸入價格
print("手續費：", price*0.015)  # 國外交易手續費1.5%
# 開始各種回饋%數大亂鬥
print("2% = ", price*0.02, "（扣除手續費後為", price*0.005, "）")
print("2.5% = ", price*0.025, "（扣除手續費後為", price*0.01, "）")
print("2.8% = ", price*0.028, "（扣除手續費後為", price*0.013, "）")
print("3% = ", price*0.03, "（扣除手續費後為", price*0.015, "）")
input()
