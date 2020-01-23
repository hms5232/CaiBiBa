'''
See https://github.com/hms5232/CaiBiBa/tree/master/EricaCompanyBonus for more information.
'''

'''
        ......  ......  ......
       7  14  28  56 112  ......
    3  6  12  24  48  96  ......
 1  2  4   8  16  32  64  ......
--------------------------------
1  5  17  49  129  ........  ?
'''


# 計算「列」上第 n 個位置的數字
def row_calculate(n):
	if n % 2 != 0:
		return n
	else:
		return row_calculate(n - 1) * 2
		

def main():
	user_input = int(input())  # 輸入要幾行/列
	all_list = [[0] * user_input for i in range(user_input)]  # 整體
	all_list[0][0] = 1  # 起始值

	for j in range(user_input):
		# 空白部分補 0
		for k in range(j):
			all_list[j][k] = 0
		
		# 計算數字囉
		m = j  # 前面空白的部分就不用計算了
		while m < user_input:
			if j == m:  # 每列的起點
				if j == 0:  # 起源
					# 因為已經在上面設定過了所以直接跳過即可
					m += 1
					continue
				# 起點的話為該行往下一列的數字+1
				all_list[j][m] = all_list[j-1][m] + 1
				m += 1
				continue
			# 剩下的則是左邊數字的兩倍
			all_list[j][m] = all_list[j][m-1]*2
			m += 1
	print(all_list)
	
	# 最後算出每一行的總和
	column_sum_list = []  # 每一行的和
	for o in range(user_input):  # column
		column_sum = 0  # 該行總和
		for p in range(user_input):  # row
			column_sum += all_list[p][o]  # 找出o行p列的數字
		column_sum_list.append(column_sum)
	print('------------ SUM ------------\n', column_sum_list)


if __name__ == '__main__':
	main()
