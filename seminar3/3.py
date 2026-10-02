def nod(n, m):
	if  n % m == 0:
		return m
	else:
		return nod(m, n%m)

a, b = map(int, input().split())
a, b = max(a, b), min(a, b)
d = nod(a, b)
k, m = a // d, b // d
for x in range(10**8):
	y = abs(1-x*k)
	if y % m == 0:
		ans1 = (x, -(y // m))
		break
for y in range(10**8):
	x = abs(1-y*m)
	if x % k == 0:
		ans2 = (-(x // k), y)
		break
if (ans1[0] + abs(ans1[1])) < (abs(ans2[0]) + ans2[1]):
	print(ans1)
elif (ans1[0] + abs(ans1[1])) == ( abs(ans2[0]) + ans2[1]):
	if ans1[0] < ans2[0]:
		print(ans1)
	else:
		print(ans2)
else:
	print(ans2)