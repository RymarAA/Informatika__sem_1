a = list(map(int, input().split()))
for i in range(len(a)):
	f = True
	for j in range(len(a)):
		if i != j and a[j] == a[i]:
			f = False
			break
	if f:
		print(a[i])
