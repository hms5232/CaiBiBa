# 算出該行某一列的數字
def count_row_num(n, c):
	if n == c:
		return 2**n - 1
	return count_row_num(n+1, c) - 2**(c-(n+1))


def main():
	n = int(input())  # 第幾行
	ans = 0
	for i in range(1, n+1):
		ans += count_row_num(i, n)
	print(ans)


if __name__ == '__main__':
	main()