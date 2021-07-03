#read csv file
with open('text1.csv') as file:
    DataSet = file.read()
DataSet = [float(i) for i in DataSet.split('\n')]


print(DataSet)

k = 3

def distance(a, b):
    return abs(b-a)

def show():
    for i in clusters:
        print(i)


def avg(a):
    k=0
    for i in a:
        k+=i
    return k/(len(a))


def getMeans(clusters):
	for i in clusters:
		currMean.append(avg(i))
	return currMean



def getMeansfrommean(clusters):
    for ix in range(len(clusters)):
        i=clusters[ix]
        currMean[ix] = avg(i)
    return currMean



def update(clusters, target_cluster, a):
    clusters[target_cluster].append(a)
    return clusters


def compare(clusters, a):
    min_d = distance(clusters[0][0], a)
    target_cluster = 0
    for i in range(1, k):
        temp_d = distance(clusters[i][0], a)
        if temp_d < min_d:
            min_d = temp_d
            target_cluster = i
    update(clusters, target_cluster, a)


def compare_from_mean(prevMean,a):
    min_d = distance(prevMean[0],a)
    target_cluster = 0
    for i in range(1, k):
        temp_d = distance(prevMean[i], a)
        if temp_d < min_d:
            min_d = temp_d
            target_cluster = i
    update(clusters, target_cluster, a)


def create_clusters(DataSet, k):
    for i in DataSet[k:]:
        compare(clusters, i)
    show()

def create_clusters_from_mean(DataSet,K):
    for i in DataSet:
        compare_from_mean(prevMean,i)
    show()



clusters = [[i] for i in DataSet[:k]]
prevMean=[]
currMean=[]
for i in range(0,k):
    prevMean.append(-1)
create_clusters(DataSet,3)
getMeans(clusters)
print(currMean)
print(prevMean)
while(currMean != prevMean):
    clusters = [[],[],[]]
    prevMean=currMean
    create_clusters_from_mean(DataSet,3)
    getMeansfrommean(clusters)
    print(currMean)
    print(prevMean)
