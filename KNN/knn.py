from math import sqrt

dataset = [[2, 2, 0],
	[1, 3, 0],
	[2, 1, 0],
	[1, 1, 0],
	[5, 3, 0],
	[9, 2, 0],
    [1, 1, 0],
    [3, 4, 0],
    [1, 2, 0],
    [7, 3, 1],
    [6, 0, 1],
    [8, 1, 1],
    [5, 4, 1],
    [6, 5, 1],
    [7, 5, 1],
    [6, 6, 1],
    [7, 6, 1],
    [6, 7, 1],
    ]



test_dataset = [3, 1]

K = 3



def euclidean_distance(training, test_dataset):
 distance = 0.0
 for i in range(len(training)-1):
  distance += (training[i] - test_dataset[i])**2
 # print(distance)
 return distance**(1/2)

def Sort(sub_li):
 return(sorted(sub_li, key = lambda x: x[0]))   


## FINDING NEIGHBOURS ##

distance = []
for row in dataset:
 disp = euclidean_distance(row, test_dataset)
 distance.append([disp, row[-1]])

distance = Sort(distance)
print("Sorted Distances are - ")
for temp in distance:
	print(temp)
distance = distance[:K]

output_values = [row[-1] for row in distance]

prediction = max(set(output_values), key=output_values.count)

print("\n***********************************************************\n")
print("Final Distances are - ")
print(distance)
print("\n***********************************************************")
print("Predicted Class - %d" % (prediction))
# print(prediction)