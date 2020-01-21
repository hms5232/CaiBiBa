def count_row_num(n):
	if n == 10:
		return 2**n - 1
	return count_row_num(n+1) - 2**(10-(n+1))

n = 10
ans = 0
for i in range(1, n+1):
	ans += count_row_num(i)
print(ans)
