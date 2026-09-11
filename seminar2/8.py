def findnewmin(m, a):
	nm = 10**6
	for el in a:
		if el > m:
			if el < nm:
				nm = el
	return nm


n = int(input())
a = list(map(int, input().split()))
r = -10**6
for i in range(n//2+1):
	r = findnewmin(r, a)
print(r)
