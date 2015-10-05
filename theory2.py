import pickle
import numpy as np
import dot_temp as dt

def examine(a1,b1,x1,wordVec,lookup,rev):
    print a1 +" is to "+b1+" as "+ x1 +" is to "
    x = wordVec[lookup[x1]]
    a = wordVec[lookup[a1]]
    b = wordVec[lookup[b1]]

    mull,score2=dt.cosmul_test(wordVec,x,a,b,[lookup[x1],lookup[a1],lookup[b1]])
    add,score1=dt.cosadd_test(wordVec,x,a,b,[lookup[a1],lookup[b1],lookup[x1]])
    score1 = np.ndarray.flatten(score1)
    score2 = np.ndarray.flatten(score2)
    for ad,mul,i in zip(add,mull,xrange(5)):
        print "Place", i, ":\n" + "Add: "+rev[ad] + "||", score1[i]
        print "Mul: "+rev[mul] + "||", score2[i]
        if i == 3:
            break
for i in ["0.p","1.p","2.p","3.p"]:
    print i
    data = pickle.load(open(i,"rb"))
    words = data[:,0]
    lookup = {words[v]:v for v in xrange(len(words))}
    rev = {v:k for k,v in lookup.iteritems()}
    temp = data[:,1:].astype(np.float)
    wordVec = np.multiply(temp,np.reciprocal(np.linalg.norm(temp,axis = 1).reshape(400000,1)))


    examine("london","england","baghdad",wordVec,lookup,rev)
    print "-----------------------------------------------"
    examine("biology","chemistry","physics",wordVec,lookup,rev)
    print "-----------------------------------------------"
    examine("couch","tv","towel",wordVec,lookup,rev)
    print "-----------------------------------------------"
    examine("tv","couch","beach",wordVec,lookup,rev)
    print "-----------------------------------------------"
    examine("medicine","pharmacy","food",wordVec,lookup,rev)
    print "-----------------------------------------------"
    examine("pharmacy","medicine","restaurant",wordVec,lookup,rev)
    print "-----------------------------------------------"
    examine("run","ran","travel",wordVec,lookup,rev)
    print "-----|----------------|-----------|-------------"
    print "-----|----------------|-----------|------------"
    print "-----|----------------|-----------|------------"
    print "-----|----------------|-----------|------------"
