with open('C:\semestr1\seminar2\input.txt') as f:
	t = f.read()
t = t.replace('\n', ' ')
t += ' '
k = 0
for i in range(1, len(t)):
	if t[i] == ' ' and t[i - 1] in ['.', '?', '!']:
		k += 1
print(k)
