a=int(input("  "))
i=int(input("  "))
k=int(input(" "))
n=int(input("  "))
m=int(input("  "))
s=int(input("  "))
for i in range(n):
	if a>k:
		k=a
		s=s+a
	if k>m and s<m+n-1:
		print('no')
	else:
		print("yes")
	