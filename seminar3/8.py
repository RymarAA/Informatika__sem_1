import numpy as np
import random


def MNK(x, y):
	b = (n*sum([x[i]*y[i] for i in range(n)])-sum(x)*sum(y))/(n*sum([x[i]**2 for i in range(n)])-sum(x)**2)
	print(b)
	a = sum(y)/n - sum(x)/n*b
	print(a)


def create(n):
	X = [i for i in range(1, n+1)]
	a = []
	for el in X:
		a.append(19*el+9+random.gauss(mu=0, sigma=0.5))
	return X, a

n = int(input())
X, Y = create(n)
MNK(X, Y)