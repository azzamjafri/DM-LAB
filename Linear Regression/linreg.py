


data = [[1, 3],
		[2, 5],
		[3, 4],
		[6, 8],
		[4, 5],
		[5, 9],
		[7, 12],
		[8, 9],
		[9, 15],
		[10, 20],
	]
print(data)
def Mean(db, index):
	x_sum = 0
	for id in db:
		# print(id)
		x_sum += float(id[index])

	return (x_sum/len(db))


X_mean = Mean(data, 0)
print(X_mean)
Y_mean = Mean(data, 1)
print(Y_mean)


def SigmaXx_Yy(db):
	num = 0
	for id in db:
		
		xX = float(id[0]) - X_mean
		yY = float(id[1]) - Y_mean
		prod = xX * yY
		#print(prod)
		num += prod
	return num


Xx_Yy = SigmaXx_Yy(data)
print(Xx_Yy)


def SigmaXx2(db):
	prod = 0
	for id in db:
		
		sub = float(id[0]) - X_mean
		prod += sub * sub
		#print(prod)
	return prod


Xx2 = SigmaXx2(data)
print(Xx2)


b1 = Xx_Yy / Xx2
print(b1)


b0 = Y_mean - (b1 * X_mean)
print(b0)


def linear(q=None):
	if q:
		pt = [q , b0 + b1 * q]
		return pt
	return

linear(10)

import numpy as np
from matplotlib import pyplot as plt

# x = np.linspace(0,30,100)
x = np.array(data)

y = b0 + b1*x
x_p=[]
y_p = []
for id in data:
	x_p.append(id[0])
	y_p.append(id[1])
print(x_p)
print(y_p)
plt.scatter(x_p, y_p, color="green", marker="^", s=20)
plt.plot(x, y, color="yellow")
plt.show()
# plt.scatter(x_test,predictions,color="d")