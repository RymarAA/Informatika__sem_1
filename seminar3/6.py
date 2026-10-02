import numpy as np

def k_MNK(X, Y):
	return (n*sum(X*Y)-sum(X)*sum(Y))/(n*sum(X*X)-sum(X)**2)


def b_MNK(X, Y):
	return sum(Y)/n - k_MNK(X, Y)*sum(X)/n


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
X = np.array([data[i][1] for i in range(n)])
Y = np.array([data[i][0]*4 for i in range(n)])

print(k_MNK(X, Y), b_MNK(X, Y))