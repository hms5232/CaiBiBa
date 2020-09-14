"""
Author: hms5232
"""


'''
算錯虧錢不干我的事喔
'''
price = int(input('請輸入股價：'))  # 每股/元
fee = price*1000*0.001425  # 原本手續費應該是多少
print("原始券商手續費：{}".format(fee))
print("電子下單手續費：{}".format(fee*0.6))
print("手續費CP最大化：{}張".format(20/(fee)))
print("電子單CP最大化：{}張".format(20/(fee*0.6)))
