def tr(n, symb):
	for i in range(1, n//2+2):
		print(symb*i)
	for i in range(n//2, 0, -1):
		print(symb*i)


n, s = input().split()
n = int(n)
tr(n, s)