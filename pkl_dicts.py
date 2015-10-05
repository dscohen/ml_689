import numpy as np
import pandas as pd
import os
import pickle

infile = map(os.path.expanduser,[ '~/Data/mini1/glove.6B.50d.txt' ,
                                 '~/Data/mini1/glove.6B.100d.txt' ,
                                 '~/Data/mini1/glove.6B.200d.txt' ,
                                  '~/Data/mini1/glove.6B.300d.txt'] )
i = 0
for fil in infile:
    df = pd.read_csv(fil,header=None,sep=r"\s+",index_col=0)
    vectors = df.as_matrix()
    words = df.index.get_values()
    df = 0
    #save as super matrix
    pickle.dump(np.column_stack((words,vectors)),open(str(i)+'.p','wb'))
    i += 1




