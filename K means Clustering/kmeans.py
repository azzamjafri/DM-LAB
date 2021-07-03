data = [1,2,3,4,5,11,12,13,14,25]
import random


def init(K,data):
	centroid=[]
	clusters=[]
	for i in range(K):
		random_element=random.choice(data)
		while random_element in centroid:
			random_element=random.choice(data)
	
		centroid.append(random_element)
			# print(centroid)
	for i in range(K):
		clusters.append([centroid[i]])

	return [centroid,clusters]


initial_list=init(2,data)
print(initial_list)
centroid=initial_list[0]
clusters=initial_list[1]
print(centroid)


def which(element,k):
	for i in range(k):
		if element in clusters[i]:
			return i
	return -1


def traversal(K):
	change=False
	for each in data:
		which_c=which(each,K)
		if each not in centroid:
			distance=[]
			for dis in centroid:
				distance.append(abs(dis-each))
			min_d=100000
			cent=0
			for i in range(len(distance)):
				if distance[i]<min_d:
					cent=i
					min_d=distance[i]
			for i in range(len(clusters)):
				if each in clusters[i]:
					clusters[i].remove(each)
					# print(clusters[i])
				if cent==which_c and which_c is not -1:
					return True
				clusters[cent].append(each)
				centroid[cent]=(each+centroid[cent])/2
	return change

change =True
loop = 10
# while change is True:
while loop > 0:

	K=2
	change=traversal(K)
	# print(centroid)
	# print(clusters)
	print("----------------------------")
	loop = loop-1