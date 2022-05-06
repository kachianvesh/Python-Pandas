import pandas as pd
import numpy as np
from sklearn import preprocessing
x=np.array([[1,2,3,4],[11,22,33,36],[45,52,23,36]])
print(x)
print('-----Lets apply normalization-----')
data_normalized = preprocessing.normalize(x, norm  = 'l2')
print ("\nL1 normalized data =\n ", data_normalized)