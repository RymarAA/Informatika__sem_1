w = [3, 5, 4, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1]
p  = [8, 12, 10, 6, 5, 4, 3, 7, 4, 5, 3, 6, 5, 6, 2]
W = 20
m = [[0 for j in range(W+1)] for i in range(len(p)+1)]
for i in range(1, len(p)+1):
    for j in range(1, W+1):
        if j < w[i-1]:
            m[i][j] = m[i-1][j]
        else:
            m[i][j] = max(m[i-1][j], m[i-1][j - w[i-1]] + p[i-1])
    print(*m[i])
print(m[-1][-1])
j = W
i = len(p)
a = []
while i*j > 0:
    if m[i][j] != m[i-1][j]:
        a.append(i)
        j -= w[i-1]
    i -= 1
print(*a)