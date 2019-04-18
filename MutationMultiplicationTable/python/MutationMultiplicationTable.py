require = input('請輸入想要的被乘數字：')
for i in range(1, int(require)+1):  # 從1開始輸出到使用者指定的數字
	for j in range(1, 6):  # 5+1
		print(i, "*", j, "=", i*j)
		# 還沒到中間（數字5）之前都要準備倒轉乘數
		if j != 5:
			reverse = 9 - j + 1  # 看看現在乘數應該是多少
			print(i, '*', reverse, '=', i*reverse)
	print()  # 被乘數*9之後換一行空白再輸出比較好看
