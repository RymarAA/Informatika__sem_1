import numpy as np



r, c = map(int, input().split())
m = []
for i in range(r):
    m.append(list(map(int, input().split())))
a = np.array([m[i][0:c-1] for i in range(r)])
b = np.array([m[i][-1] for i in range(r)])
x = np.linalg.solve(a, b)
print(x)