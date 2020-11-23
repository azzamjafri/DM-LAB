import csv
def getValuesFromCsv(path):
    f = open( path , 'r')
    data = csv.reader(f)
    csvData = {}
    for row in data:
        csvData[row[0]] = row[1].split()
    return csvData

data = getValuesFromCsv("datafile.txt")
#print(data)
for item in data:
    print(item, data[item])
    #print(data[item])

def createL1(data):
    L1 = {}
    for key in data:
        l = data[key]
        for i in l:
            if i in L1:
                count = L1[i]
                count += 1
                L1[i] = count
            else:
                L1[i] = 1
    return L1

L1 = createL1(data)
print("L1 table")
for item in L1:
    print(item, L1[item])


def prune(l, minSup):
    keysToDelete = []
    for key in l:
        if (l[key] < minSup):
            keysToDelete.append(key)

    for key in keysToDelete:
        del (l[key])
    return l


def apriori(data, L1, minSup):
    kTables = {}
    k = 2
    print("l1:", L1)
    c = prune(L1, minSup)
    print("c1:", c)
    kTables[1] = c
    while (True):
        l = join(c, data, k)
        print("l" + str(k) + ":", l)
        c = prune(l, minSup)
        print("c" + str(k) + ":", c)
        if (len(c) == 0):
            break
        kTables[k] = c
        k += 1
    print("\nFinal Answer:")
    print(kTables[k - 1])


def join(c, data, k):
    keys = [*c.keys()]
    keys.sort()

    newKeys = []
    l = len(keys)

    for i in range(0, l):
        startKey = keys[i]
        startKeySplit = startKey.split(",")

        for j in range(i + 1, l):
            nextKey = keys[j]
            nextKeySplit = nextKey.split(",")
            if (compare(startKeySplit, nextKeySplit, k)):
                nK = createNewKey(startKeySplit, nextKeySplit)
                if nK not in newKeys:
                    newKeys.append(nK)

    l = createL(newKeys, data)
    return l


def compare(key1, key2, k):
    matchCount = 0
    for l in key1:
        if l in key2:
            matchCount += 1
    return (matchCount >= (k - 2))


def createNewKey(key1, key2):
    for l in key1:
        if l not in key2:
            key2.append(l)
    key2.sort()
    return ",".join(key2)


def createL(newKeys, data):
    l = {}
    for key in newKeys:
        keySplit = key.split(",")
        count = 0
        for dKey in data:
            listToCheck = data[dKey]
            flag = True
            for k in keySplit:
                if k not in listToCheck:
                    flag = False
                    continue
            if (flag):
                count += 1
        l[key] = count
    return l


minSup = 2
print("Minimum Support:", minSup)
apriori(data, L1, minSup)