import matplotlib.pyplot as plt
import numpy as np
data = [
	(126, 171.0),
	(116, 156.9),
	(99, 133.5),
	(78, 105.15),
	(65, 85.5),
	(49, 65.1),
	(53, 71.5),
	(67, 90.3),
	(89, 120.0),
	(94, 126.9),
	(105, 141.6),
	(118, 159.2),
]
n = len(data)
x = []
y = []
for a, b in data:
	x.append(b)
	y.append(a*4)

k = (n*sum([x[i]*y[i] for i in range(len(x))])-sum(x)*sum(y))/(n*sum([el**2 for el in x])-sum(x)**2)
b = sum(y)/n - k * sum(x) / n

x_line = np.linspace(min(x), max(x), 100)
y_line = k * x_line

x_err = 0.05
y_err = 2

plt.errorbar(
    x, y, 
    xerr=x_err,
    yerr=y_err,
    fmt='o',
    color='black',
    ecolor='black',
    elinewidth=1.5,
    capsize=4,
    label='Данные эксперимента'
)
dk = 1/n**0.5*abs((sum([el**2 for el in y])-sum(y)**2)/(sum([el**2 for el in x])-sum(x)**2)-k**2)**0.5

plt.plot(
    x_line, y_line, 
    color='blue', linestyle='-', linewidth=2, 
    label=f'Аппроксимация: y = {k:.3f}x + ({b:.3f})\n d = {dk:.3f}'
)

dk = 1/n**0.5*abs((sum([el**2 for el in y])-sum(y)**2)/(sum([el**2 for el in x])-sum(x)**2)-k**2)**0.5
db = dk*abs(sum([el**2 for el in x])-sum(x)**2)**0.5
print(f'{dk:.3f}    {db:.3f}')
plt.title('График U(I) для L = 30 см')
plt.xlabel('I, мА')
plt.ylabel('U, мВ')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.show()