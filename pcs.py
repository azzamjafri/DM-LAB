import numpy as np

def standardize(table):
    avgs = []
    sds=[]
    num = len(table[0])
    for i in range(num):
        avg = sum([ table[s][i] for s in range(len(table)) ])/len(table)
        avgs.append(avg)
        sd = (sum([ (table[s][i] - avg)**2 for s in range(len(table)) ])/len(table))**0.5
        sds.append(sd)
    for i in range(len(table)):
        for j in range(num):
            table[i][j] = (table[i][j] - avgs[j])/sds[j]
    print(table)
    return avgs, sds, table            

def covarianceMatrix(table, sds, avgs):
    cov_matrix=[]
    for i in range(len(table[0])):
        q = [0]*(len(table[0]))
        cov_matrix.append(q)
    for i in range(len(cov_matrix)):
        for j in range(len(cov_matrix[0])):
            if i==j:
                cov_matrix[i][i] = (sds[i])**2
            else:
                t = [(table[s][i] - avgs[i])*(table[s][j] - avgs[j]) for s in range(len(table)) ]
                cov_matrix[i][j] = (sum([ (table[s][i] - avgs[i])*(table[s][j] - avgs[j]) for s in range(len(table)) ])/len(table))**0.5
    return cov_matrix
    
def eigenvalvec(cov_matrix):
    cov_matrix = np.array(cov_matrix)
    return np.linalg.eigh(cov_matrix)

def printTopK(eigenvalues, eigenvectors, k):
    print("\n\n")
    print("**********************************************")
    print("ALL EIGENVALUES AND EIGENVECTORS")
    print("**********************************************")
    print()
    for i in range(len(eigenvalues)):
        print(i+1,") Eigenvalue : ",eigenvalues[i])
        print("EigenVector : ",eigenvectors[:,i])
        print("")
    print("**********************************************")
    print("Top K eigen vectors")
    print("**********************************************")
    print()
    for i in range(k):
        print(i+1,") Eigenvalue : ", eigenvalues[i])
        print("EigenVector", eigenvectors[:,i])
        print("")
        
f= open('data.txt')
top_k = int(f.readline())
table=[]

for i in f:
    read = i.split()
    table.append([float(s) for s in read])

avgs,sds,table = standardize(table)
cov_matrix = covarianceMatrix(table, sds, avgs)
# print(cov_matrix)
print("")
print("******************* COVARIANCE MATRIX *********************")
for i in cov_matrix:
    print(i)
eigenvalues, eigenvectors = eigenvalvec(cov_matrix)
printTopK(eigenvalues, eigenvectors, top_k)

   
