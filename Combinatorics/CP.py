#排列組合
#n取k
n = int(input('n:'))
k = int(input('k:'))
a = 1 #n!
b = 1 #k!
c = 1 #(n-k)!
for i in range(1,n+1): #n!
	a *= i
for i in range(1,k+1): #k!
	b *= i
print(n,"!=",a)
print(k,"!=",b)
if(n-k<0):
	print("(",n,"-",k,")!不存在")
	print("There is nothing I can do.")
else:
	for i in range(1,(n-k)+1): #(n-k)!
		c *= i
	print("(",n,"-",k,")!=",c)
	print(a/(b*c),"種組合") #組合Combination
	print(a/c,"種排列") #排列Permutation
print()
input("請按下Enter以結束程式或直接關閉視窗")