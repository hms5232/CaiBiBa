"""
 * I（1）
 * V（5）
 * X（10）
 * L（50）
 * C（100）
 * D（500）
 * M（1000）
"""


# 檢查使用者輸入的羅馬數字和轉換成阿拉伯數字
def transformRomanNum(ronum):
	# 沒有switch QQ
	return {
		'I':1,
		'V':5,
		'X':10,
		'L':50,
		'C':100,
		'D':500,
		'M':1000
	}.get(ronum, -1)  # 預設回傳-1


# 不能連續四個一樣的數碼
def checkRestriction(numerals):
	for j in range(2, len(numerals)-1):
		"""
			XXXX
			  ↑
			檢查前面兩個和後面一個數碼是否和現在指向的數碼相同
		"""
		if(numerals[j-2]==numerals[j] and numerals[j-1]==numerals[j] and numerals[j+1]==numerals[j]):
			if(numerals[j] == 1):  # 唯一的例外IIII
				continue
			return 1;
	return 0;


# 最後，當然就是加起來囉（不過還要檢查左減的數碼）
def compute(numerals):
	result = 0  # ※羅馬數字中是沒有0的喔
	for l in range(len(numerals)):
		if(l == 0):
			result += numerals[l]
			continue
		if(numerals[l] > numerals[l-1]):  # 左邊的數字比較小就減掉
			# 左減的數字有限制，僅限於I、X、C
			if(numerals[l-1]==1 or numerals[l-1]==10 or numerals[l-1]==100):
				numerals[l-1] *= -2  # 加倍奉還（把原本加上去的扣回來）
				result += (numerals[l] + numerals[l-1])
			else:
				print("左減的數字有限制，僅限於I、X、C")
				exit(0)
		else:  # 右邊的數字比較小就相加
			result += numerals[l]
	return result


# == 以下 main ==

ronum = input("請輸入：")
# python 沒有陣列(Array)但有列表(list)
nums = list(ronum.upper())  # 將使用者輸入的東西逐一放進list
numerals = []  # 存放轉換成的阿拉伯數字

# 檢查使用者輸入的羅馬數字數碼
for i in range(len(nums)):
	checkRomanNum = transformRomanNum(nums[i])
	if(checkRomanNum == -1):  # 『好像有奇怪的東西混進來了』
		print(nums[i]+" 不是正確的羅馬數字")
		exit(0)  # return 不能用在 outside function
	else:
		numerals.append(checkRomanNum)

# 不能連續四個一樣的數碼
if(checkRestriction(numerals)):
	print("不能連續四個一樣的數碼")
	exit(0)

# 『さあ、ゲームを始めよう』
print("結果：",compute(numerals))
input()