import re

with open('input.txt') as f:
	t = f.read()
t = t.replace('\n', ' ')
print(t)
p = r'[!?.][ ]'
k = 0
for el in re.finditer(p, t):
	k += 1
print(k)
