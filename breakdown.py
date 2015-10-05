import os

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def pprint(collection):
    for i in xrange(4):
        print i,".p dataset:"
        print "google\t\t\t\t \t \t msr"
        print "sem =", collection["google"][i]["sem"], "\t", collection["msr"][i]["sem"]
        print collection["google"][i]["sem"][0]/collection["google"][i]["sem"][1]
        print "syn =", collection["google"][i]["syn"], "\t", collection["msr"][i]["syn"]
        print collection["google"][i]["syn"][0]/collection["google"][i]["syn"][1]

folder = "google"
files = [folder+"/"+f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder,f))]

def examine(x):
    i = -1
    collection = {'google' : [], 'msr' : []}
    syn = "gram"
    with open(x,"r") as f:
        for l in f:
            if "total" in l:
                continue
            if ".p" in l:
                i += 1
                collection["google"].append({})
                collection["msr"].append({})
                collection["google"][i]['syn'] = [0.,0.]
                collection["google"][i]['sem'] = [0.,0.]
                collection["msr"][i]['syn'] = [0.,0.]
                collection["msr"][i]['sem'] = [0.,0.]
            elif "running" in l:
                continue
            elif "txt" in l:
                sem = True
                if syn in l:
                    sem = False
                folder = l.split('/')[-2]
                coming = True
                fi = l.split('/')[-1].replace("\n","")
                length = file_len(folder+"/"+fi)
            elif coming:
                correct = float(l)*length
                if sem:
                    entry = 'sem'
                else:
                    entry = 'syn'
                collection[folder][i][entry][0] += correct
                collection[folder][i][entry][1] += length
                coming = False
            else:
                continue
    pprint(collection)

cosmult = open("results_cosmult.txt")
cosadd = open("results_dot_full.txt")


data = {}
for lmult,ladd in zip(cosmult,cosadd):
    if "home/" in ladd:
        add = True
        folder = ladd.split('/')[-1]
        if folder not in data:
            data[folder] = []
    if "0." in ladd and "p" not in ladd and add:
        data[folder].append(float(lmult) - float(ladd))
        add=False


for k in data:
    print k + " " + str(data[k])






