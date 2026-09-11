a = list(map(int, input().split()))
mxel = 0
mx = 0
for el in set(a):
	c = a.count(el)
	if c > mx:
		mx = c
		mxel = el
print(mxel)
