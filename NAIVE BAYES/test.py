import csv
import math
import random
import pandas as pd
pd.read_csv(r"play_tennis.csv")

def loadcsv(filename):
    lines=csv.reader(open(r"play_tennis.csv"))
    dataset=list(lines)
    for i in range(1,len(dataset)):
        dataset[i]=[x for x in dataset[i]]
    return dataset
def splitdataset(dataset,splitratio):
    trainsize=int(len(dataset)*splitratio)
    trainset=[]
    copy=list(dataset)
    while len(trainset)<trainsize:
        index=random.randrange(len(copy))
        trainset.append(copy.pop(index))
    return [trainset,copy]
def separatebyclass(dataset):
    separated={}
    for i in range(len(dataset)):
        vector=dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]]=[]
        separated[vector[-1]].append(vector)
    return separated
def mean(numbers):
    print(sum(numbers))
    return sum(numbers)/float(len(numbers))

def stdev(numbers):
    avg=mean(numbers)
    variance=sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)

def summarize(dataset):
    summaries=[(mean(attribute),stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries

def summarizedbyclass(dataset):
    separated=separatebyclass(dataset)
    # print(separated)
    summaries={}
    for classvalue,instances in separated.items():
        summaries[classvalue]=summarize(instances)
    # print(summaries)
    return summaries

def calculateprobability(x,mean,stdev):
    exponent=math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1/(math.sqrt(2*math.pi)*stdev))*exponent

def calculateclassprobabilities(summaries,inputvector):
    probabilities={}
    for classvalue,classsummaries in summaries.items():
        probabilities[classvalue]=1
        for i in range(len(classsummaries)):
            mean,stdev=classsummaries[i]
            x=inputvector[i]
            probabilities[classvalue]*=calculateprobability(x,mean,stdev)
        return probabilities

def predict(summaries,inputvector):
    probabilities=calculateclassprobabilities(summaries,inputvector)
    bestlabel,bestprob=None,-1
    for classvalue,probabilty in probabilities.items():
        if bestlabel is None or probabilty>bestprob:
            bestprob=probability
            bestlabel=classvalue
    return bestlabel

def getaccuracy(testset,predictions):
    correct=0
    for x in range(len(testset)):
        if testset[x][-1]==predictions[x]:
            correct+=1
    return(correct/float(len(testset)))*100.0

def main():
    filename=r"play_tennis.csv"
    splitratio=0.67
    dataset=loadcsv(filename)
    print(dataset)
    trainingset,testset=splitdataset(dataset,splitratio)
    print("Split {0} rows into train = {1} and test = {2} rows".format(len(dataset),len(trainingset),len(testset)))
    
    #preparemodel
    summaries=summarizedbyclass(trainingset)
    #testmodel
    predictions=predict(summaries,testset)
    accuracy=getaccuracy(testset,predictions)
    print("Accuracy:{0}%".format(accuracy))
    
main()