import numpy as np


r, c = map(int, input().split())
m = []
for i in range(r):
	m.append([0 for j in range(c)])
k = 1
i, j = 0, 0
f = False
d = 'r'
while not f:
	if -1 < i < r and -1 < j < c and m[i][j] == 0:
		m[i][j] = k
		k += 1
	else:
		if d == 'r':
			d = 'd'
			i += 1
			j -= 1
		elif d == 'd':
			d = 'l'
			i -= 1
			j -= 1
		elif d == 'l':
			d = 'u'
			i -= 1
			j += 1
		else:
			d = 'r'
			i += 1
			j += 1
		m[i][j] = k
		k += 1
	if d == 'r':
		j += 1
	elif d == 'd':
		i += 1
	elif d == 'l':
		j -= 1
	else:
		i -= 1
	if k == r*c + 1:
		f = True
print(*m, sep='\n')
m1 = []
for i in range(r):
	a = np.array([m[i][j] for j in range(c)])*i
	m1.append(a)
print(*m1, sep="\n")