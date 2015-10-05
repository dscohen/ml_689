import numpy as np
import scipy.spatial
import pickle
import os
import time
import numpy.core._dotblas

def cosadd(wordVec,x,a,b,ind):
    vec = x-a+b
    vec = np.reshape(vec,(vec.size,1))
    result = np.dot(wordVec,vec)
    for i in ind:
        result[i] = -float('Inf')
    return np.argmax(result)

def cosmul(wordVec,x,a,b,ind):
    def convert(x):
	return (x+1)/2.
    result = (convert(np.dot(wordVec,x)) * convert(np.dot(wordVec,b)))*(np.reciprocal((convert(np.dot(wordVec,a)))+0.001))
    for i in ind:
        result[i] = -float('Inf')
    return np.argmax(result)

def cosadd_test(wordVec,x,a,b,ind):
    vec = x-a+b
    vec = np.reshape(vec,(vec.size,1))
    result = np.dot(wordVec,vec)
    for i in ind:
        result[i] = -float('Inf')
    result = -result
    indices=np.argsort(np.ndarray.flatten(result))[0:5]
    indices = np.ndarray.flatten(indices)
    return indices,result[np.ix_(indices)]


def cosmul_test(wordVec,x,a,b,ind):
    def convert(x):
	return (x+1)/2.
    result = (convert(np.dot(wordVec,x)) * convert(np.dot(wordVec,b)))*(np.reciprocal((convert(np.dot(wordVec,a)))+0.001))
    for i in ind:
        result[i] = -float('Inf')
    result = -result
    indices=np.argsort(np.ndarray.flatten(result))[0:5]
    indices = np.ndarray.flatten(indices)
    return indices,result[np.ix_(indices)]

def run(folder,wordVec,lookup,rev,distance):
    print "running google"
    correct = 0.
    total = 0.
    files = [folder+"/"+f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder,f))]
    for fil in files:
        file_correct = 0.
        file_total = 0.
        print fil
        f = open(fil,"r")
        for line in f:
            line = line.split()
            result = rev[distance(wordVec,wordVec[lookup[line[2]],:],wordVec[lookup[line[0]],:],
                                  wordVec[lookup[line[1]],:],[lookup[line[2]],lookup[line[0]],
                                                                     lookup[line[1]]])]
            total += 1
            file_total +=1
            # print str(line) + "::: " + result
            if (result == line[3]):
                correct += 1
                file_correct += 1
        print file_correct/file_total
    print "total: "
    return correct/total


def ex():
    for i in (["0.p","1.p","2.p","3.p"]):
        print "running " + i
        data = pickle.load(open(i,"rb"))
        words = data[:,0]
        lookup = {words[v]:v for v in xrange(len(words))}
        rev = {v:k for k,v in lookup.iteritems()}
        temp = data[:,1:].astype(np.float)
        wordVec = np.multiply(temp,np.reciprocal(np.linalg.norm(temp,axis = 1).reshape(400000,1)))
        d = 0
        temp = 0


        google_dir = os.path.expanduser("~/Data/mini1/google")
        msr_dir = os.path.expanduser("~/Data/mini1/msr")

        print run(google_dir,wordVec,lookup,rev,cosmul)
        print run(msr_dir   ,wordVec,lookup,rev,cosmul)



if __name__ == '__main__':
    ex()



