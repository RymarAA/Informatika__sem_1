def de(n):
	global a
	for i in range(2, int(n**0.5)+2):
		if n % i == 0:
			a.append(i)
			return de(n//i)
	a.append(n)
	return
a = []
de(int(input()))
print(a)
