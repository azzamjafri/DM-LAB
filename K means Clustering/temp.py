import random

k = 3

loop = 10


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
# print(data)
d1 = random.randint(0, len(data)-1)
d2 = random.randint(0, len(data)-1)
d3 = random.randint(0, len(data)-1)

p1 = data[d1]
p2 = data[d2]
p3 = data[d3]

def dist(p, q):
	return  abs(p[0] - q[0])+  abs(p[1] - q[1])

while loop > 0:
	d1_array = []
	d2_array = []
	d3_array = []


	clusters = {}

	for i in range(k):
		clusters[i] = []
	# print(clusters)

	# print(d1)
	# print(d2)
	# print(d3)


	for i in data:

		d1_array.append(dist(i, p1))
		d2_array.append(dist(i, p2))
		d3_array.append(dist(i, p3))

	# print(d1_array)
	# print(d2_array)
	# print(d3_array)

	def calculateMean(a, b, c):
		sum = 0
		for i in a:
			sum += i
		p1 = sum/len(a)

		sum = 0
		for i in b:
			sum += i
		p2 = sum/len(b)

		sum = 0
		for i in c:
			sum += i
		p3 = sum/len(c)
		# print(p1)
		# print(p2)
		# print(p3)


	print("********************************************************************************* ")
	print("Iteration - {}\n".format(10 - loop + 1))
	print("Point  \t    D1    D2    D4    Cluster")
	for i in range(0, len(data)):
		if d1_array[i] < d2_array[i]:
			if d1_array[i] < d3_array[i]:
				clusters[0].append(i)
				cl = 1
			else:
				clusters[2].append(i)
				cl = 3
		else:
			# b < a
			if d2_array[i] < d3_array[i]:
				clusters[1].append(i)
				cl = 2
			else:
				clusters[2].append(i)
				cl = 3
		print("{}      {}     {}        {}       {}".format(data[i], d1_array[i], d2_array[i], d3_array[i], cl))
		# assignCluster(d1_array[i], d2_array[i], d3_array[i])
		
	calculateMean(d1_array, d2_array, d3_array)

	print("\nClusters assigned - ")
	print("Cluster 1 - {}".format(clusters[0]))
	print("Cluster 2 - {}".format(clusters[1]))
	print("Cluster 3 - {}".format(clusters[2]))
	loop = loop - 1



print("\n\n#############  Clusters  ##############\n")

for i in range(0, len(clusters)):
	t = clusters[i]
	print("Points in Cluster {} ".format(i+1))
	for j in t:
		print(data[j])
